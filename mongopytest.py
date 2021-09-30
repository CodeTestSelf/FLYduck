import pymongo

def mongoadd(mydict):
    
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')

    mydb = myclient['test1']

    mycol = mydb["products"]

    # mydict = {"name": "krishna", "age" : "24"}

    mycol.insert_one(mydict)
    print(myclient.list_database_names())