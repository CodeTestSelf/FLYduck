for x in ar:
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