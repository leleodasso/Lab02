

class Dictionary:
    def __init__(self, dizionario = {}):
        self.dizionario = dizionario

    def addWord(self, aliena, italiano):
        if aliena not in self.dizionario:
            self.dizionario[aliena] = italiano
        else:
            if isinstance(self.dizionario[aliena], str):
                lista = [self.dizionario[aliena], italiano]
                self.dizionario[aliena] = lista
            elif isinstance(self.dizionario[aliena], list):
                self.dizionario[aliena].append(italiano)

    def translate(self, aliena):
        return self.dizionario[aliena]

    def translateWordWildCard(self):
        pass

