from reportlab.pdfgen import canvas  #pip install reportlab
from reportlab.lib.pagesizes import A4
import datetime





def generate_invoice(items,otherVariables,gst,invoiceNumber):

    billNo=str(invoiceNumber).zfill(3)
    x = datetime.datetime.now()
    date = str(x.day)+" - "+x.strftime("%b")+" - "+str(x.year)
    time = str(x.strftime("%I"))+" : "+str(x.strftime("%M"))+" : "+x.strftime("%p")
    InvoiceNumber = str(x.year)+str(x.month)+str(x.day)+str(billNo)
    paymentMode=otherVariables["PaymentMode"]

    customerName=otherVariables["CustomerName"]
    customerAddress=otherVariables["CustomerAddress"]
    customerContact=otherVariables["CustomerContact"]

    c = canvas.Canvas("invoices/"+InvoiceNumber+".pdf", pagesize=A4)
    c.drawImage("invoice.jpg", 0, 0,width=600,height=850)
    
    c.setLineWidth(0.3)
    c.setFont('Helvetica', 10)
    
    c.drawString(500,626,date)
    c.drawString(500,612,time)

    c.setFont('Helvetica', 12)
    c.drawString(110,626,InvoiceNumber) 
    c.drawString(110,603,customerName)
    c.drawString(110,590,customerAddress)
    c.drawString(110,575,customerContact)
    c.setFont('Helvetica', 10)

    c.drawString(500,597,paymentMode)
    
    GrandTotal=gst["GrandTotal"]
    gstMaterial=gst["GstAmount"]
    gstMaking=gst["GstMaking"]
    gstTotal=gst["GstTotal"]
    
    sno=1
    row=515
    for x in items:
        c.drawString(38,row, str(sno))
        sno+=1
        currentRow=row
        if len(str(x["ProductName"]))>17 :
             productName=x["ProductName"]
             stringEnd=17
             stringStart=0
             
             for y in range(0,(int(len(str(productName))/17))+1):
                 c.drawString(70,currentRow, str(productName[stringStart:stringEnd]))
                 currentRow-=10
                 stringStart=stringEnd
                 stringEnd+=17
             currentRow+=10
        else:     
            c.drawString(70,row, str(x["ProductName"]))
            
        c.drawString(185,row, str(x["GrossWeight"]))
        c.drawString(230,row, str(x["NetWeight"])) 
        c.drawString(267,row, str(x["Rate"]))
        c.setFont('Helvetica', 7)
        c.drawString(300,row+5, str(x["Purity"]))
        c.setFont('Helvetica', 10)
        c.drawString(300,row-5, str(x["Material"]))
        c.drawString(345,row, str(x["Wastage"]))
        c.drawString(385,row, str(x["Amount"]))
        c.drawString(445,row, str(x["Making"]))
        c.drawString(490,row, str(x["Total"]))
        row=currentRow
        row-=25   

    c.drawString(390,240, str(gstMaterial))    
    c.drawString(440,240, str(gstMaking))
    c.drawString(490,195, str(GrandTotal))
    c.drawString(490,240, str(gstTotal))

    c.save()

item1 = {                 "_id"             : "12345", 
                          "ProductName"     : "Muthyala Haram1234567124312", 
                          "GrossWeight"     : "12.45" , 
                          "NetWeight"       : "12.45", 
                          "Rate"            : "4561", 
                          "Purity"          : "916 KDM",
                          "Material"        : "Gold",
                          "Wastage"         : "10%",
                          "Amount"          : "100000",
                          "Making"          : "10000" ,
                          "Total"           : "110000"
                      }
    
items=[item1]

otherVariables={           "CustomerName"      :"Bitla Krishna Sai",
                           "CustomerAddress"   :"Gudibandal, Hanamkonda",
                           "CustomerContact"   :"8106040999 ",
                           "invoiceNumber"     :"12345",
                           "PaymentMode"       :"Cash"
}

