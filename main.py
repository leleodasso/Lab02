import sys
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


opzione = 0

while opzione != "5":
    # printare il menu
    t.printMenu()
    opzione = input("scegli opzione: ")


    #Aggiungi nuova parola
    if opzione == "1":
        nuovo = input("Ok, quale parola devo aggiungere: ")
        alien_ita = nuovo.lower().split(" ")
        verifica = True
        if len(alien_ita) == 2:
            for parola in alien_ita:
                for lettera in parola:
                    if lettera not in "qwertyuiopasdfghjklzxcvbnm ":
                        verifica = False
                        break
            if verifica:
                d.addWord(alien_ita[0], alien_ita[1], True)
                print("['"+alien_ita[0]+"', '"+alien_ita[1]+"']")
                print("Aggiunta!")
            else:
                print("hai digitato caratteri non validi")
        if len(alien_ita) > 2:
            for parola in alien_ita:
                for lettera in parola:
                    if lettera not in "qwertyuiopasdfghjklzxcvbnm ":
                        verifica = False
                        break
            if verifica:
                for i in range(1, len(alien_ita)):
                    d.addWord(alien_ita[0], alien_ita[i], True)
            else:
                print("hai digitato caratteri non validi")


    #Cerca una traduzione
    if opzione == "2":
        traduzione = input("Ok, quale parola devo tradurre: ")
        print(d.translate(traduzione.lower()))

    #Wildcard
    if opzione == "3":
        traduzione_wild = input("Ok, quale parola con wildcard devo tradurre: ")
        print(d.translateWordWildCard(traduzione_wild.lower())[0])
        print(d.translateWordWildCard(traduzione_wild.lower())[1])


    #stampa dizionario
    if opzione == "4":
        with open("dictionary.txt", "r") as file:
            for line in file:
                print(line)

    if opzione not in "12345":
        raise print("input digitato non valido")

if opzione == "5":
    print("chiusura programma")
    sys.exit()
