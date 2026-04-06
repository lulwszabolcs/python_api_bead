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
    name: str 
    brand: str
    price: float
    quantity: int


class Basket(BaseModel):
    id: int
    user_id: int 
    items: List[Item]


class User(BaseModel):
    id: int
    name: str
    email: str
