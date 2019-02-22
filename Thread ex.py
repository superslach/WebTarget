import serial
from tkinter import *
from threading import Thread

#Partie Class pour le thread

class ecoute_arduino(Thread):
    def __init__(self, hard):
        Thread.__init__(self)
        self.hard = hard


    def run(self):
        while True:
            donnee = hard.readline().decode('utf-8')
            print(donnee)
            dVar.set(donnee)


hard = serial.Serial('COM5', 115200)
print(hard)
auditeur = ecoute_arduino(hard)
auditeur.start()

# Ma fenetre
fenetre = Tk()
fenetre.geometry("200x100")
fenetre.title("SR04")

# Mes éléments
dVar = StringVar()
valeur = Entry(fenetre, width=20, textvariable=dVar)
valeur.pack()

fenetre.mainloop()