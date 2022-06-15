import json
from pymongo import MongoClient
import jsonschema as jsonSchema

client = MongoClient("mongodb://localhost:27017/")
db = client["test"]
coll = db["companies"]

def separate():
    print("_______________________________________________________________________")

while True:
    option = input("Selecciona una opció (1-8): ")

    if int(option) == 1:
        print("EXERCICI 1")
        print(" ")

        # aux = coll.create_index({"products."})
        aux = coll.find({"$expr": {"$gt": [{"$size": "$products"}, 4]}})
        cont = 0
        print("Cerca realitzada. Mostrant les 10 primeres companyies del llistat: ")
        for i in aux:
            if cont < 10:
                print(i["name"])
                cont += 1
            else:
                break

        print(" ")
        separate()

    elif int(option) == 2:
        print("EXERCICI 2")
        print(" ")

        aux = coll.aggregate([{"$group": {"_id": "$name", "count": {"$sum": 1}}}])
        print("Cerca realitzada. Mostrant les 10 primeres companyies del llistat: ")

        cont = 0
        for i in aux:
            if cont < 10:
                if i["count"] > 1:
                    print(i["_id"], "- número d'aparicions: ", i["count"])
                    cont += 1
            else:
                break

        print(" ")
        separate()

    elif int(option) == 3:
        print("EXERCICI 3")
        print(" ")

        aux = coll.aggregate(
            [{"$addFields": {"totalProducts": {"$size": "$products"}}}, {"$sort": {"totalProducts": -1}}])
        print("Cerca realitzada. Mostrant (de més a menys) les 10 primeres companyies del llistat: ")

        cont = 0
        for i in aux:
            if cont < 10:
                print(i["name"], "- número de productes: ", len(i["products"]))
                cont += 1
            else:
                break

        print(" ")
        separate()

    elif int(option) == 4:
        print("EXERCICI 4")
        print(" ")

        companies = coll.find({"partners": {"$gt": {"$size": 0}}}).limit(10)
        print("Mostrant les 10 primeres companyies del llistat: ")
        for company in companies:
            print(company["name"])

        print(" ")
        separate()

    elif int(option) == 5:
        print("EXERCICI 5")
        print(" ")

        companies = coll.find({"acquisitions": {"$size": 3}}).limit(10)
        print("Mostrant les 10 primeres companyies del llistat: ")
        for company in companies:
            print(company["name"])

        print(" ")
        separate()

    elif int(option) == 6:
        print("EXERCICI 6")
        print(" ")

        companies = coll.find({"category_code": "advertising", "competitions.3": {"$exists": True}}).limit(10)
        print("Mostrant les 10 primeres companyies del llistat: ")
        for company in companies:
            print(company["name"])

        print(" ")
        separate()

    elif int(option) == 7:
        print("EXERCICI 7")
        print(" ")

        print(" ")
        separate()

    elif int(option) == 8:
        print("EXERCICI 8")
        print(" ")

        print("Per a validar els camps podem crear un validator amb jsonSchema.")
        print("A continuació es defineix un validator (company_validator).")

        company_validator = {
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["name", "permalink", "number_of_employees", "founded_year", "email_address", "created_at",
                             "updated_at", "acquisition"],
                "properties": {
                    "name": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "permalink": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "number_of_employees": {
                        "bsonType": "int"
                    },
                    "founded_year": {
                        "bsonType": "int"
                    },
                    "email_address": {
                        "bsonType": "string",
                        "pattern": "/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/"
                    },
                    "created_at": {
                        "bsonType": "date"
                    },
                    "updated_at": {
                        "bsonType": "date"
                    },
                    "acquisition": {
                        "bsonType": "object",
                        "properties": {
                            "price_amount": {
                                "bsonType": "double",
                                "description": "must be a double and is required"
                            },
                            "price_currency_code": {
                                "bsonType": "string",
                                "description": "must be a string and is required"
                            },
                            "acquired_year": {
                                "bsonType": "double",
                                "description": "must be a double and is required"
                            }
                        }
                    }
                }
            }
        }

        print("Finalment, executem el validator.")
        db.command("collMod", "companies", validator=company_validator)

        print(" ")
        print("S'han afegit les regles de validació a la col·lecció.")

        print(" ")
        separate()

    else:
        break
