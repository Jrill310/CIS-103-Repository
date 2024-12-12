from random import *
YesNo = 'y'
def Powerball(x):
    y = 0
    numblist = []
    while y < 5:
        numb = randint(1,x)
        if numb not in numblist:
            numblist.append (numb)
            y = y + 1
    numblist.sort()
    print ('Powerball',numblist)
def MegaMillion(x):
    y = 0
    numblist = []
    while y < 5:
        numb = randint(1,x)
        if numb not in numblist:
            numblist.append (numb)
            y = y + 1
    numblist.sort()
    print ('Mega Million',numblist)
def LuckyDayLotto(x):
    y = 0
    numblist = []
    while y < 5:
        numb = randint(1,x)
        if numb not in numblist:
            numblist.append (numb)
            y = y + 1
    numblist.sort()
    print ('Lucky Day Lotto',numblist)
def Lotto(x):
    y = 0
    numblist = []
    while y < 6:
        numb = randint(1,x)
        if numb not in numblist:
            numblist.append (numb)
            y = y + 1
    numblist.sort()
    print ('Lotto',numblist)
    return
while YesNo == 'y':
    x = 0
    z = 0
    try:
        choice = int(input ('1.   Powerball\n2.   Mega Millions\n3.   Mega Millions\n4.   Lotto\n\n9.   Quit\n\nInput Here: '))
        if choice == 1:
            x = 69
            Powerball(x)
            YesNo = input ('Would You Like To Run Again?: ')
        elif choice == 2:
            x = 70
            MegaMillion(x)
            YesNo = input ('Would You Like To Run Again?: ')
        elif choice == 3:
            x = 45
            LuckyDayLotto(x)
            YesNo = input ('Would You Like To Run Again?: ')
        elif choice == 4:
            x = 52
            Lotto(x)
            YesNo = input ('Would You Like To Run Again?: ')
        elif choice == 9:
            break
        elif (choice != 1) or (choice != 2) or (choice != 3) or (choice != 4) or (choice != 9):
            print ('Please Input A Valid Number')
            YesNo = input ('Would You Like To Run Again?: ')
    except ValueError:
        print ('Please Input A Number')
        YesNo = input ('Would You Like To Run Again?: ')
