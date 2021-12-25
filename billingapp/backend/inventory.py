
from mongo import mongoAdd
def addInventory(inventoryVariables,databaseName,collectionName):
    inventoryVariables = {"_id"             : inventoryVariables["_id"], 
                          "ProductName"     : inventoryVariables["ProductName"], 
                          "GrossWeight"     : inventoryVariables["GrossWeight"] , 
                          "NetWeight"       : inventoryVariables["NetWeight"], 
                          "Material"        : inventoryVariables["Material"], 
                          "Purity"          : inventoryVariables["Purity"],
                          "Description"     : inventoryVariables["Description"],
                          "PurchasedFrom"   : inventoryVariables["PurchasedFrom"],
                          "PurchaseBillNum" : inventoryVariables["PurchaseBillNum"] 
                      }
    mongoAdd(inventoryVariables,databaseName,collectionName)                  
    print(inventoryVariables)




inventoryVariables = {    "_id"             : "12345", 
                          "ProductName"     : "ring", 
                          "GrossWeight"     : 1 , 
                          "NetWeight"       : "", 
                          "Material"        : "", 
                          "Purity"          : "",
                          "Description"     : "",
                          "PurchasedFrom"   : "",
                          "PurchaseBillNum" : "" 
                      }

databaseName="SoumyaJewellers"
collectionName="Inventory"                      
addInventory(inventoryVariables,databaseName,collectionName)

def serialNum():
    
    pass
