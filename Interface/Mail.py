from tkinter import *
from tkinter.messagebox import *
from Interface.Test_Mail import *
from Interface.Liste_Mail import *


def t_mail(fenetre, exp, obj, msg, pwd, mail_list, campagne):
    info = {"expediteur": exp, "objet":obj, "message": msg, "password":pwd}
    fenetre.destroy()
    fenetre1 = Tk()
    test_mail(fenetre1, info, mail_list, campagne)


def mail(fen5, mail_list, campagne):
    fen5.title("Envoi du Mail")
    tex1 = Label(fen5, text='Expéditeur : ', fg='black').grid(row=1, column=0, padx=5, pady=5)
    nom = StringVar()
    Entry(fen5, width=40, textvariable=nom).grid(row=1, column=1, padx=5, pady=5)
    tex2 = Label(fen5, text='Objet : ', fg='black').grid(row=2, column=0, padx=5, pady=5)
    nom2 = StringVar()
    Entry(fen5, width=40, textvariable=nom2).grid(row=2, column=1, padx=5, pady=5)
    tex3 = Label(fen5, text='Message : ', fg='black').grid(row=3, column=0, padx=5, pady=5)
    nom3 = StringVar()
    Entry(fen5, width=40, textvariable=nom3).grid(row=3, column=1, padx=5, pady=5)
    tex3 = Label(fen5, text='Mot de Passe : ', fg='black').grid(row=4, column=0, padx=5, pady=5)
    nom4 = StringVar()
    Entry(fen5, width=40, textvariable=nom4).grid(row=4, column=1, padx=5, pady=5)
    bou1 = Button(fen5, text='Valider', command=lambda: t_mail(fen5, str(nom.get()), str(nom2.get()), str(nom3.get()), str(nom4.get()), mail_list, campagne)).grid(row=5, column=1, padx=5, pady=5)
    fen5.mainloop()
