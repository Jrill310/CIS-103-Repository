#Program number 13
def main():   
    YesNo = 'Y'
    YesNo2 = ''
    numeraldict = {1: 'I',
                   2: 'II',
                   3: 'III',
                   4: 'IV',
                   5: 'V',
                   6: 'VI',
                   7: 'VII',
                   8: 'VIII',
                   9: 'IX',
                   10: 'X',
                   11: 'XI',
                   12: 'XII',
                   13: 'XIII',
                   14: 'XIV',
                   15: 'XV',
                   16: 'XVI',
                   17: 'XVII',
                   18: 'XVIII',
                   19: 'XIX',
                   20: 'XX',
                   21: 'XXI',
                   22: 'XXII',
                   23: 'XXIII',
                   24: 'XXIV'}
                   
    while (YesNo == 'Y'):
        print (numeraldict)
        try:
            x = int(input('Input a number: '))
            if x > 0:
                if x in numeraldict:
                    y = numeraldict[x]
                    print ('the roman numeral for',x,'=',y)
                    YesNo = input('Run Again? Y/N: ')
                    YesNo = YesNo.capitalize()  
                else:
                    print ('This Key is not in the dictionary.\nWould you like to add it?')
                    YesNo2 = input ('Y/N: ')
                    if YesNo2 == 'Y':
                        NewNumber = x
                        NewNumeral = input ("Input your number's numeral: ")
                        if NewNumeral.isalpha:
                            numeraldict[NewNumber] = NewNumeral
                            print (numeraldict)
                            YesNo = input('Run Again? Y/N: ')
                            YesNo = YesNo.capitalize()  
                        else:
                            print ('Numeral must be alphabetic')
                            YesNo = input('Run Again? Y/N: ')
            else:
                break
        except ValueError:
            print ('Must be numeric')
            YesNo = input('Run Again? Y/N: ')
    print (numeraldict)
main()
