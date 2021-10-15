import pymongo

def mongoUpdate(databaseName,collectionName,update):#update is a list with first value serian num , second dictionary of new values doesnt return anything

    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient[databaseName]
    mycol = mydb[collectionName]
    
    update[0]={"_id":int(update[0])}
    print(update[0])
    myquery = update[0]
    newvalues = { "$set": update[1] }
    mycol.update_one(update[0],newvalues)    


mongoUpdate("SoumyaJewellers","invoiceNumber",["1",{"InvoiceNumber":2}])