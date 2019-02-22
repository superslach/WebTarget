from tkinter import *
from tkinter.messagebox import *
from Interface.Liste_Mail import *

def callback(fen1,campagne):
    if askyesno('Confirmation', 'Continuer?'):
        showinfo('Validation', 'Nom de la campagne pris en compte en cours')
        fen1.destroy()
        write_file(campagne,"")
        mail=[]
        Liste_Mail(mail, campagne)


    else:
        showinfo('Annulation', 'Nom de la campagne non pris en compte')


fen1 = Tk()
fen1.title("Nom Campagne")
Label(fen1, text='Saisir un nom de campagne : ', fg='red').pack()
value = StringVar()
Entry(fen1, width=40, textvariable=value).pack(side=LEFT, padx=5, pady=5)
Button(fen1, text='Valider', command=lambda: callback(fen1, str(value.get()))).pack(side=RIGHT, padx=5, pady=5)
fen1.mainloop()



