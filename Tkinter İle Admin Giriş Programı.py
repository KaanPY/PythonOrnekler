# İyi çalışmalar <3

from tkinter import *
import tkinter as tk

def control():
    if((entryText.get() == 'admin')and(entryText2.get() == '123456')):
        labelText8 = Label(win, text=' ', font='Verdana 10 bold', foreground='green', background='#303030', width=30).place(x=0, y=15)
        labelText7 = Label(win, text='> Giriş Yapıldı!', font='Verdana 10 bold', foreground='green', background='#303030').place(x=0, y=15)
        
        entryText.delete(0, 'end')
        entryText2.delete(0, 'end')
        entryText.focus()

        win2 = Tk()
        win2.geometry('320x310')
        win2.resizable(False, False)
        win2.configure(background='#303030')
        win2.wm_attributes('-alpha', 0.8)
        win2.title('Admin Hk')

        labelText5 = Label(win2, text='Yapım Aşamasında!', font='Verdana 15 bold', foreground='yellow', background='#303030').place(x=47, y=130)

        win2.mainloop()
    else:
        entryText2.delete(0, 'end')
        labelText6 = Label(win, text='> Kullanıcı adı veya şifre yanlış!', font='Verdana 10 bold', foreground='red', background='#303030').place(x=0, y=15)
        
win = Tk()
win.geometry('320x310+720+320')
win.resizable(False, False)
win.configure(background='#303030')
win.wm_attributes('-alpha', 0.9)
win.title('Admin Hk Giriş!')

labelText = Label(win, text='Admin HK', font='Verdana 15 bold', background='#303030', foreground='#ffffff').place(x=100,y=40)

labelText2 = Label(win, text='Kullanıcı Adı:', font='Verdana 10 bold', background='#303030', foreground='#ffffff').place(x=110,y=90)
entryText = Entry(win, font='Verdana 10 bold', width=12, background='#ffffff', foreground='#303030', justify='center')
entryText.place(x=105,y=115)
entryText.focus()
labelText3 = Label(win, text='Şifre:', font='Verdana 10 bold', background='#303030', foreground='#ffffff').place(x=140,y=145)
entryText2 = Entry(win, show='*', font='Verdana 10 bold', width=12, background='#ffffff', foreground='#303030', justify='center')
entryText2.place(x=105,y=170)

buttonEnter = Button(win, text='Giriş', font='Times 10 italic', foreground='#ffffff', background='#303030', width=10, activebackground='#2e2c2c', activeforeground='green', command=control).place(x=120, y=210)

labelText4 = Label(win, text='> Giriş Bilgileri; Kullanıcı Adı: admin, Şifre: 123456', font='Verdana 7 bold', foreground='#838383', background='#303030').place(x=5, y=260)

win.mainloop()
