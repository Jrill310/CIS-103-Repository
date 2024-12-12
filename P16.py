def Recur(origin,a):
        if origin > 0:
            a = a + origin
            origin = origin - 1
            Recur(origin,a)
        elif origin < 0:
            print ('Number Cannot Be negative')
        else:
            print(a)
        return ()
a = 0
Yesno = 'y'
while Yesno == 'y':
    try:
        origin = input ('enter a whole positive number: ')
        if (origin.isspace()):
            print ('cannot be blank')
            Yesno = input ('run again y/n: ')
        elif (origin.isalpha()):
            print ('Must Be a Number')
            Yesno = input ('run again y/n: ')
        else:
            origin = int(origin)
            Recur (origin,a)
            Yesno = input ('run again y/n: ')
    except ValueError:
        print ('Number Must Be an Integer')
        Yesno = input ('run again y/n: ')
        