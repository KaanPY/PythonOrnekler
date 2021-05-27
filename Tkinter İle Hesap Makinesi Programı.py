# İyi Çalışmalar <3

from tkinter import *
import tkinter as tk

def toplama():
    if((number.get().isdigit())and(number2.get().isdigit())):
        n1=float(number.get())
        n2=float(number2.get())
        result.configure(text=str(n1+n2))
        print(f'{n1} + {n2} = {n1+n2}')
    else:
        result.configure(text='Sayı giriniz!')
def cikarma():
    if((number.get().isdigit())and(number2.get().isdigit())):
        n1=float(number.get())
        n2=float(number2.get())
        result.configure(text=str(n1-n2))
        print(f'{n1} - {n2} = {n1-n2}')
    else:
        result.configure(text='Sayı giriniz!')
def carpma():
    if((number.get().isdigit())and(number2.get().isdigit())):
        n1=float(number.get())
        n2=float(number2.get())
        result.configure(text=str(n1*n2))
        print(f'{n1} x {n2} = {n1*n2}')
    else:
        result.configure(text='Sayı giriniz!')
def bolme():
    try:
        if((number.get().isdigit())and(number2.get().isdigit())):
            n1=float(number.get())
            n2=float(number2.get())
            result.configure(text=str(n1/n2))
            print(f'{n1} / {n2} = {n1/n2}')
        else:
            result.configure(text='Sayı giriniz!')
    except ZeroDivisionError:
        result.configure(text='sıfıra bölünemez!')

win = Tk()
win.geometry('320x300')
win.title('Hesap Makinesi')

number = Entry(foreground='#228b22', font="Courier 14 bold", width=15, justify="right")
number.place(x=70, y=50)
number2 = Entry(foreground='#228b22', font="Courier 14 bold", width=15, justify="right")
number2.place(x=70, y=80)

number.focus()

result = Label(text='Sonuç', foreground='#8b7500', font='Courier 16 bold', width=30, justify='center')
result.place(x=-50, y=20)

buttonTopla = Button(text='+', foreground='#1c6071', font='Courier 14 bold', width=10, command=toplama).place(x=90, y=110)
buttonCikarma = Button(text='-', foreground='#1c6071', font='Courier 14 bold', width=10, command=cikarma).place(x=90, y=150)
buttonCarpma = Button(text='x', foreground='#1c6071', font='Courier 14 bold', width=10, command=carpma).place(x=90, y=190)
buttonBolme = Button(text='/', foreground='#1c6071', font='Courier 14 bold', width=10, command=bolme).place(x=90, y=230)

win.mainloop()
