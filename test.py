from mongo import mongoAdd
import pymongo


def innerloop(key,value,counter,x):
    
    flag = False
    if counter==len(ar):
        flag=True
        return True
      
        
    
    
    if counter<len(ar):
      
      if x[key[counter]]==value[counter]:
        
        print(x[key[counter]],end="")
        print("===="+value[counter])
        counter+=1
        
        flag=innerloop(key,value,counter,x)
        print("flag=="+str(flag))
        
        return flag
     
      else:
        print("false")
        
        flag = False
        return flag
        
          
    else:
        print("end")
        print(flag)
        
        

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
        
        
    
    for x in mycol.find():  
        y=innerloop(key,value,counter,x)
        
        print(y)
        print(x)
        print("")
        

        a.append(x)    
               
                  
                
                
            
    if (counter==0):
        pass#print("record not found")

mydict1={"age":"1"}
mydict2={"name":"krishna"}
ar=[mydict2,mydict1]
filter("test1","products",ar)


