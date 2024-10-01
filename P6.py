z='y'
print ('Calorie Calculation')
print ('--------------------')
while z == 'y' or z =='Y':
    Minutes = float (input ('Enter running time in minutes: '))
    if Minutes <= 5:
        print ('Time must be greater than 5')
    else:
 
        x=5
        while x < Minutes + 1:
            CaloriesBurnt = x * 4.9
            print ('Minutes:',x,'burns',CaloriesBurnt,'calories')
            x=x+5
    print ('--------------------')
    z = input ('Again y/n?')
    print ('--------------------')
            
print ('***Done')
