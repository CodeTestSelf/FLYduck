import pymongo

def mongoAdd(mydict,databaseName,collectionName):
    
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')

    mydb = myclient[databaseName]

    mycol = mydb[collectionName]

    # mydict = {"name": "krishna", "age" : "24"}

    mycol.insert_one(mydict)
    print(myclient.list_database_names())


def mongoUpdate():
    pass


def mongoRead():
    pass

def mongoUpdate():
    pass
    