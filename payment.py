from tkinter import * 
from tkinter import messagebox
from web3 import Web3
from info import * 
from acc_transaction import * 
def payment():
    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter user id : ")
    L.grid(row = 6, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 6, column = 2)

    clas=Entry(window,width=8,font =('arial', 15, 'bold'))
    clas.grid(row=6,column=3)
    
    submitbtn=Button(window,text="Submit",command=account_1.get(),bg="DodgerBlue2",fg="white",font = ('arial', 15, 'bold'))
    submitbtn.grid(row=9,columnspan=3)
        