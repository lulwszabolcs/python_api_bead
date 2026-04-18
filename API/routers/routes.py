from schemas.schema import User, Basket, Item
from fastapi.responses import JSONResponse
from fastapi import HTTPException, APIRouter
from data.filehandler import add_user, add_basket, add_item_to_basket, save_json, remove_item_from_basket, update_item_in_basket, save_json_file, load_json_file
from data.filereader import get_user_by_id, get_basket_by_user_id, get_all_users, get_total_price_of_basket, load_json
from typing import Dict, Any

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

@routers.post('/addshoppingbag',summary="Add a shopping bag to an User")
def addshoppingbag(userid: int) -> str:
    try:
        add_basket(userid)
        return JSONResponse(content="Sikeres kosár hozzárendelés!",status_code=200)
    except ValueError:
        raise HTTPException(status_code=404,detail="Error while adding new basket")

@routers.post('/additem',summary="Add item to an User's basket",response_model=Basket)
def additem(userid: int, item: Item) -> Basket:
    try:
        item_to_add = item.model_dump()
        add_item_to_basket(userid,item_to_add)
        return JSONResponse(content=get_basket_by_user_id(userid)[0],status_code=200)
    except:
        raise HTTPException(status_code=404,detail="Error while adding to basket")


@routers.put('/updateitem',summary="Update an item in a User's shopping bag")
def updateitem(userid: int, itemid: int, updateItem: Item) -> Basket:
    try:
        update_item_in_basket(userid,itemid,updateItem)
        return JSONResponse(content=get_basket_by_user_id(userid),status_code=200)
    except ValueError:
        raise HTTPException(status_code=404,detail="Error while item update")


@routers.delete('/deleteitem',summary="Delete an item from an User's basket",response_model=Basket)
def deleteitem(userid: int, itemid: int) -> Basket:
    try:
       remove_item_from_basket(userid,itemid)
       return JSONResponse(content=get_basket_by_user_id(userid)[0],status_code=200)
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
    
@routers.post('/save')
def save(source: str, dest: str):
    try:
        data: Dict[str, Any] = load_json_file(source)
        save_json_file(data, dest)

        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "message": f"Adatok sikeresen mentve",
                "source": source,
                "dest": dest
            }
        )
    except FileNotFoundError:
        raise HTTPException(status_code=404,detail=f"A file nem talalhato")

@routers.post('/reload')
def reload(dest: str, source: str):
    try:
        data: Dict[str, Any] = load_json_file(source)
        save_json_file(data, dest)
        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "message": f"Adatok sikeresen visszatöltve: {source} → {dest}",
                "source": source,
                "dest": dest
            }
        )
    except FileNotFoundError:
        raise HTTPException(status_code=404,detail=f"A file nem talalhato")