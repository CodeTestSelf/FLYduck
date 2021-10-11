import datetime

x = datetime.datetime.now()
y=str(x.day)+" - "+x.strftime("%b")+" - "+str(x.year)

print(y)