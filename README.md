## English Readme:

# Uni Product Database

Uni Product Database is a Python application built with the Kivy framework that enables users to interact with a product database stored in MongoDB. This application offers users the ability to search for products, add new ones, and view a list of all stored products.

### Features

- **Product Search**: Users can search for products by name, and the application provides detailed information about the product.

- **Add Products**: Users can add new products to the database, providing both a name and a description.

- **View All Products**: Users can access a list of all the products stored in the database.

### How It Works

The app uses the Kivy framework for the graphical user interface and connects to a MongoDB database to manage product data. When a user enters a product name and clicks the "Keresés" (Search) button, the app queries the database for the product's details. If the product exists, it displays its name and description; otherwise, it indicates that there's no match.

Users can add new products by clicking the "Termék hozzáadása" (Add Product) button, which opens a popup window for entering the product name and description. Clicking the "Hozzáadás" (Add) button saves the new product to the database.

To view all products, click the "Összes termék" (All Products) button, which displays a list of all the stored products. You can select a product from the list to see its details.

### Installation

Before running the app, make sure you have the required libraries installed. You'll also need to set up a MongoDB database and replace the `uri` variable with your MongoDB connection URI.

### Usage

1. Run the app by executing the script.
2. Enter a product name and click the "Keresés" (Search) button to find a product.
3. Click the "Termék hozzáadása" (Add Product) button to add new products.
4. Click the "Összes termék" (All Products) button to view a list of all stored products.

### Dependencies

- Kivy: An open-source Python framework for developing multitouch applications.
- pymongo: A Python driver for MongoDB, used for database operations.

## Hungarian Readme:

# Uni Product Database

Az Uni Product Database egy Python alkalmazás, amelyet a Kivy keretrendszer segítségével készítettek. Ez lehetővé teszi a felhasználók számára, hogy egy MongoDB adatbázisban tárolt termékadatokkal interakcióba lépjenek. Ez az alkalmazás lehetővé teszi a termékek keresését, új termékek hozzáadását és az összes tárolt termék listájának megtekintését.

### Funkciók

- **Termékkkeresés**: A felhasználók kereséseket végezhetnek terméknevek alapján, és az alkalmazás részletes információt nyújt a termékről.

- **Termékek hozzáadása**: A felhasználók új termékeket adhatnak hozzá az adatbázishoz, megadva a termék nevét és leírását.

- **Az összes termék megtekintése**: A felhasználók megtekinthetik az adatbázisban tárolt összes termék listáját.

Működés
Az alkalmazás a Kivy keretrendszert használja a grafikus felhasználói felülethez, és csatlakozik egy MongoDB adatbázishoz a termékadatok kezeléséhez. Amikor egy felhasználó beír egy terméknevet, majd megnyomja a "Keresés" gombot, az alkalmazás lekérdezi az adatbázist a termék részletekért. Ha a termék létezik, megjeleníti a nevét és leírását; ha nem, jelezni fogja, hogy nincs találat.

Az alkalmazás lehetőséget nyújt új termékek hozzáadására is. Ehhez meg kell nyomni a "Termék hozzáadása" gombot, ami egy felugró ablakot nyit meg a termék nevének és leírásának megadásához. A "Hozzáadás" gomb megnyomásával a rendszer elmenti az új terméket az adatbázisba.

Az összes termék megtekintéséhez meg kell nyomni az "Összes termék" gombot, amely megjeleníti az összes adatbázisban tárolt termék listáját. A listából kiválaszthat egy terméket a részletek megtekintéséhez.

Telepítés
Az alkalmazás futtatása előtt győződj meg róla, hogy telepítetted a szükséges könyvtárakat. Emellett be kell állítanod egy MongoDB adatbázist, és le kell cserélned a uri változót a saját MongoDB kapcsolati URI-dal.

Használat
Az alkalmazást a main.py fájl futtatásával indítsd el.
Add meg a termék nevét, majd nyomd meg a "Keresés" gombot a termék kereséséhez.
A "Termék hozzáadása" gombra kattintva adhatsz hozzá új termékeket.
Az "Összes termék" gombra kattintva megtekintheted az összes adatbázisban tárolt termék listáját.
