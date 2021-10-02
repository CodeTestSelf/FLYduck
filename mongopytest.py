from mongo import mongoAdd
import pymongo


def mongoUpdate():
    pass


def searchOne(databaseName,collectionName,index,value):
    
    
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')

    mydb = myclient[databaseName]

    mycol = mydb[collectionName]

    # mydict = {"name": "krishna", "age" : "24"}

    for x in mycol.find():
        if (x[index]==value):
            print(x)
            break
    if (x[index]!=value):
        print("record not found")
        
    print(x)

def searchAll(databaseName,collectionName,index,value):
    
    
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')

    mydb = myclient[databaseName]

    mycol = mydb[collectionName]

    # mydict = {"name": "krishna", "age" : "24"}
    counter = 0
    for x in mycol.find():
        if (x[index]==value):
            counter+=1
            a={}
            a.update(x)
            
            print(a)
            
    if (counter==0):
        print("record not found")
            
    


mydict={"name":"kkk","age": "1"}
searchAll("test1","products","name","hi")


