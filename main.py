from operator import truediv

import translator as tr
from dictionary import Dictionary

t = tr.Translator()
d = Dictionary()

#popolo il dizionario di partenza
with open("dictionary.txt", "r") as file:
    for line in file:
        coppia = line.rstrip().split(" ")
        d.addWord(coppia[0], coppia[1])

#printare il menu
t.printMenu()
opzione = input("scegli opzione: ")

#Aggiungi nuova parola
if opzione == "1":
    nuovo = input("Ok, quale parola devo aggiungere: ")
    coppia = nuovo.lower().split(" ")
    verifica = True
    for lettera in coppia[0]:
        if lettera not in "qwertyuiopasdfghjklzxcvbnm":
            verifica = False
            break
    for lettera in coppia[1]:
        if lettera not in "qwertyuiopasdfghjklzxcvbnm":
            verifica = False
            break
    if verifica:
        d.addWord(coppia[0], coppia[1])
    else:
        print("hai digitato caratteri non validi")

#Cerca una traduzione
if opzione == "2":
    traduzione = input("Ok, quale parola devo tradurre: ")
    print(d.translate(traduzione.lower()))


'''
while(True):

    t.printMenu()

    t.loadDictionary("filename.txt")

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print()
        txtIn = input()
        pass
    if int(txtIn) == 2:
        pass
    if int(txtIn) == 3:
        pass
    if int(txtIn) == 4:
        break
'''