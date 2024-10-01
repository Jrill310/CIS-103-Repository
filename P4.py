Name=input('Input your name: ')
AccountNum=input('Input your account number: ')
PaymentAmm=input('Input payment ammount')
NameLen=len(Name)
AccountNumLen=len(AccountNum)
PaymentAmmLen=len(PaymentAmm)
if (NameLen == 0):
    print ('Name cannot be blank')
else:
    if (Name.isspace()):
        print ('Name cannot be blank')
    else:
        if (NameLen < 3):
            print ('Name Too Short')
        else:
            if (not Name.isalpha()):
                print ('name must be alphabetic')
            else:
                print ('No name issues')
if (AccountNumLen == 0):
    print ('Account number cannot be blank')
else:
    if (AccountNum.isspace()):
        print ('Name cannot be blank')
    else:
        if (not AccountNum.isnumeric()):
            print ('Account number must be numeric')
        else:
            if (AccountNumLen != 9):
                print ('Account number must be 9 digits')
            else:
                print ('No account number issues')
if (PaymentAmmLen == 0):
    print ('Payment ammount cannot be blank')
else:
    if (PaymentAmm.isspace()):
        print ('Payment ammount cannot be blank')
    else:
        if (PaymentAmm.isnumeric()):
            PaymentAmm = int(PaymentAmm)
        else:
            if (PaymentAmm < 0):
                print ('Payment ammount cannot be negative')
            else:
                if (PaymentAmm == 0):
                    print ('Payment ammount cannot be zero')