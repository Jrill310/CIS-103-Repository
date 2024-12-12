import datetime
time = datetime.time()
def main():
    time = datetime.datetime.now()
    lettergrade=''
    pointsfile = 'c:/temp/points.txt'
    gradesfile = 'c:/temp/grades.txt'
    errorfile = 'c:/temp/error.txt'
    inpoints = open(pointsfile,'r')
    ingrades = open(gradesfile,'w')
    inerror = open(errorfile,'w')
    linepoints = inpoints.readline()
    acount = 0
    bcount = 0
    ccount = 0
    dcount = 0
    fcount = 0
    errorcount = 0
    while (linepoints !=''):
        linepoints = linepoints.strip()
        (a,b,c) = linepoints.split(',')
        try:
            c = int(c)
            if (c > 1000):
                errormessage = 'cannot be above 1000'
                c = str(c)
                fulleq = a +','+ b +','+ c +','+ errormessage +'\n'
                inerror.write(fulleq)
                errorcount = errorcount + 1
            elif (c < 0):
                errormessage = 'cannot be negative'
                c = str(c)
                fulleq = a +','+ b +','+ c +','+ errormessage +'\n'
                inerror.write(fulleq)
                errorcount = errorcount + 1
            elif (c >= 900) and (c <= 1000):
                lettergrade = 'A'
                c = str(c)
                fulleq = a +','+ b +','+ c +','+ lettergrade +'\n'
                acount = acount + 1
                ingrades.write(fulleq)
            elif (c >= 800) and (c <= 899):
                lettergrade = 'B'
                c = str(c)
                fulleq = a +','+ b +','+ c +','+ lettergrade +'\n'
                bcount = bcount + 1
                ingrades.write(fulleq)
            elif (c >= 700) and (c <= 799):
                 lettergrade = 'C'
                 c = str(c)
                 fulleq = a +','+ b +','+ c +','+ lettergrade +'\n'
                 ccount = ccount + 1
                 ingrades.write(fulleq)
            elif (c >= 600) and (c <= 699):
                lettergrade = 'D'
                c = str(c)
                fulleq = a +','+ b +','+ c +','+ lettergrade +'\n'
                ingrades.write(fulleq)
                dcount = dcount + 1
            elif (c >= 0) and (c <= 599):
                lettergrade = 'F'
                c = str(c)
                fulleq = a +','+ b +','+ c +','+ lettergrade +'\n'
                ingrades.write(fulleq)
                fcount = fcount + 1
        except ValueError: 
            errormessage = "must be numeric"
            fulleq = a +','+ b +','+ c +','+ errormessage +'\n'
            inerror.write(fulleq)
            errorcount = errorcount + 1
        linepoints = inpoints.readline() 
    def line():
        ingrades.write('\n')
    count = acount+bcount+ccount+dcount+fcount
    countextra = count + errorcount
    print (time)
    print ('Number of records read:',countextra)
    print ("Number of A's:",acount)
    print ("Number of B's:",bcount)
    print ("Number of C's:",ccount)
    print ("Number of D's:",dcount)
    print ("Number of F's:",fcount)
    print ('number of graded records:',count)
    print ('number of error records:',errorcount)
    print (time)
    inpoints.close()
    ingrades.close()
    inerror.close()
main()