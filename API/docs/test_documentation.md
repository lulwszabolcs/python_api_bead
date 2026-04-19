## User tesztek

| Teszteset neve | Leírás | Metódus | Végpont | Bemenet | Várt kimenet |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Új felhasználó hozzáadása** | Új felhasználó sikeres hozzáadása | **POST** | `/adduser` | Body: `{"id": 1, "name": "Kertész Géza", "email": "kertesz@inf.elte.hu"}` | `201 Created` + user objektum |
| *Hiba: Hiányzó adatok* | Regisztráció kötelező mezők (pl. név) nélkül | **POST** | `/adduser` | Body: `{"id": 2, "email": "teszt@teszt.hu"}` | `422 Unprocessable Entity` |
| **Egy felhasználó lekérdezése** | Egy konkrét felhasználó adatainak lekérése | **GET** | `/user` | Query param: `userid=1` | `200 OK` + user adatai |
| *Hiba: Nem létező user* | Nem létező ID lekérdezése | **GET** | `/user` | Query param: `userid=999` | `404 Not Found` |
| **Összes felhasználó listája** | Az összes regisztrált felhasználó kilistázása | **GET** | `/users` | - | `200 OK` + lista |
| *Hiba: Szerver/Lekérdezés hiba* | Adatbázis hiba az összes felhasználó lekérésekor | **GET** | `/users` | - | `418 I'm a teapot` |
| **Felhasználó fizetendője** | A felhasználó kosarának végösszege | **GET** | `/getusertotal` | Query param: `userid=1` | `200 OK` + összeg |
| *Hiba: Üres/Nem létező kosár* | Összeg lekérése kosár nélkül | **GET** | `/getusertotal` | Query param: `userid=999` | `404 Not Found` |

---

## Basket tesztek

| Teszteset neve | Leírás | Metódus | Végpont | Bemenet | Várt kimenet |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Kosár hozzáadása** | Bevásárlókosár rendelése egy felhasználóhoz | **POST** | `/addshoppingbag` | Query param: `userid=1` | `200 OK` + Tájékoztató üzenet |
| *Hiba: Duplikált kosár* | Már létező kosár újra létrehozása | **POST** | `/addshoppingbag` | Query param: `userid=1` | `404 Not Found` |
| **Kosár lekérdezése** | Egy felhasználó aktuális kosarának tartalma | **GET** | `/shoppingbag` | Query param: `userid=1` | `200 OK` + kosár adatai |
| *Hiba: Hiányzó kosár* | Nem létező felhasználó/kosár lekérése | **GET** | `/shoppingbag` | Query param: `userid=999` | `404 Not Found` |

---

## Item tesztek

| Teszteset neve | Leírás | Metódus | Végpont | Bemenet | Várt kimenet |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Áru hozzáadása** | Termék kosárba helyezése | **POST** | `/additem` | Query: `userid=1`<br>Body: `{"item_id": 5, "name": "Szilva", "brand": "Stanley", "price": 10.5, "quantity": 2}` | `200 OK` + frissített kosár |
| *Hiba: Nem létező kosár/user* | Termék hozzáadása rossz azonosítóval | **POST** | `/additem` | Query: `userid=999`<br>Body: Érvényes Item | `404 Not Found` |
| **Áru módosítása** | Kosárban lévő termék frissítése | **PUT** | `/updateitem` | Query: `userid=1, itemid=5`<br>Body: `{"item_id": 5, "name": "Szilva", "brand": "Stanley", "price": 10.5, "quantity": 5}` | `200 OK` + módosított kosár |
| *Hiba: Érvénytelen db* | Negatív mennyiség megadása | **PUT** | `/updateitem` | Query: `userid=1, itemid=5`<br>Body: `{"item_id": 5, "name": "Szilva", "brand": "Stanley", "price": 10.5, "quantity": -1}` | `422 Unprocessable Entity` |
| **Áru törlése** | Termék eltávolítása a kosárból | **DELETE** | `/deleteitem` | Query param: `userid=1, itemid=5` | `200 OK` + frissített kosár |
| *Hiba: Hiányzó elem* | Olyan elem törlése, ami nincs a kosárban | **DELETE** | `/deleteitem` | Query param: `userid=1, itemid=99` | `404 Not Found` |

---

## Egyéb tesztek

| Teszteset neve | Leírás | Metódus | Végpont | Bemenet | Várt kimenet |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Mentés** | Aktuális állapot perzisztálása (mentése) | **POST** | `/save` | Query param: `source="data.json"`, `dest="backup.json"` | `200 OK` + Siker üzenet |
| *Hiba: Forrásfájl nem található* | Mentés nem létező fájlból | **POST** | `/save` | Query param: `source="nincs.json"`, `dest="backup.json"` | `404 Not Found` |
| **Újratöltés** | Adatok frissítése/visszatöltése | **POST** | `/reload` | Query param: `dest="data.json"`, `source="backup.json"` | `200 OK` + Siker üzenet |
| *Hiba: Sikertelen reload* | Betöltési hiba forrás hiányában | **POST** | `/reload` | Query param: `dest="data.json"`, `source="nincs.json"` | `404 Not Found` |