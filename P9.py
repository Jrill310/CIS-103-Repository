#Program number 9
YesNo = 'y'
def MiToKm():
    Kilometers = MilesInput * 1.609344
    print (MilesInput,"Miles equals",Kilometers,"Kilometers")
def LbToKilo ():
    Kilograms = PoundsInput * 0.45359237
    print (PoundsInput,'Pounds equals',Kilograms,'Kilograms')
def FToC():
    Celsius = (FahrenheitInput - 32) * (5 / 9)
    print (FahrenheitInput, "degrees equals",Celsius,"Celsius")
while YesNo == 'y' or YesNo == 'Y':
    try:
        MilesInput = float (input('Input Distance in Miles: '))
        MiToKm()
    except ValueError:
        print ('value error')
    except TypeError:
        print ('type error')
    except:
        print('unknown error')
    try:
        PoundsInput = float (input('Input Weight in Pounds: '))
        LbToKilo()
    except ValueError:
        print ('value error')
    except TypeError:
        print ('type error')
    except:
        print('unknown error')
    try:
        FahrenheitInput = float (input('Input Degrees in Fahrenheit: '))
        FToC()
    except ValueError:
        print ('value error')
    except TypeError:
        print ('type error')
    except:
        print('unknown error')
    YesNo = input ('Again? Y/N: ')
else:
    print ('Program Finished')
