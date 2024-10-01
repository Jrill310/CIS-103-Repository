# property tax program calculator 2
def getinput(msg):
    xin = float(input(msg))
    return xin

def main():
    print('\n')
    AssesmentLevel = .10
    HomeOwnerEx = 500.43
    SeniorCEX = 357.45
    PropertyValue = float (input('Enter value of property: '))
    LocalTaxRate = float (input('Enter local tax rate: '))
    StateEqualizer = float (input('Enter state equalizer rate: '))
    print('\n')
    AssessedValue= PropertyValue * AssesmentLevel
    EqualizeValue = AssessedValue * StateEqualizer
    PropertyTaxBefore = EqualizeValue * LocalTaxRate
    TotalPropertyTax = PropertyTaxBefore - HomeOwnerEx - SeniorCEX
    print('\n')
    print('Property tax due: ',TotalPropertyTax)
    print('\n')
    return
main()
