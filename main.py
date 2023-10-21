from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import dns.resolver
import certifi
ca = certifi.where()

dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']

uri = "mongodb+srv://YOURMONGOUSERNAME:YOURMONGODBPASSWORDHERE@cluster0.6nqbmqw.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=ca, server_api=ServerApi('1'))
db = client["Cluster0"]  # Adatbázis neve
collection = db["products"]
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


class AllProductsPopup(Popup):
    def __init__(self, product_list, **kwargs):
        super(AllProductsPopup, self).__init__(**kwargs)
        self.title = "Összes termék"

        layout = GridLayout(cols=1, spacing=10, size_hint=(1, 1))

        scroll_view = ScrollView()
        scroll_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        scroll_layout.bind(minimum_height=scroll_layout.setter('height'))

        self.product_buttons = []

        for product in product_list:
            name, description = product[0], product[1]
            product_button = Button(text=name)
            product_button.bind(
                on_press=lambda button, name=name, description=description: self.show_product_description(name,
                                                                                                          description))
            delete_button = Button(text="Törlés")
            delete_button.bind(
                on_press=lambda button, name=name: self.delete_product(name))

            product_layout = GridLayout(cols=3, spacing=10, size_hint_y=None)
            product_layout.add_widget(product_button)
            product_layout.add_widget(delete_button)
            scroll_layout.add_widget(product_layout)

            self.product_buttons.append((product_button, name))

        scroll_view.add_widget(scroll_layout)
        layout.add_widget(scroll_view)

        self.product_detail_label = TextInput(text="", readonly=True, multiline=True)
        layout.add_widget(self.product_detail_label)

        cancel_button = Button(text="Vissza", size_hint_y=1 / 5)
        cancel_button.bind(on_press=self.dismiss)
        layout.add_widget(cancel_button)

        self.content = layout

    def delete_product(self, name):
        # Törlés a MongoDB adatbázisból
        collection.delete_one({"name": name})

        # Frissítés: eltávolítjuk a törölt terméket a listából
        self.product_buttons = [(layout, product_name) for layout, product_name in self.product_buttons if
                                product_name != name]

        self.update_left_panel()

    def show_product_description(self, name, description):
        self.product_detail_label.text = f"Név: {name}\nTermék Specifikáció: {description}"

    def update_left_panel(self):
        if len(self.content.children) > 0:
            layout = self.content.children[0]

            if len(layout.children) > 0:
                # Töröljük a meglévő gombokat a layout-ból
                layout.clear_widgets()

                for product_layout, _ in self.product_buttons:
                    layout.add_widget(product_layout)

                # Frissítjük a részletek szövegmezőt az első termékhez
                if self.product_buttons:
                    product_button = self.product_buttons[0][0].children[0]
                    self.show_product_description(product_button.text, "")

                layout.add_widget(self.product_detail_label)


class UniProductDatabaseApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.qr_input = TextInput(hint_text="Termék neve", multiline=False, size_hint_y=1 / 5)
        layout.add_widget(self.qr_input)

        button_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))

        self.product_detail_button = Button(text="Keresés")
        self.product_detail_button.bind(on_press=self.show_product_detail)
        button_layout.add_widget(self.product_detail_button)

        self.add_product_button = Button(text="Termék hozzáadása")
        self.add_product_button.bind(on_press=self.show_add_product_popup)
        button_layout.add_widget(self.add_product_button)

        layout.add_widget(button_layout)

        self.product_description_input = TextInput(hint_text="Termék Specifikáció", multiline=True, readonly=True)
        layout.add_widget(self.product_description_input)

        self.all_products_button = Button(text="Összes termék", size_hint_y=1 / 5)
        self.all_products_button.bind(on_press=self.show_all_products)
        layout.add_widget(self.all_products_button)

        return layout

    def show_add_product_popup(self, instance):
        add_product_popup = AddProductPopup()
        add_product_popup.open()

    def show_product_detail(self, instance):
        try:
            query = self.qr_input.text.lower()
            result = collection.find_one({"name": query})

            if result:
                product_name = query
                product_description = result["description"]
                self.product_description_input.text = f"Név: {product_name}\nTermék Specifikáció: {product_description}"
            else:
                self.product_description_input.text = "Nincs találat."
        except Exception as er:
            print(er, "Empty description")
            self.product_description_input.text = "Nincs találat."
            pass

    def show_all_products(self, instance):
        # Lekérjük az összes terméket a MongoDB adatbázisból
        product_list = list(collection.find())

        if product_list:
            product_list = [(product["name"], product["description"]) for product in product_list]
        else:
            product_list = []

        all_products_popup = AllProductsPopup(product_list)
        all_products_popup.open()


class AddProductPopup(Popup):
    def __init__(self, **kwargs):
        super(AddProductPopup, self).__init__(**kwargs)
        self.title = "Termék hozzáadása"

        self.result_label = Label(text="")
        layout = BoxLayout(orientation='vertical')
        self.product_name_input = TextInput(hint_text="Termék neve")
        self.description_input = TextInput(hint_text="Termék Specifikáció")
        add_button = Button(text="Hozzáadás")
        add_button.bind(on_press=self.add_product)

        layout.add_widget(self.product_name_input)
        layout.add_widget(self.description_input)
        layout.add_widget(add_button)
        layout.add_widget(self.result_label)
        self.content = layout

        cancel_button = Button(text="Vissza")
        cancel_button.bind(on_press=self.dismiss)
        layout.add_widget(cancel_button)

    def add_product(self, instance):
        name = self.product_name_input.text
        description = self.description_input.text

        if name:
            # Hozzáadjuk a MongoDB adatbázishoz
            product = {"name": name, "description": description}
            collection.insert_one(product)

            self.product_name_input.text = ""
            self.description_input.text = ""
            self.result_label.text = "Termék hozzáadva."
        else:
            self.result_label.text = "Kérjük, töltse ki a név mezőt."


if __name__ == '__main__':
    UniProductDatabaseApp().run()
