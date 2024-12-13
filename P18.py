#Program number 18
from tkinter import *
def a(TextBox,CBox,FBox,EBox):
    try:
        KelvinInput = TextBox.get()
        if KelvinInput.isspace():
            Error ='Cannot be blank'
            EBox.insert(0,Error)
        else:
            KelvinInput = float(KelvinInput)
            if KelvinInput == 0:
                Error = 'Cannot be 0'
                EBox.insert(0,Error)
            elif KelvinInput < 0:
                Error = 'Cannot be negative'
                EBox.insert(0,Error)
            else:
                Celcius = KelvinInput - 273.15
                Fahrenheit = (9/5)*(KelvinInput-273)+32
                print (Celcius,Fahrenheit)
                CBox.insert(0,Celcius)
                FBox.insert(0,Fahrenheit)
    except ValueError:
        Error = 'must be a number'
        EBox.insert(0,Error)
def b(TextBox,CBox,FBox,EBox):
    TextBox.delete(0,"end")
    CBox.delete(0,"end")
    FBox.delete(0,"end")
    EBox.delete(0,"end")
def main():
    print('--> start <--')
    mainwin = Tk()
    color='white'
    wcan = Canvas(mainwin,bg=color,
         width=600,height=700)
    wcan.pack()
    thetext = 'Temperature Conversion'
    wcan.create_text(150, 50, font="Times 20 italic bold",
            anchor='w',text=thetext)
    KelvinText= 'Kelvin:'
    wcan.create_text(30, 150, font="Times 20 italic bold",
            anchor='w',text=KelvinText)
    TextBox = Entry(mainwin, width = 20)
    TextBox.place ( x=230, y=140)
    CelsiusText= 'Celsius:'
    wcan.create_text(30, 250, font="Times 20 italic bold",
            anchor='w',text=CelsiusText)
    CBox = Entry(mainwin,width = 20)
    CBox.place ( x=230, y=240)
    FahrenheitText= 'Fahrenheit:'
    wcan.create_text(30, 350, font="Times 20 italic bold",
            anchor='w',text=FahrenheitText)
    FBox = Entry(mainwin,width = 20)
    FBox.place ( x=230, y=340)
    EBox = Entry(mainwin,font="Times 20 italic bold",width = 20)
    EBox.place ( x=30, y=500)
    RunButton = Button(text = 'Calc', command = lambda:a(TextBox,CBox,FBox,EBox))
    RunButton.place(x=30,y=450)
    ResetButton = Button(text = 'Reset', command = lambda:b(TextBox,CBox,FBox,EBox))
    ResetButton.place(x=130, y=450)
    mainwin.mainloop()
main()
