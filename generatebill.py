from mongo import mongoadd

def itemPrice(sno,grossWeight, netWeight, making, rate):
    
    item_sNo=sno

    total = (netWeight*rate)+making
    print(total)
    return total
    



item1={"name" : "ring", "grossWeight" : 1.2, "netWeight" : 2, "making" :500, "rate":500 }
item2={"name" : "chain", "grossWeight" : 1.2, "netWeight" : 3, "making" :500, "rate":500 }

def generateBill(*item):
    totalItems=0
    grandTotal=0
    total = []
    for a in item:

        x=itemPrice(a["name"],a["grossWeight"], a["netWeight"],a["making"], a["rate"])
        mongoadd(a)
        total.append(x)
        totalItems+=1

        grandTotal=grandTotal + x


    print("Total number of items is "+ str(totalItems))
    print("Grand total is "+ str(grandTotal))
    print(total)    
    
generateBill(item1,item2)
