import pymongo

def mongoAdd(mydict,databaseName,collectionName):
    
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient[databaseName]
    mycol = mydb[collectionName]
    
    mycol.insert_one(mydict)
    


def mongoUpdate(databaseName,collectionName,update):#update is a list with first value serian num , second dictionary of new values doesnt return anything

    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient[databaseName]
    mycol = mydb[collectionName]
    
    update[0]={"_id":int(update[0])}
    print(update[0])
    myquery = update[0]
    newvalues = { "$set": update[1] }
    mycol.update_one(update[0],newvalues)    


def mongoRead(databaseName,collectionName):

    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient[databaseName]
    mycol = mydb[collectionName]
    #print(myclient.list_database_names()) 
    for x in mycol.find():
        print(x) 


def filteredSearch(databaseName,collectionName,filter): #filter is input list of key value pairs of filters required

    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient[databaseName]
    mycol = mydb[collectionName]
    
    counter = 0
    index=0
    searchResult=[]
    key=[]
    value=[]

    def innerloop(key,value,counter,x):   #returns boolean value whether the filter matched or no 
        flag = False
        if counter==len(filter):
            flag=True
            return True #ends here if all filters match
      
        if counter<len(filter):

            if x[key[counter]]==value[counter]:
                print(x[key[counter]],end="")
                print("===="+value[counter])
                counter+=1
                flag=innerloop(key,value,counter,x)
                return flag
     
            else:   
                return False
    
    for x in range(0,len(filter)):     #converting keys and values into seperate lists from input list of dictionaries
        
        valueAsList=[*filter[x].values()]
        value.append(valueAsList[0])

        keyAsList=[*filter[x].keys()]
        key.append(keyAsList[0])  
    
    for x in mycol.find():  
        filterMatched=innerloop(key,value,counter,x)
        
        print(filterMatched)
        print(x)
        print("")

        if filterMatched==True:
            searchResult.append(x)       
    print(searchResult)                      
    if (counter==0):
        print("record not found")



def searchOne(databaseName,collectionName,index,value):  #Search the collection when serial num or id is given as parameter
    
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient[databaseName]
    mycol = mydb[collectionName]

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


def mongoDelete(databaseName,collectionName,delete):

    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient[databaseName]
    mycol = mydb[collectionName]
    
    for x in mycol.find():
        
        if x["_id"]==delete:
            
            mycol.delete_one(x)


#searchAll("test1","products","name","krishna")

#mydict1={"age":"1"}
#mydict2={"name":"krishna"}
#mydict3={"place":"hnk"}
#filter=[mydict2,mydict1,mydict3]
#filteredSearch("test1","products",filter)  

#searchOne("test1","products","name","krishna")