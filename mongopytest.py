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

def filteredSearch(databaseName,collectionName,ar):#ar is input list of key value pairs of filters required
    
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient[databaseName]
    mycol = mydb[collectionName]
    
    counter = 0
    index=0
    searchResult=[]
    key=[]
    value=[]

    def innerloop(key,value,counter,x):    
        flag = False
        if counter==len(ar):
            flag=True
            return True #ends here if all filters match
      
        if counter<len(ar):

         if x[key[counter]]==value[counter]:
            print(x[key[counter]],end="")
            print("===="+value[counter])
            counter+=1
            flag=innerloop(key,value,counter,x)
            return flag
     
         else:
            flag = False
            return flag
    
    for x in range(0,len(ar)):     #converting keys and values into seperate lists from input list of dictionaries
        
        valueAsList=[*ar[x].values()]
        value.append(valueAsList[0])

        keyAsList=[*ar[x].keys()]
        key.append(keyAsList[0])  
    
    for x in mycol.find():  
        y=innerloop(key,value,counter,x)
        
        print(y)
        print(x)
        print("")

        if y==True:
            counter+=1
            searchResult.append(x)       
    print(searchResult)                      
    if (counter==0):
        print("record not found")

mydict1={"age":"1"}
mydict2={"name":"krishna"}
mydict3={"place":"hnk"}
ar=[mydict2,mydict1,mydict3]
#filteredSearch("test1","products",ar)
#mongoRead(mydict,"test1","products")