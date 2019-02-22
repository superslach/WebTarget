from tkinter.messagebox import *
from Interface.ImportCSV import *
from Interface.ImportURL import *
from Interface.Mail import *


def import_url(fenetre, campagne):
    fenetre.destroy()
    fenetre1 = Tk()
    ImportURL(fenetre1, campagne)


def import_csv(fenetre, campagne):
    fenetre.destroy()
    fenetre1 = Tk()
    ImportCSV(fenetre1, campagne)


def ecrit_mail(fenetre, mail_list, campagne):
    fenetre.destroy()
    fenetre1 = Tk()
    mail(fenetre1, mail_list, campagne)


def erase(fenetre, mail_list, campagne):
    fenetre.destroy()
    new_list = supp_doublon(mail_list)
    Liste_Mail(new_list,campagne)


def verif (fenetre, mail_list, campagne):
    fenetre.destroy()
    new_list = []
    for mail in mail_list:
        if verif_email(mail):
            mail = mail.replace('"', '')
            new_list.append(mail)
    Liste_Mail(new_list, campagne)


def Liste_Mail(mail_list,campagne):
    fen6 = Tk()
    fen6.title("Liste de Mails")
    Button1 = Button(fen6, text='Dédoublonner', command=lambda: erase(fen6, mail_list, campagne)).grid(row=1, column=0, padx=5, pady=5)
    Button2 = Button(fen6, text='Vérification', command=lambda: verif(fen6, mail_list, campagne)).grid(row=1, column=1, padx=5, pady=5)
    Button3 = Button(fen6, text='Import CSV', command=lambda: import_csv(fen6, campagne)).grid(row=2, column=0, padx=5, pady=5)
    Button4 = Button(fen6, text='Import URL', command=lambda: import_url(fen6, campagne)).grid(row=2, column=1, padx=5, pady=5)
    tex1 = Label(fen6, text='Liste de mail : ', fg='green').grid(row=3, column=0, padx=5, pady=5)

    if len(mail_list) > 0:
        for ligne in range(len(mail_list)):
                Label(fen6, text=mail_list[ligne], borderwidth=1).grid(row=ligne + 4, column= 1)
    else:
        Label(fen6, text='Pas encore de mail', borderwidth=1).grid(row=4, column=2)

    bou1 = Button(fen6, text='Valider', command=lambda: ecrit_mail(fen6, mail_list, campagne)).grid(row=len(mail_list)+5, column=1, padx=5, pady=5)

    fen6.mainloop()