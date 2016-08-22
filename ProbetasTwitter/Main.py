import TwitterClass
import time

consumer_key = ""               #GO TO TWITTER TO FIND THIS INFO
consumer_secret = ""
access_token = ""
access_token_secret = ""

numberOfTweets = [0,0,0,0]
lastTweet = ["", "", "", ""]

twitterObj = TwitterClass.TwitterClass(consumer_key, consumer_secret, access_token, access_token_secret)


while True:

    #Search the last tweet of the first plant
    currentTwit = twitterObj.getLastTweetWithoutRT("#SalvarPrimera")
    if lastTweet[0] != currentTwit:
        numberOfTweets[0] = numberOfTweets[0] + 1
        lastTweet[0] = currentTwit

    currentTwit = twitterObj.getLastTweetWithoutRT("#SalvarSegunda")
    if lastTweet[1] != currentTwit:
        numberOfTweets[1] = numberOfTweets[1] + 1
        lastTweet[1] = currentTwit

    currentTwit = twitterObj.getLastTweetWithoutRT("#SalvarTercera")
    if lastTweet[2] != currentTwit:
        numberOfTweets[2] = numberOfTweets[2] + 1
        lastTweet[2] = currentTwit

    currentTwit = twitterObj.getLastTweetWithoutRT("#SalvarCuarta")
    if lastTweet[3] != currentTwit:
        numberOfTweets[3] = numberOfTweets[3] + 1
        lastTweet[3] = currentTwit

    print("-------------------------")
    print(numberOfTweets[0])
    print(numberOfTweets[1])
    print(numberOfTweets[2])
    print(numberOfTweets[3])
    time.sleep(60)
