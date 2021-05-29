# İyi çalışmalar <3

from tkinter import *
import tkinter as tk

def result():
    if((int(entryText.get().isdigit()))and(int(entryText2.get().isdigit()))and(int(entryText3.get().isdigit()))):
        hesap = (int(entryText.get()) + int(entryText2.get()) + int(entryText3.get()))/3
        labelText.configure(text=f'Ortalama: {str(hesap)}', foreground='green')
    else:
        labelText.configure(text='Sayı giriniz!', foreground='red')
win = Tk()
win.geometry('320x240')
win.resizable(False, False)
win.title('Ortalama Hesaplama!')
win.configure(background='#303030')
win.wm_attributes('-alpha', 0.9)

labelText = Label(text='Ortalama Hesaplama!', font='Verdana 12 bold', foreground='orange', background='#303030')
labelText.place(x=65, y=40)
labelText2 = Label(text='1.Not:', font='Verdana 9 bold', foreground='#0062ca', background='#303030').place(x=65, y=70)
labelText2 = Label(text='2.Not:', font='Verdana 9 bold', foreground='#0062ca', background='#303030').place(x=65, y=100)
labelText2 = Label(text='Performans:', font='Verdana 9 bold', foreground='#0062ca', background='#303030').place(x=24, y=130)

entryText = Entry(font='Verdana 10 bold', foreground='#ffffff', background='#002e63', width=10)
entryText.place(x=110, y=70)
entryText2 = Entry(font='Verdana 10 bold', foreground='#ffffff', background='#002e63', width=10)
entryText2.place(x=110, y=100)
entryText3 = Entry(font='Verdana 10 bold', foreground='#ffffff', background='#002e63', width=10)
entryText3.place(x=110, y=130)

entryText.focus()

button = Button(text='Hesapla', font='Verdana 10 bold',width=10, foreground='black', background='#00bb18', command=result).place(x=105, y=160)

win.mainloop()
