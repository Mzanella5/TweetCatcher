import pickle
import sys
from struct import *
from collections import namedtuple

from Tweet import Tweet
from Index import Index
from IndexController import IndexController

class FileController(object):
    """index table controller"""

    def __init__(self):
        self.index = list()
        self.reg = 0      

    def saveTweet(self, tweet):
        try: 
            file = open('dados.bin','ab')
        except:
            file = open('dados.bin','wb')

        #file.seek(0,2)
        p = pack(
            'q50p280p200p30pq?',
            tweet.id,
            str(tweet.user).encode('utf-8'),
            str(tweet.message).encode('utf-8'),
            str(tweet.hashtags).encode('utf-8'),
            str(tweet.datetime).encode('utf-8'),
            -1, # >= 0 significa que referencia uma posição do arquivo de extencao
            False #Se true o mesmo pode ser subtituido
            )

        size = file.write(p)
        self.reg+= 1
        print("Salvando: " + str(tweet.id) + " @" + tweet.user + " | " + str(self.reg) )
        if(self.reg >= 1000):
            self.reg = 0
        #print( str(file.tell() - 577) + "> Tweet Salvo " + str(size) + " bytes")
        #IndexController.setIndex(self,tweet.id, file.tell()) # insere o registro de indice contendo o tamanho em bytes do tweet e o id do mesmo 
        file.close()            
        
    def show(self):

        try:
            file = open('dados.bin','rb')
        except:
            print("Erro: Não achei o arquivo dados.bin")
            return

        while file.tell() >= 0:
            # Lê o tweet
            s = file.read(577)
            #desSerializa
            try:
                a,b,c,d,e,f,g = unpack('q50p280p200p30pq?', s)

                print("ID: " + str(a))
                print("=======@"+ b.decode() +"========")
                print(c.decode())
                print("Hashtags: " + d.decode())
                print("Data: " + e.decode())
                print("Excluido: " + str(g))
                print("===============================")
            except:
                break

        file.close()

    def change(self, id, tweet):
        pass

    def remove(self, id):
        pass



