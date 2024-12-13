#Program number 12
x=0
a=0
monthlist = ['January','February','March','April','May','June','July','Augest','September','October','November','December']
rainlist = []
while x < 12:
    print ('Input',monthlist[x]+"'s rainfall data",)
    Rainfall = float (input ('->'))
    rainlist.append (Rainfall)
    x=x+1
print (rainlist)
average = sum(rainlist) / 12
print ('highest: ',max(rainlist))
print ('lowest: ',min(rainlist))
print ('Total: ',sum(rainlist))
print ('Average: ',average)

    
