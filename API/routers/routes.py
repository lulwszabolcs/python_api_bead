#from schemas.schema import User, Basket, Item
from fastapi.responses import JSONResponse
from fastapi import HTTPException, APIRouter
#from data.filehandler import add_user, add_basket, add_item_to_basket, save_json
#from data.filereader import get_user_by_id, get_basket_by_user_id, get_all_users, get_total_price_of_basket, load_json

'''

Útmutató a fájl használatához:

- Minden route esetén adjuk meg a response_modell értékét (típus)
- Ügyeljünk a típusok megadására
- A függvények visszatérési értéke JSONResponse() legyen
- Minden függvény tartalmazzon hibakezelést, hiba esetén dobjon egy HTTPException-t
- Az adatokat a data.json fájlba kell menteni.
- A HTTP válaszok minden esetben tartalmazzák a 
  megfelelő Státus Code-ot, pl 404 - Not found, vagy 200 - OK

'''

routers = APIRouter()

@routers.post('/adduser')
def adduser(user):
    pass

@routers.post('/addshoppingbag')
def addshoppingbag(userid: int) -> str:
    pass

@routers.post('/additem')
def additem(userid: int, item):
    pass

@routers.put('/updateitem')
def updateitem(userid: int, itemid: int, updateItem):
    pass

@routers.delete('/deleteitem')
def deleteitem(userid: int, itemid: int):
   pass

@routers.get('/user')
def user(userid: int):
   pass

@routers.get('/users')
def users():
    pass

@routers.get('/shoppingbag')
def shoppingbag(userid: int):
    pass

@routers.get('/getusertotal')
def getusertotal(userid: int) -> float:
    pass
