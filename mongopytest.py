from mongo import mongoAdd
import pymongo


def mongoUpdate():
    pass



mydict={"name":"hi","age": "0"}


def mongoRead(mydict,databaseName,collectionName):
    
    
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')

    mydb = myclient[databaseName]

    mycol = mydb[collectionName]

    x=mycol.find_one(mydict)
    print(x)
    


            

def filter(databaseName,collectionName,ar):
    
    
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')

    mydb = myclient[databaseName]

    mycol = mydb[collectionName]

    # mydict = {"name": "krishna", "age" : "24"}
    counter = 0
    index=0
    a=[]
    key=[]
    value=[]
    
    for x in range(0,len(ar)):     #converting keys and values into seperate lists from input list of dictionaries
        
        valueAsList=[*ar[x].values()]
        value.append(valueAsList[0])

        keyAsList=[*ar[x].keys()]
        key.append(keyAsList[0])
        
        
    print(value)
    print(key)
    for x in mycol.find():        
            if x[key[counter]]==value[counter] and x[key[1]]==value[1]:
                counter+=1
                  
                a.append(x)
                
                
                      
    print(a)     
            
    if (counter==0):
        print("record not found")

mydict1={"age":"1"}
mydict2={"name":"krishna"}
ar=[mydict2,mydict1]
filter("test1","products",ar)




