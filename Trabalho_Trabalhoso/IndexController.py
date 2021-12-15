import pickle
import sys
from struct import *

from Index import Index

class IndexController(object):
    "'Index Controller'"

    def __init__(self):
        pass

    def setIndex(self, id, position):
        try:
            file = open('index.bin','ab')
        except:
            file = open('index.bin','wb')

        #insercao no inicio
        bin = pack('qi', id, position)
        file.seek(0,2)
        n = file.write(bin)
        print( str( file.tell() -12 ) + ">indice salvo " + str(n) + " bytes")    
        file.close()
        #Ordena
        #self.unHappyBubbleSort()

    def getIndex():
        try:
            file = open('index.bin','rb')
        except:
            print("Erro: Não encontrei o arquivo index.bin")


        file.seek(position)
        index = file.read(12)
        index = pickle.loads(index)
        position = position + 12
        return index

        self.regPosition = 0

    def show(self):
        try:
            file = open('index.bin','rb')
        except:
            print("Erro: Não achei o arquivo index.bin")
            return

        while file.tell() >= 0:
            # Lê o tweet
            s = file.read(12)
            #desSerializa
            try:
                a,b = unpack('qi', s)

                print("POS: " + str(file.tell() - 12))
                print("ID: " + str(a))
                print("TWEET: " + str(b))
                print("===============================")
                
            except:
                break

        file.close()
        
    def unHappyBubbleSort(self):

        file = open('index.bin','ab')
        
        for index in file.read(200,2):
            index = pickle.loads(index)
            for index2 in file.read(200,2):
                index2 = pickle.loads(index2)
                if index.datetime < index2.datetime:
                    pass
                                        