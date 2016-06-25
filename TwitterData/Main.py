import TwitterClass


consumer_key = ""               #GO TO TWITTER TO FIND THIS INFO
consumer_secret = ""
access_token = ""
access_token_secret = ""

twitterObj = TwitterClass.TwitterClass(consumer_key, consumer_secret, access_token, access_token_secret)
twitterObj.searchTweets()
