def MiToKm():
    Kilometers = MilesInput * 1.609344
    print (MilesInput,"Miles equals",Kilometers,"Kilometers")
def LbToKilo ():
    Kilograms = PoundsInput * 0.45359237
    print (PoundsInput,'Pounds equals',Kilograms,'Kilograms')
def FToC():
    Celsius = (FahrenheitInput - 32) * (5 / 9)
    print (FahrenheitInput, "degrees equals",Celsius,"Celsius")
MilesInput = float (input('Input Distance in Miles: '))
MiToKm()
PoundsInput = float (input('Input Weight in Pounds: '))
LbToKilo()
FahrenheitInput = float (input('Imput Degrees in Fahrenheit: '))
FToC()
