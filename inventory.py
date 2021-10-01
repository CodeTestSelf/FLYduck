
from mongo import mongoadd
def addInventory(inventoryVariables,databaseName,collectionName):
    inventoryVariables = {"SerialNum"       : inventoryVariables["SerialNum"], 
                          "ProductName"     : inventoryVariables["ProductName"], 
                          "GrossWeight"     : inventoryVariables["GrossWeight"] , 
                          "NetWeight"       : inventoryVariables["NetWeight"], 
                          "Material"        : inventoryVariables["Material"], 
                          "Purity"          : inventoryVariables["Purity"],
                          "Description"     : inventoryVariables["Description"],
                          "PurchasedFrom"   : inventoryVariables["PurchasedFrom"],
                          "PurchaseBillNum" : inventoryVariables["PurchaseBillNum"] 
                      }
    mongoadd(inventoryVariables,databaseName,collectionName)                  
    print(inventoryVariables)


inventoryVariables = {"SerialNum"       : "12345", 
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

