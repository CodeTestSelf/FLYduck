import pymongo
from mongo import mongoAdd,mongoUpdate
from invoice import generate_invoice
import datetime

def invoiceNumber(): #generates invoice number
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient["SoumyaJewellers"]
    mycol = mydb["invoiceNumber"]
  
    x = datetime.datetime.now()
    date = str(x.day)+x.strftime("%m")+str(x.year)
    
    for x in mycol.find():
        if x["_id"]==2:
            if x["Date"]!=date:    
                mongoUpdate("SoumyaJewellers","invoiceNumber",[2,{"Date":date}])
                mongoUpdate("SoumyaJewellers","invoiceNumber",[1,{"InvoiceNumber":1}])

    for x in mycol.find():
        invoiceNumber=x["InvoiceNumber"]        
        mongoUpdate("SoumyaJewellers","invoiceNumber",[1,{"InvoiceNumber":invoiceNumber+1}]) 
        return invoiceNumber
    



def itemPrice(sno,grossWeight, netWeight, making, rate,wastage):
    
    item_sNo=sno
    wastage=int(wastage[0:len(wastage)-1])

    total = netWeight*rate
    total=int(total+(total*wastage/100))
   
    return total
    

item1 = {                 "_id"             : "123", 
                          "ProductName"     : "Muthyala Haram1234567124312", 
                          "GrossWeight"     : "12.45" , 
                          "NetWeight"       : "12.45", 
                          "Rate"            : "4561", 
                          "Purity"          : "916 KDM",
                          "Material"        : "Gold",
                          "Wastage"         : "10%",
                          "Amount"          : "",
                          "Making"          : "1001" ,
                          "Total"           : ""
                      }
item2 = {                 "_id"             : "123", 
                          "ProductName"     : "Muthyala Haram", 
                          "GrossWeight"     : "20.45" , 
                          "NetWeight"       : "20.45", 
                          "Rate"            : "4562", 
                          "Purity"          : "916 KDM",
                          "Material"        : "Gold",
                          "Wastage"         : "10%",
                          "Amount"          : "",
                          "Making"          : "1000" ,
                          "Total"           : ""
                      }
    
items=[item1,item2]

otherVariables={           "CustomerName"      :"Bitla Krishna Sai",
                           "CustomerAddress"   :"Gudibandal, Hanamkonda",
                           "CustomerContact"   :"8106040999 ",
                           "Email_id"          :"",
                           "invoiceNumber"     :"12345",
                           "PaymentMode"       :"Cash"
}



def generateBill(items,otherVariables):
    totalItems=0
    grandTotal=0
   
    counter=1
    sale={}
    amount=0
    making=0
    gstAmount=0
    gstMaking=0
    gst={}
    for a in items:

        x=itemPrice(a["ProductName"],float(a["GrossWeight"]), float(a["NetWeight"]),int(a["Making"]), int(a["Rate"]),a["Wastage"])
        a["Amount"]=round(x,2)
        a["Total"]=int(x + float(a["Making"]))
        
        

        sale["InvoiceNumber"]             =otherVariables["invoiceNumber"]
        sale["ProductName"+str(counter)]  =a["ProductName"]
        sale["GrossWeight"+str(counter)]  =a["GrossWeight"] 
        sale["NetWeight"+str(counter)]    =a["NetWeight"]
        sale["Making"+str(counter)]       =a["Making"] 
        sale["Rate"+str(counter)]         =a["Rate"]
        sale["Purity"+str(counter)]       =a["Purity"]
        sale["Material"+str(counter)]     =a["Material"]
        sale["wastage"+str(counter)]      =a["Wastage"]
        sale["Amount"+str(counter)]       =a["Amount"]
        sale["Making"+str(counter)]       =a["Making"]
        sale["Total"+str(counter)]        =a["Total"]

        
        
        grandTotal=grandTotal + x+int(sale["Making"+str(counter)])
        

        amount=amount+int(sale["Amount"+str(counter)])
        making=making+int(sale["Making"+str(counter)])

        counter+=1
        totalItems+=1

        
    gstAmount=round((amount*0.03),2)
    gstMaking=round(making*0.05,2)
    
    gstTotal=round(gstAmount+gstMaking,2)
    grandTotal=round(grandTotal+gstAmount+gstMaking,2)

    sale["GstAmount"]=gstAmount
    sale["GstMaking"]=gstMaking
    sale["GstTotal"] =gstTotal
    sale["GrandTotal"]=grandTotal

    gst["GstAmount"]=gstAmount
    gst["GstMaking"]=gstMaking
    gst["GstTotal"] =gstTotal
    gst["GrandTotal"]=grandTotal


    customer={}
    customer["Name"]=otherVariables["CustomerName"]
    customer["Address"]=otherVariables["CustomerAddress"]
    customer["PhoneNumber"]=otherVariables["CustomerContact"]
    customer["Email_id"]=otherVariables["Email_id"]
    mongoAdd(customer,"SoumyaJewellers","CustomerDetails")               
                    
    invoicenumber=invoiceNumber()                
    generate_invoice(items,otherVariables,gst,invoicenumber)
    mongoAdd(sale,"SoumyaJewellers","Sales")
    
    print("Total number of items is "+ str(totalItems))
    print("Grand total is "+ str(grandTotal))
       
    
generateBill(items,otherVariables)
