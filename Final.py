#Program for the final
import random
def main():
    yesno = 'y'
    x = 0
    y = 0
    key = 0
    loops = 0
    name = input ("Who's playing?: ")
    while (yesno == 'y'):
        try:
            n = random.randint(1, 200)
            loops = 0
            loops = input ('How many tries would you like?: ')
            loopslen = len(loops)
            if loopslen == 0:
                loops = 15
                key = 1
            elif loops.isspace():
                loops = 15
                key = 1
            else:
                loops = int(loops)
                key = 1
            if (loops < 1) or (loops > 100):
                print ('tries must be between 1 and 100')
            else:
                left = loops
        except TypeError:
            print ('Must be a number')
        except ValueError:
            print ('Must be a whole number')
        x = 0
        y = 0
        z = 0
        if key == 1:
            print ('\n'*15)
        while (z == 0) and (key == 1):
            try:
                guess = int(input("Enter an integer from 1 to 200: "))
                while (n != "guess"):
                    if (loops == 1) and (n == guess):
                        print ('\n'*4,'__You guessed it!__')
                        print ('in 1 guess(es)')
                        print (y,'errors')
                        yesno = input ('Would you like to play again: y/n: ')
                        key = 0
                        z = 1
                        break
                    elif left == 1:
                        print ('\n'*4,'you lose')
                        print ("you've expeneded all",loops,'guesses')
                        print (y,'errors')
                        yesno = input ('Would you like to play again: y/n: ')
                        x = 0
                        y = 0
                        z = 1
                        key = 0
                        break
                    else:
                        if (guess < 1) or (guess > 200):
                            print ('Guess must be between 1 and 200')
                            print (x,'guess(es)')
                            print (left,'guesses left')
                            guess = int(input("Enter an integer from 1 to 200: "))
                        else:    
                            if guess < n:
                                print ("guess is low")
                                x = x + 1
                                left = left - 1
                                print (x,'guess(es)')
                                print (left,'guesses left')
                                guess = int(input("Enter an integer from 1 to 200: "))
                            elif guess > n:
                                print ("guess is high")
                                x = x + 1
                                print (x,'guess(es)')
                                left = left - 1
                                print (left,'guesses left')
                                guess = int(input("Enter an integer from 1 to 200: "))
                            else:
                                print ('\n'*4,"__you guessed it!__")
                                x = x + 1
                                left = left - 1
                                print ('in',x,'guess(es)')
                                print (left,'guesses left')
                                print (y,'Errors')
                                yesno = input ('Would you like to play again: y/n: ')
                                z = 1
                                key = 0
                                break
            except ValueError:
                print ('Must input a whole number')
                print (x,'guess(es)')
                print (left,'guesses left')
                y = y + 1
main()


