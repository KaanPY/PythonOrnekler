# İyi Çalışmalar <3

from tkinter import * 
import tkinter as tk

def verified():

    win2 = Tk()
    win2.geometry('500x280')
    win2.configure(background='#303030')
    win2.wm_attributes('-alpha', 0.9)
    win2.title('Sipariş Onaylandı!')

    labelWin2 = Label(win2, text='Sipariş Onaylandı!', font='Verdana 15 bold', background='#303030', foreground='green').place(x=60,y=30)

    labelWin2Text = Label(win2, text='Ad & Soyad:', font='Verdana 10 bold', background='#303030', foreground='#ffffff').place(x=40,y=75)
    entryWin2Text = Label(win2,text=f'{entryText.get()}', font='Verdana 10 bold', background='#303030', foreground='green').place(x=130,y=75)

    labelWin2Text3 = Label(win2, text='Boyut:', font='Verdana 10 bold', background='#303030', foreground='#ffffff').place(x=40,y=110)
    labelWin2Text3 = Label(win2, text=f'{radio.get()}', font='Verdana 10 bold', background='#303030', foreground='green').place(x=90,y=110)

    labelWin2Text4 = Label(win2, text='Ekstra:', font='Verdana 10 bold', background='#303030', foreground='#ffffff').place(x=40,y=140)
    checkWin2Button = Label(win2, text=f'{check.get()} - {check2.get()} - {check3.get()}', font='Verdana 10 bold', background='#303030', foreground='green').place(x=95,y=140)

    labelWin2Text5 = Label(win2, text='Adres:', font='Verdana 10 bold', background='#303030', foreground='#ffffff').place(x=40,y=170)
    entryWin2Text2 = Label(win2,text=f'{entryText2.get()}', font='Verdana 10 bold', background='#303030', foreground='green').place(x=90,y=170)

    win2.mainloop()

win = Tk()
win.geometry('320x280')
win.resizable(False, False)
win.wm_attributes('-alpha', 0.9)
win.configure(background='#303030')
win.title('Sipariş Sistemi')

labelText = Label(win, text='Sipariş Sistemi!', font='Verdana 15 bold', background='#303030', foreground='orange').place(x=70,y=30)

labelText2 = Label(win, text='Ad & Soyad:', font='Verdana 10 bold', background='#303030', foreground='#ffffff').place(x=40,y=75)
entryText = Entry(win, font='Verdana 10 bold', background='#ffffff', foreground='#303030', width=15)
entryText.place(x=135,y=75)

radio=StringVar()
radio.set('Orta')
labelText3 = Label(win, text='Boyut:', font='Verdana 10 bold', background='#303030', foreground='#ffffff').place(x=40,y=110)
radioButton = Radiobutton(win, text='Küçük', font='Verdana 10 bold', background='#303030', foreground='#2f6cad', activebackground='#303030', value='Küçük', variable=radio)
radioButton.place(x=90,y=110)
radioButton2 = Radiobutton(win, text='Orta', font='Verdana 10 bold', background='#303030', foreground='#2f6cad', activebackground='#303030', value='Orta', variable=radio)
radioButton2.place(x=160,y=110)
radioButton3 = Radiobutton(win, text='Büyük', font='Verdana 10 bold', background='#303030', foreground='#2f6cad', activebackground='#303030', value='Büyük', variable=radio)
radioButton3.place(x=220,y=110)

check=StringVar()
check.set('Sucuk')
check2=StringVar()
check2.set('Kaşar')
check3=StringVar()
check3.set('Mısır')
labelText4 = Label(win, text='Ekstra:', font='Verdana 10 bold', background='#303030', foreground='#ffffff').place(x=40,y=140)
checkButton = Checkbutton(win, text='Sucuk', font='Verdana 10 bold', background='#303030', foreground='#2f6cad', activebackground='#303030', variable=check, onvalue='Sucuk')
checkButton.place(x=95,y=140)
checkButton2 = Checkbutton(win, text='Kaşar', font='Verdana 10 bold', background='#303030', foreground='#2f6cad', activebackground='#303030', variable=check2, onvalue='Kaşar')
checkButton2.place(x=165,y=140)
checkButton3 = Checkbutton(win, text='Mısır', font='Verdana 10 bold', background='#303030', foreground='#2f6cad', activebackground='#303030', variable=check3, onvalue='Mısır')
checkButton3.place(x=230,y=140)

labelText5 = Label(win, text='Adres:', font='Verdana 10 bold', background='#303030', foreground='#ffffff').place(x=40,y=170)
entryText2 = Entry(win, font='Verdana 10 bold', background='#ffffff', foreground='#303030', width=20)
entryText2.place(x=95,y=170)

buttonText = Button(win, text='Sipariş Ver', font='Verdana 10 bold', background='#303030', foreground='#ffffff', activebackground='green', width=10, command=verified).place(x=110, y=220)

win.mainloop()
