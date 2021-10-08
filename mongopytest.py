from mongo import mongoAdd
import pymongo


def mongoUpdate():
    pass


mydict={"name":"hi","age": "0"}

def mongoRead(mydict,databaseName,collectionName):    
    
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient[databaseName]
    mycol = mydb[collectionName]

    x = mycol.find_one(mydict)
    print(x)            

