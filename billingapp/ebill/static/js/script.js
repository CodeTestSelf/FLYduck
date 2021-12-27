var x =0

function form(x){
    document.write('<link rel="stylesheet" type="css" href="css/style.css">')
    document.write('<form class ="test" action=""  method="GET"> ')  
    if (x<2)
    {
    document.write('<input name="bill"type="submit" value="GenerateBill"></input><br>')
    }
    document.write('<form action=""  method="POST"> ')
    document.write("Product Name"+x+"         <input name='Productname"+x+"' type='text' ><br> ");
    document.write("Description"+x+"         <input name='Description"+x+"' type='text' ><br> ");
    document.write("Gross_Weight"+x+"         <input name='Gross_Weight"+x+"' type='text' ><br> ");
    document.write("Net_Weight"+x+"         <input name='Net_Weight"+x+"' type='text' ><br> ");
    document.write("Material"+x+"         <input name='Material"+x+"' type='text' ><br> ");
    document.write("Wastage"+x+"         <input name='Wastage"+x+"' type='text' ><br> ");
    document.write("Making"+x+"         <input name='Making"+x+"' type='text' ><br> <br> <br> ");
}

function addItem()
{   if (x<1){
    
    document.write("<input button value='add Item' onclick='addItem()' id = 'add' ></button>")
}
    while (x<8){
    x=x+1;
    form(x)
    console.log(x)
    
    return x
    }
    
}

console.log(x)