print ('--Program start')
print ('Table codes: A = add, S = subtract, M = multiple, D = divide')
TableCode = input ('Enter Table Code: ')
Number = float (input ('Enter number for table: '))
if TableCode == 'A':
    for _ in range (1,11):
       Equals = Number + _ 
       print (Number,'+',_,'=',Equals)
else:
     if TableCode == 'S':
         for _ in range (1,11):
              Equals = Number - _ 
              print (Number,'-',_,'=',Equals)
     else:
         if TableCode == 'M':
             for _ in range (1,11):
                  Equals = Number * _ 
                  print (Number,'*',_,'=',Equals)
         else:
             if TableCode == 'D':
                 for _ in range (1,11):
                      Equals = Number / _ 
                      print (Number,'/',_,'=',Equals)