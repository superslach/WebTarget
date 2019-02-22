from tkinter import *
from tkinter.messagebox import *
from fonction import *
import Interface.Liste_Mail as Liste_Mail

def callback(fen,val, campagne):
    if askyesno('Confirmation', 'Continuer?'):
        showinfo('Validation', 'Import du CSV en cours')
        lecture = read_file(val)
        mail_list = lecture.split(",")
        fen.destroy()
        Liste_Mail.Liste_Mail(mail_list, campagne)
    else:
        showinfo('Annulation', 'Import du CSV Interrompu')


def ImportCSV(fen2, campagne):
    fen2.title("Importation depuis un CSV")
    Label(fen2, text='Saisir un CSV : ', fg='red').pack()
    value = StringVar()
    Entry(fen2, width=40, textvariable=value).pack(side=LEFT, padx=5, pady=5)
    Button(fen2, text='Valider', command=lambda: callback(fen2, str(value.get()), campagne)).pack(side=RIGHT, padx=5, pady=5)
    fen2.mainloop()




