DatabaseName = "hi"

showDarabases = "show dbs" #shows available databases

createNewDatabase = "use " + DatabaseName #Creates new Database

switchDatabase = "use "+ DatabaseName #Switches to database



print(createNewDatabase)


import pymongo

def mongoadd(mydict,databaseName,collectionName):
    
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')

    mydb = myclient[databaseName]

    mycol = mydb[collectionName]

    # mydict = {"name": "krishna", "age" : "24"}

    mycol.insert_one(mydict)
    print(myclient.list_database_names())
    