from django.shortcuts import render
from django.http import HttpResponse
from backend.generatebill import *


def index(request):
    print(request.GET)
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
    url=r'file://C:\Users\krishnasai\Desktop\Django Projects\bill\desktop Stand Alone\invoices' +"\\"+invoicenumber+".pdf"

    print("check")
    print(invoicenumber)
    print(url)

    webbrowser.open_new(url)

    form={'form':"click for bill form "}
    return render(request,"index.html",form)

    

def addformfield(request):
    formcount=request.formcount
    while formcount<8:
        pass

    return render(request,"generatebill.html")


def addformfield(request):
    formcount=request.formcount
    while formcount<8:
     pass


    return render(request,"index.html")


# Create your views here.
