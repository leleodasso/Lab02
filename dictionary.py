#import re

class Dictionary:
    def __init__(self, dizionario = {}):
        self.dizionario = dizionario

    def addWord(self, aliena, italiano, flag_input=False):
        if flag_input == False:
            if aliena not in self.dizionario:
                lista = [italiano]
                self.dizionario[aliena] = lista
            else:
                self.dizionario[aliena].append(italiano)
        if flag_input == True:
            if aliena not in self.dizionario:
                lista = [italiano]
                self.dizionario[aliena] = lista
            else:
                self.dizionario[aliena].append(italiano)
            file = open("dictionary.txt", "a")
            file.write(aliena + " " + italiano+"\n")
            file.close()


    def translate(self, aliena):
        stringa = ""
        i=0
        for p in self.dizionario[aliena]:
            i += 1
            stringa += p+" "
        return stringa

    def translateWordWildCard(self,aliena_wild):
        stringa = ""
        i = 0
        for lettera in "qwertyuiopasdfghjklzxcvbnm":
            if aliena_wild.replace("?",lettera) in self.dizionario:
                for p in self.dizionario[aliena_wild.replace("?", lettera)]:
                    temp = aliena_wild.replace("?", lettera)
                    i += 1
                    stringa += p + "'], ['"
            else:
                pass
        array = [temp, "['"+stringa[:-4]]
        return array

