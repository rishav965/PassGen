from random import *
from tkinter import *
from tkinter.font import ITALIC
num="0123456789"
alphanumeric="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQSTUVWXYZ"
splalphanumeric="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQSTUVWXYZ'#@+()"

# passlen = int (input(" Enter password length \n"))
# randpass = []

# print ("Select the type of passwords \n1. Numbers\n2. AlphaNum\n3. special alpha numeric\n")

# Selecttype = int(input())
# if Selecttype == 1:
#     for i in range (passlen):
#         randpass.append (choice(num))

# elif (Selecttype == 2):
#     for i in range (passlen):
#         randpass.append (choice(alphanumeric))

# else:
     
#     for i in range (passlen):
#         randpass.append (choice(splalphanumeric))

# result = " ".join(randpass)

# print(" Your Random password is : " +result)


# def Create_pass():
#     Thechoice = Tchoice.get()

#     if Thechoice =="":
#         resultBox.delete(0.0, END)
#         resultBox.insert(END, "\n Select the password you like")

#         length = int (pass_length.get())
#         randpass = []
#         for i in range (length):
#             randpass.append(choice(Thechoice))

# result="".join(randpass)

# TheResult = "\n *** your password is : "+result+" ***\n"


#  resultBox.delete(0.0, END)
# resultBox.insert(END, TheResult)


window = Tk() 
window.geometry("800x500")
window.title("SpoolPassGen (copyright-rishav)")

ProgName = Label (window,font=('kristen ITC', 15, 'bold'), text="Password Generator \n (create random password)", fg="blue")
ProgName.grid(row=1,column=3, padx=250, pady=30)

ChooseType = Label  (window,font=('kristen ITC', 15, 'bold'), text="Choose any among 3", fg="red")
ChooseType.place(relx=.03, rely=.25)

Tchoice = StringVar()

Numchoice = Radiobutton (window, font= ('corbel', 10, 'italic'), text="Numeric", variable= Tchoice,value=num)
Numchoice.place(relx=.03, rely= .35)

AlphaNumchoice = Radiobutton (window, font= ('corbel', 10, 'italic'), text="Alpha Numeric", variable= Tchoice,value=alphanumeric)
AlphaNumchoice.place(relx=.03, rely= .4)

Specialchoice = Radiobutton (window, font= ('corbel', 10, 'italic'), text="Special", variable= Tchoice,value=splalphanumeric)
Specialchoice.place(relx=.03, rely= .45)

size = Label  (window, font=('Copperplate Gothic', 12, 'bold'), text="Passlength Size:")
size.place(relx=.69, rely= .32)

pass_length = Spinbox (window,from_=8, to=100)
pass_length.place(relx=.73, rely=.4)

Genbutton = Button (window, text= "Generate")
Genbutton.place(relx=.45, rely=.60)

resultBox = Text (window, height = 5, width = 70)
resultBox.place(relx=.06, rely=.7)




window.mainloop()
