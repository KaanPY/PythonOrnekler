# İyi çalışmalar <3

from tkinter import *
import tkinter as tk

def control():
    if((entryText.get() == 'admin')and(entryText2.get() == '123456')):
        win2 = Tk()
        win2.title('Admin Panel!')
        win2.geometry('250x250')
        win2.configure(background='#303030')
        win2.resizable(False, False)
        win2.wm_attributes('-alpha', 0.9)

        welcomeAdmin = Label(win2, text='Yapım aşamasında!', font='Verdana 12 bold', foreground='#e63e0b', background='#303030').place(x=40, y=90)

        win2.mainloop()
    else:
        labelText.configure(text='> Kullanıcı Adı Veya Şifre Yanlış!', font='Verdana 10 bold', foreground='red')

win = Tk()
win.geometry('350x300')
win.title('Admin Giriş!')
win.configure(background='#303030')
win.resizable(False, False)

labelText = Label(win, text='Giriş Yapınız!', font='Verdana 15 bold', foreground='orange',backgroun='#303030', width='25', justify='center')
labelText.place(x=0, y=40)
text1 = Label(win, text='Kullanıcı Adı:', font='Verdana 10 bold', foreground='#ffffff', background='#303030').place(x=1, y=80)
text2 = Label(win, text='Şifre:', font='Verdana 10 bold', foreground='#ffffff', background='#303030').place(x=55, y=110)
text3 = Label(win, text='> Giriş bilgileri; Kullanıcı Adı: admin, Şifre: 123456', font='Verdana 8 bold', foreground='#818386', background='#303030').place(x=0, y=210)

entryText = Entry(win, font='Verdana 10 bold', foreground='#0070b6', width='15', background='#ffffff')
entryText.place(x=102, y=80)
entryText2 = Entry(win,show='*', font='Verdana 10 bold', foreground='#0070b6', width='15', background='#ffffff')
entryText2.place(x=102, y=110)

buttonInput = Button(win, text='Giriş Yap', font='Vedana 10 bold', foreground='#ffffff', width='10', background='#00bb18', command=control).place(x=120, y=140)

win.mainloop()
