from Tweet import Tweet
from FileController import FileController
from IndexController import IndexController

class TweetsController(object):
    """description of class"""
    def __init__(self):
        self.lista = list()
        self.fileController = FileController()
        self.indexController = IndexController()

    def printTweets(self):
        for t in self.lista:
            print("======== ID: " + str(t.id) + " User: @" + t.user + " ========")
            print(t.message + ">>>") 
            print("Data:" + str(t.datetime))
            for tag in t.hashtags:
                print(tag + " " + str(len(tag)))

            print(len(t.hashtags))

    def listTweets(self, tweets):
        for t in tweets:            
            self.lista.append(Tweet(t.id, t.user.screen_name, t.text, self.getHashtags(t.text), t.created_at))

    def saveTweets(self):
        for t in self.lista:
            self.fileController.saveTweet(t)
        #self.fileController.show()
        #self.indexController.show()


    @staticmethod
    def getHashtags(text):
        s_return = list()
        aux = ""
        for i in range(1,len(text)):
            if(text[i] != '#' and text[i] != ' ' and text[i] != '…'):
                aux = aux + text[i]
            if(text[i] == '#' or text[i] == '…'):                
                s_return.append('#' + aux)
                aux = ""

        s_return.pop(0)
        return s_return


                
                   



