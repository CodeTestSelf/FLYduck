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


def mongoRead(mydict,databaseName,collectionName):
    
    
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')

    mydb = myclient[databaseName]

    mycol = mydb[collectionName]

    x=mycol.find_one(mydict)
    #print(myclient.list_database_names()) 
    print(x)

    

def mongoUpdate():
    pass
    

def searchOne(databaseName,collectionName,index,value):  #Search the collection when serial num or id is given as parameter
    
    
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
        
    


def searchAll(databaseName,collectionName,index,value):#Search all the dictionaries in collection when one parameter is given
    
    
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')

    mydb = myclient[databaseName]

    mycol = mydb[collectionName]

    a=[]
    counter = 0
    for x in mycol.find():
        if (x[index]==value):
            counter+=1
            a.append(x)
    print(a)        
            
    if (counter==0):
        print("record not found")


#searchAll("test1","products","name","krishna")