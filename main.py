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
separate()
print("EJERCICIO 1")
print(" ")



print(" ")
separate()

# EJERCICIO 2
separate()
print("EJERCICIO 2")
print(" ")



print(" ")
separate()

# EJERCICIO 3
separate()
print("EJERCICIO 3")
print(" ")



print(" ")
separate()

# EJERCICIO 4
separate()
print("EJERCICIO 4")
print(" ")



print(" ")
separate()

# EJERCICIO 5
separate()
print("EJERCICIO 5")
print(" ")



print(" ")
separate()

# EJERCICIO 6
separate()
print("EJERCICIO 6")
print(" ")



print(" ")
separate()

# EJERCICIO 7
separate()
print("EJERCICIO 7")
print(" ")



print(" ")
separate()

# EJERCICIO 8
separate()
print("EJERCICIO 8")
print(" ")



print(" ")
separate()