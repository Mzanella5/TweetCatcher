from TweetsReceiver import TweetsReceiver 
from TweetsController import TweetsController

import time
def main():
    receiver = TweetsReceiver()
    controller = TweetsController()
    
    words = list()
    words.append("#song")
    words.append("#music")
    words.append("#singer")
    words.append("#musician")

    while True:
        print("Coletando Tweets...")
        controller.listTweets(receiver.getTweets(words,1000))
        #controller.printTweets()
        controller.saveTweets()
        print("Durmindo...")
        time.sleep(300)
        

if __name__ == "__main__":
    main()