import random 

class Notebook:
    def __init__(self):
        self.__notes = list()
        self.numberOfNotes()
    
    def storeNote(self,note):
        self.__notes.append(note)
 
    def numberOfNotes(self):
        return len(self.__notes)
    
    def showNote(self,noteNumber):
        if noteNumber >= 0 and noteNumber < self.numberOfNotes():
            print(self.__notes[noteNumber])
        else:
            print("Este não é um número de nota válido")

    def removeNote(self, note):
        if note in self.__notes:
            self.__notes.remove(note)
        
        else:
            print("Esta não é uma nota válida")
    
    def listNotes(self):
        index = 0
        while index < self.numberOfNotes():
            print(self.__notes[index])
            print("\n")
            index += 1

    def listNotesfor(self):
        for index in range (0, self.numberOfNotes()):
            print(self.__notes[index])
            print("\n")
    
    def hasNotes(self):
        if self.numberOfNotes() != 0:
            return True
        
        else:
            return False
        
    def compareNote(self, note):
        if note in self.__notes:
            return True
        
        else:
            return False
        
    def showNoteRandom(self):
        print(random.choice(self.__note))
     
    def showMultiNoteRandom(self, numNotes):
        index = 0
        if int(numNotes) <= self.numberOfNotes():
            while index < int(numNotes):
                print(random.choice(self.__note))
                index += 1
        else:
            print("Lista vazia.")
