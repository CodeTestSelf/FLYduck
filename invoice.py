from reportlab.pdfgen import canvas  #pip install reportlab
from reportlab.lib.pagesizes import A4
import datetime




def generate_invoice():

    billNo="001"
    x = datetime.datetime.now()
    date = str(x.day)+" - "+x.strftime("%b")+" - "+str(x.year)
    time = str(x.strftime("%I"))+" : "+str(x.strftime("%M"))+" : "+x.strftime("%p")
    InvoiceNumber = str(x.year)+str(x.month)+str(x.day)+str(billNo)


    c = canvas.Canvas("sample.pdf", pagesize=A4)
    c.drawImage("invoice.jpg", 0, 0,width=600,height=850)
    
    c.setLineWidth(0.2)
    c.setFont('Helvetica', 10)
    c.drawString(185,500,"1.2")

    c.drawString(500,626,date)
    c.drawString(500,612,time)
    c.drawString(110,626,InvoiceNumber)

    counter=500
    
    item1={}
    items=[1.2,1.3,4.5,5.06,6,3,5,1]
    for x in items:
         if len(str(x))>8:
             counter2=7
             counter3=0
             for y in range(0,int(len(str(x))/7)):
                 c.drawString(185, counter, str(x[counter3:counter2]))
                 counter-=10
                 counter3+=(counter2+1)
                 counter2+=7
        
         else:
             c.drawString(185, counter, str(x))
         counter-=25
        
    

    # c.setLineWidth(.3)
    # c.setFont('Helvetica', 12)

    # c.line(20, 820, 580, 820)
    # c.line(30, 805, 570, 805)#top

    # c.line(30, 805, 30, 40)#left
    # c.line(20, 820, 20, 25)

    # c.line(30, 40, 570, 40)#bottom
    # c.line(20, 25, 580, 25)

    # c.line(570, 805, 570, 40)#right
    # c.line(580, 820, 580, 25)

    # c.line(120, 700, 580, 700)
    # c.drawString(120, 703, "JOHN DOE")




    c.save()

generate_invoice()