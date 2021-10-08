from mongo import searchOne
import pymongo


def serialKey(productName):

    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient[databaseName]
    mycol = mydb[collectionName]
    
    counter=1
    for y in mycol.find():
        z=[*y.keys()]
        break
    
    print(len(z))

    
    mydoc = mycol.find().sort("_id")
    for x in mydoc:
        if x["_id"]==counter:
            counter+=1
        else:
            print(counter)
            return counter

    print(mydoc)

    #x= mycol.insert_many(mydoc1)
        




databaseName="SoumyaJewellers"
collectionName="Inventory"
mydict1=int(12345)



serialKey(1)