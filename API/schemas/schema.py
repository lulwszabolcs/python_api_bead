from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List

'''

Útmutató a fájl használatához:

Az osztályokat a schema alapján ki kell dolgozni.

A schema.py az adatok küldésére és fogadására készített osztályokat tartalmazza.
Az osztályokban az adatok legyenek validálva.
 - az int adatok nem lehetnek negatívak.
 - az email mező csak e-mail formátumot fogadhat el.
 - Hiba esetén ValuErrort kell dobni, lehetőség szerint ezt a 
   kliens oldalon is jelezni kell.

'''

ShopName='Bolt'

class Item(BaseModel):
    item_id: int
    @field_validator("item_id", mode="after")
    @classmethod
    def check_item_id(cls,item_id: int) -> int:
        if item_id < 0:
            raise ValueError("Hiba: Az item_id nem lehet negatív!")
        return item_id
    
    name: str
    brand: str
    price: float

    quantity: int
    @field_validator("quantity",mode="after")
    @classmethod
    def check_quantity(cls,quantity: int) -> int:
        if quantity < 0:
            raise ValueError("Hiba: A quantity nem lehet negatív!")
        return quantity


class Basket(BaseModel):
    id: int
    @field_validator("id",mode="after")
    @classmethod
    def check_id(cls,id: int) -> int:
        if id < 0:
            raise ValueError("Hiba: Az id (Kosar) nem lehet negatív!")
        return id
    
    user_id: int 
    @field_validator("user_id",mode="after")
    @classmethod
    def check_user_id(cls,user_id: int) -> int:
        if user_id < 0:
            raise ValueError("Hiba: Az user_id nem lehet negatív!")
        return user_id
    
    items: List[Item]


class User(BaseModel):
    id: int
    @field_validator("id",mode="after")
    @classmethod
    def check_id(cls,id: int) -> int:
        if id < 0:
            raise ValueError("Hiba: Az id (Felhasznalo) nem lehet negatív!")
        return id
    name: str
    email: EmailStr
