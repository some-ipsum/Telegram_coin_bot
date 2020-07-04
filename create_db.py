import sqlite3
import json

db = sqlite3.connect('Account.db')
cur = db.cursor()
    # Создаем таблицу
cur.execute("""CREATE TABLE IF NOT EXISTS Account (
    ID INTEGER PRIMARY KEY,
    PHONE TEXT,
    PASS TEXT,
    API_ID TEXT,
    API_HASH TEXT,
    ACTIVITY TEXT,
    LITECOIN TEXT
)""")

db.commit()


def import_from_json(path):
    #если хотите импортировать переменные из json файла, то используйте эту функцию, как  должна выглядить файл смотрите в json_example.json
    with open(path) as f:
        data = json.loads(f.read())
        cur.execute(f"SELECT PHONE FROM Account WHERE PHONE = '{data[0]['Phone']}'")
        if cur.fetchone() is None:
            for var in data:
                print("Зарегистрированно!")
                cur.execute("""INSERT INTO Account(PHONE, PASS, API_ID, API_HASH, ACTIVITY, LITECOIN) VALUES (?,?,?,?,?,?);""", (var['Phone'], var['password'], var['Api_id'], var['Api_hash'], var['Activity'], var['Litecoin']))
                db.commit()
                

Phone = "+88005553535"
password = "13236546460"
Api_id = "1488"
Api_hash = "05xxxxxxx45xxxxxxx435xxxxx435xxxxxxx9"
Activity = "ON"
Litecoin = "ltc1qlhs4e459wwtu8sx7a4rtumtffs9lr4ktmfl6ny"

cur.execute(f"SELECT PHONE FROM Account WHERE PHONE = '{Phone}'")
if cur.fetchone() is None:
    cur.execute("""INSERT INTO Account(PHONE, PASS, API_ID, API_HASH, ACTIVITY, LITECOIN) VALUES (?,?,?,?,?,?);""", (Phone, password, Api_id, Api_hash, Activity, Litecoin))
    db.commit()
    print("Зарегистрированно!")
    for value in cur.execute("SELECT * FROM Account"):
        print(value)