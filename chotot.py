from fastapi import FastAPI
import json
app = FastAPI()
def string_to_number(stringtime):
    parts = stringtime.strip().split()
    heso = 1
    if (parts[1] == 'phút'):
        heso = 60
    elif (parts[1] == 'giờ'):
        heso = 3600
    else:
        heso = 1
    return int(parts[0])*heso

@app.get("/category/")
def getProduct_category(id : int):
    productsReturn = []
    with open('data.json', 'r',encoding="utf-8") as json_file:
        dataload = json.load(json_file)
    for product in dataload:
        if (product["category"] == id):
            print(product)
            productsReturn.append(product)
    return productsReturn

@app.get("/time/")
def getProduct_time(number : int,unit : int = 1):
    productsReturn = []
    with open('data.json', 'r',encoding="utf-8") as json_file:
        dataload = json.load(json_file)
    for product in dataload:
        if (number*unit >= string_to_number(product["date"])):
            productsReturn.append(product)
    return productsReturn