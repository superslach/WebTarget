from tkinter import *
from tkinter.messagebox import *
from fonction import *
import Interface.Liste_Mail as Liste_Mail


def callback(fen3, value, campagne):
    if askyesno('Confirmation', 'Continuer?'):
        showinfo('Validation', 'Import de l''URL en cours')
        mail_list = crawl(value)
        fen3.destroy()
        Liste_Mail.Liste_Mail(mail_list, campagne)
    else:
        showinfo('Annulation', 'Import de l''URL Interrompu')


def ImportURL(fen3, campagne):
    fen3.title("Importation d'une URL")
    Label(fen3, text='Saisir une URL : ', fg='red').pack()
    value = StringVar()
    Entry(fen3, width=40, textvariable=value).pack(side=LEFT, padx=5, pady=5)
    Button(fen3, text='Valider', command=lambda: callback(fen3, str(value.get()), campagne)).pack(side=RIGHT, padx=5, pady=5)
    fen3.mainloop()
