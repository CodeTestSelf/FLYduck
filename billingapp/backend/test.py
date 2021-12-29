def items(items_number,myDict):
    itemsarray=[]
    
    a=len(myDict)-6
    a=int(a/9)
    
    counter=0
    
    for k in range(0,a):
        
        exec(f'item{k+1} = {{}}',None, globals())  #{"{k}":myDict["{k}"]}
        exec(f"itemsarray.append(item{k+1})")
        
    
    for y in range(0,2):
        print(y)
        for x in myDict:
            if counter<6+(y*9):
                
                counter=counter+1
            else:
                exec(f'item{y+1}["{x}"]=myDict["{x}"][0]',None,globals())
               
                counter=counter+1
                if counter>(6+(y+1)*8):
                    print(counter)
                    counter=0
                    break           
        
        
    
    
    print("items are", itemsarray)
    
    
    return itemsarray

myDict={'bill': ['GenerateBill'], 'CustomerAddress': [''], 'CustomerContact': [''], 'Email_id': [''], 'PaymentMode': ['Cash'], 'number': ['1'], 'ProductName1': ['1'], 'Description1': ['1'], 'GrossWeight1': ['1'], 'NetWeight1': ['1'], 'Rate': ['1'], 'Purity': ['1'], 'Material1': ['1'], 'Wastage1': ['1'], 'Making1': ['1'],'ProductName2': ['2'], 'Description2': ['2'], 'GrossWeight2': ['2'], 'NetWeight2': ['2'], 'Rate2': ['2'], 'Purity2': ['2'], 'Material2': ['2'], 'Wastage2': ['2'], 'Making2': ['2']}
items_number=1





items(items_number,myDict)
