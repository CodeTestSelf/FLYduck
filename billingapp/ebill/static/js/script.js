var x =0

function form(x){
    document.write('<form class ="test" action=""  method="GET"> ')  
    if (x<2)
    {
    document.write('<input name="bill"type="submit" value="GenerateBill"></input><br><br>')
    document.write(("CustomerName         <input name='CustomerName' type='text' ><br> "))
    document.write(("CustomerAddress         <input name='CustomerAddress' type='text' ><br> "))
    document.write(("CustomerContact         <input name='CustomerContact' type='text' ><br> "))
    document.write("Email_id         <input name='Email_id' type='text' ><br> ")
    document.write(("PaymentMode         <select name='PaymentMode' type='text' > <option value='Cash'>Cash<option><option value='card'>Card</option></select><br><br> "))
    
    }
    document.write('<form action=""  method="POST"> ')
    document.write("<input name='number' value="+x+"><br>")
    document.write("Product Name"+x+"         <input name='ProductName"+"' type='text' ><br> ");
    document.write("Description"+x+"         <input name='Description"+"' type='text' ><br> ");
    document.write("Gross_Weight"+x+"         <input name='GrossWeight"+"' type='text' ><br> ");
    document.write("Net_Weight"+x+"         <input name='NetWeight"+"' type='text' ><br> ");
    document.write("Rate         <input name='Rate' type='text' ><br> ")
    document.write("Purity         <input name='Purity' type='text' ><br> ")
    document.write("Material"+x+"         <input name='Material"+"' type='text' ><br> ");
    document.write("Wastage"+x+"         <input name='Wastage"+"' type='text' ><br> ");
    document.write("Making"+x+"         <input name='Making"+"' type='text' ><br> <br> <br> ");
    
}

function addItem()
{   if (x<1){
    
    document.write("<input button value='add Itema' onclick='addItem()' id = 'add' >add</button><br>")
}
    while (x<8){
    x=x+1;
    form(x)
    console.log(x)
    
    return x
    }
    
}

