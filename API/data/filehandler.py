import json
import os
from typing import Dict, Any
from schemas.schema import Item

'''
Útmutató a fájl függvényeinek a használatához

Új felhasználó hozzáadása:

new_user = {
    "id": 4,  # Egyedi felhasználó azonosító
    "name": "Szilvás Szabolcs",
    "email": "szabolcs@plumworld.com"
}

Felhasználó hozzáadása a JSON fájlhoz:

add_user(new_user)

Hozzáadunk egy új kosarat egy meglévő felhasználóhoz:

new_basket = {
    "id": 104,  # Egyedi kosár azonosító
    "user_id": 2,  # Az a felhasználó, akihez a kosár tartozik
    "items": []  # Kezdetben üres kosár
}

add_basket(new_basket)

Új termék hozzáadása egy felhasználó kosarához:

user_id = 2
new_item = {
    "item_id": 205,
    "name": "Szilva",
    "brand": "Stanley",
    "price": 7.99,
    "quantity": 3
}

Termék hozzáadása a kosárhoz:

add_item_to_basket(user_id, new_item)

Hogyan használd a fájlt?

Importáld a függvényeket a filehandler.py modulból:

from filehandler import (
    add_user,
    add_basket,
    add_item_to_basket,
)

 - Hiba esetén ValuErrort kell dobni, lehetőség szerint ezt a 
   kliens oldalon is jelezni kell.

'''

JSON_DIR = os.path.dirname(__file__)


JSON_FILE_PATH = os.path.join(os.path.dirname(__file__), "data.json")

def load_json() -> Dict[str, Any]:
    with open(JSON_FILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)

def save_json(data: Dict[str, Any]) -> None:
    with open(JSON_FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def load_json_file(filename: str) -> Dict[str, Any]:
    file_path = os.path.join(JSON_DIR, filename)

    with open(file_path,"r",encoding="utf-8") as file:
        return json.load(file)

def save_json_file(data: Dict[str, Any], filename: str) -> None:
    file_path = os.path.join(JSON_DIR, filename)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        
def add_user(user: Dict[str, Any]) -> None:
    data = load_json()
    data["Users"].append(user)
    save_json(data)

def _get_last_basket_id() -> int:
    data = load_json()
    baskets = data.get("Baskets", [])
    
    if not baskets:
        return 0
    
    last_basket = baskets[-1]
    return last_basket["id"]
         
def add_basket(userid: int) -> None:
    data = load_json()
    for basket in data["Baskets"]:
        if (basket["user_id"] == userid):
            raise ValueError("Mar van kosara a felhasznaloknak.")
    new_basket = {
        "id": _get_last_basket_id() + 1,  # Egyedi kosár azonosító
        "user_id": userid,  # Az a felhasználó, akihez a kosár tartozik
        "items": []  # Kezdetben üres kosár
    }
    data["Baskets"].append(new_basket)
    save_json(data)

def add_item_to_basket(user_id: int, item: Dict[str, Any]) -> None:
    data = load_json()
    for basket in data["Baskets"]:
        if (basket["user_id"] == user_id):
            basket.get("items").append(item)
            save_json(data)
            return
    raise ValueError("Hiba a termek kosarba helyezese kozben!")
        
def remove_item_from_basket(userid: int, itemid: int):
    data = load_json()
    item_deleted = False
    for basket in data["Baskets"]:
        if basket["user_id"] == userid:
            original_count = len(basket["items"])
            basket["items"] = [item for item in basket["items"] if item["item_id"] != itemid]
            if len(basket["items"]) < original_count:
                item_deleted = True
                break
    if item_deleted:
        save_json(data)
    else:
        raise ValueError("Hiba a torles kozben")
    
def update_item_in_basket(userid: int, itemid: int, updateItem: Item):
    data = load_json()
    item_replacement = updateItem.model_dump()
    for basket in data["Baskets"]:
        if basket["user_id"] == userid:
            for item in basket["items"]:
                if item["item_id"] == itemid:
                    basket["items"].remove(item)
                    basket["items"].append(item_replacement)
                    save_json(data)
                    return
    raise ValueError("Hiba a termek frissitese kozben")