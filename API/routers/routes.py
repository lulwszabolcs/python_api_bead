from schemas.schema import User, Basket, Item
from fastapi.responses import JSONResponse
from fastapi import HTTPException, APIRouter
from data.filehandler import add_user, add_basket, add_item_to_basket, save_json, remove_item_from_basket
from data.filereader import get_user_by_id, get_basket_by_user_id, get_all_users, get_total_price_of_basket, load_json

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

@routers.post('/adduser',summary="Add a new User",response_model=User)
def adduser(user: User) -> User:
    try:
        userToAdd = user.model_dump()
        add_user(userToAdd)
        return JSONResponse(content=userToAdd,status_code=201)
    except ValueError:
        raise HTTPException(status_code=404,detail="Error adding a new User")

@routers.post('/addshoppingbag')
def addshoppingbag(userid: int) -> str:
    ...

@routers.post('/additem')
def additem(userid: int, item):
    pass

@routers.put('/updateitem')
def updateitem(userid: int, itemid: int, updateItem):
    pass

@routers.delete('/deleteitem',summary="Delete an item from an User's basket")
def deleteitem(userid: int, itemid: int) -> Basket:
    try:
       remove_item_from_basket(userid,itemid)
       return get_basket_by_user_id(userid)[0]
    except ValueError:
        raise HTTPException(status_code=404,detail="Error while item delete")

@routers.get('/user',summary="Get an User by user_id",response_model=User) 
def user(userid: int) -> User:
   try:
        user = get_user_by_id(userid)   
        return JSONResponse(content=user,status_code=200)
   except ValueError:
        raise HTTPException(status_code=404,detail="No user with given ID")

@routers.get('/users',summary="Get all the users",response_model=User)
def users() -> list[User]:
    try:
        all_users = get_all_users()
        return JSONResponse(content=all_users,status_code=200)
    except ValueError:
        raise HTTPException(status_code=418,detail="Cannot get the list of Users")

@routers.get('/shoppingbag',summary="Get a basket of an User",response_model=Basket)
def shoppingbag(userid: int) -> list[Item]:
    try:
        basket_of_user = get_basket_by_user_id(userid)
        return JSONResponse(content=basket_of_user,status_code=200)
    except ValueError:
        raise HTTPException(status_code=404,detail="No basket with given ID")


@routers.get('/getusertotal',summary="Get the total price of an User")
def getusertotal(userid: int) -> float:
    try:
        total_price = get_total_price_of_basket(userid)
        return JSONResponse(content=total_price,status_code=200)
    except ValueError:
        raise HTTPException(status_code=404,detail="No total price with given ID")

    
