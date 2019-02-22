from tkinter import *
from tkinter.messagebox import *
from fonction import *
from Interface.Mail import *
from Interface.Liste_Mail import *


def send_mail(info, mail_test):
    if verif_email(mail_test):
        exp = info["expediteur"]
        obj = info["objet"]
        msg = info["message"]
        pwd = info["password"]
        envoi_mail(exp, mail_test, obj, msg, pwd)


def send_all_mail(info, mail_list, campagne):
    exp = info["expediteur"]
    obj = info["objet"]
    msg = info["message"]
    pwd = info["password"]
    for ligne in mail_list:
        write_file(campagne,ligne)
        envoi_mail(exp, ligne, obj, msg, pwd)


def test_mail(fen4, info, mail_list, campagne):
    fen4.title("Test pour l'envoi")
    tex1 = Label(fen4, text='Mail test ', fg='blue').grid(row=1, column=0, padx=5, pady=5)
    mail_test = StringVar()
    Entry(fen4, width=40, textvariable=mail_test).grid(row=1, column=1, padx=5, pady=5)
    bou1 = Button(fen4, text='Valider', command=lambda: send_mail(info, str(mail_test.get()))).grid(row=1, column=3, padx=5, pady=5)
    bt_accepter_all = Button(text='Envoyer à toute la liste', command=lambda: send_all_mail(info, mail_list, campagne)).grid(row=2, column=1, padx=5, pady=5)
    fen4.mainloop()