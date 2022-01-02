from django.shortcuts import render
from django.http import HttpResponse
from backend.generatebill import *
import os
from backend.items import send




def index(request):
    otherVariables={}
    myDict = dict(request.GET)
    
    if myDict=={}:
        pass
    else:  
        print(myDict)     
        for x in myDict:  # Adds Data to customerdata variables
            otherVariables[x]=myDict[x][0]
            if x =="PaymentMode":
                break
    
          #Creates variables based on number of items and adds them to items array 
        
        items=send(myDict) 


        print()
  
    
    
    if myDict=={}:
        pass
    else:
        
        
        print(items)
        invoicenumber=generateBill(items,otherVariables)
        directory = os.getcwd() 
        url=directory+ r"\backend\invoices" +"\\"+invoicenumber+".pdf"
        directory = os.getcwd() 

        print(directory)
        print(otherVariables)
        
        webbrowser.open_new(url)
        
    form={'form':"click for bill form "}
    return render(request,"index.html",form)

    

def generatebill(request):
    otherVariables={           "CustomerName"      :"Bitla Krishna Sai",
                           "CustomerAddress"   :"Gudibandal, Hanamkonda",
                           "CustomerContact"   :"8106040999 ",
                           "Email_id"          :"",
                           "invoiceNumber"     :"12345",
                           "PaymentMode"       :"Cash"
                    }

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
    invoicenumber=generateBill(items,otherVariables)
    directory = os.getcwd() 
    url=directory+ r"\backend\invoices" +"\\"+invoicenumber+".pdf"
    

    directory = os.getcwd() 

    print(directory)

    print("check")
    print(invoicenumber)
    print(url)

    webbrowser.open_new(url)
    return(request,"index.html")


# Create your views here.
