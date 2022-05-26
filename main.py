import json
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["test"]
coll = db["companies"]

def print_value_key(collection, field, key, value):  # funcion que ayuda a imprimir el valor de una field con una condicion de key
    base = collection.find({})
    for d in base:
        if d[field] == key:
            valor = str(d[value])
            print("El valor de " + value + " es " + valor)

def separate():
    print("_______________________________________________________________________")

# EJERCICIO 1
print("EJERCICIO 1")
print(" ")

#aux = coll.create_index({"products."})
aux = coll.find( {"$expr": {"$gt":[{"$size":"$products"}, 4]} } )
cont = 0
print("Busqueda realizada. Imprimiendo solo 10 compañias del listado: ")
for i in aux:
    if cont < 10:
        print(i["name"])
        cont+=1
    else:
        break

print(" ")
separate()

# EJERCICIO 2
print("EJERCICIO 2")
print(" ")

aux = coll.aggregate([{"$group" : {"_id" : "$name", "count" : {"$sum" : 1}}}])
print("Busqueda realizada. Imprimiendo solo 10 compañias del listado: ")

cont = 0
for i in aux:
    if cont < 10:
        if i["count"] > 1:
            print(i["_id"], ",veces que aparece: ", i["count"])
            cont += 1
    else:
        break

print(" ")
separate()

# EJERCICIO 3
print("EJERCICIO 3")
print(" ")

aux = coll.aggregate([ {"$addFields" : {"totalProducts" : {"$size" : "$products"}}} , {"$sort" : {"totalProducts" : -1}} ])
print("Busqueda realizada. Imprimiendo (de más a menos) solo 10 compañias del listado: ")

cont = 0
for i in aux:
    if cont < 10:
        print(i["name"], ",numero de productos: ", len(i["products"]))
        cont += 1
    else:
        break

print(" ")
separate()

# EJERCICIO 4
print("EJERCICIO 4")
print(" ")

companies = coll.find({"partners": {"$gt": {"$size": 0}}}).limit(10)
print("Mostrant 10 de les companyies: ")
for company in companies:
    print(company["name"])

print(" ")
separate()

# EJERCICIO 5
print("EJERCICIO 5")
print(" ")

companies = coll.find({"acquisitions": {"$size": 3}}).limit(10)
print("Mostrant 10 de les companyies: ")
for company in companies:
    print(company["name"])

print(" ")
separate()

# EJERCICIO 6
print("EJERCICIO 6")
print(" ")

companies = coll.find({"category_code": "advertising", "competitions.3": {"$exists": True}}).limit(10)
print("Mostrant 10 de les companyies: ")
for company in companies:
    print(company["name"])

print(" ")
separate()

# EJERCICIO 7
print("EJERCICIO 7")
print(" ")



print(" ")
separate()

# EJERCICIO 8
print("EJERCICIO 8")
print(" ")



print(" ")
separate()