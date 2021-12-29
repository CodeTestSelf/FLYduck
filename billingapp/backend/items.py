def send(inp):
    itemsarray=[]
    
    a=len(inp)-6
    a=int(a/9)
    
    counter=0
    
    for k in range(0,a):
        
        exec(f'item{k+1} = {{}}',None, globals())  
        exec(f"itemsarray.append(item{k+1})")
        
    
    for y in range(0,2):
        print(y)
        for x in inp:
            if counter<7+(y*9):
                print(counter,"  ",y," ",a)
                counter=counter+1
            else:
                exec(f'item{y+1}["{x}"]={inp}["{x}"][0]',None,globals())
                exec(f'print(item{y+1})')
                counter=counter+1
                if counter>(7+(y+1)*8):
                    print(counter)
                    counter=0
                    break           
        
        
    
    
    print("items are", itemsarray)
    
    
    return itemsarray






