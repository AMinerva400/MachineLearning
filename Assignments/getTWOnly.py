# Steven Lindo
# Sep 8, 2016
# Mining the Social Web - get Twitter Search Results

import twitter 
import csv
import sys
import json
from authTwitter import authTW
import re

def getSearch(t_obj, hashtag):
    q = hashtag  
    count = 100 
    search_results = t_obj.search.tweets( q = q, count = count) 
    statuses = search_results['statuses']
    tw_list = []
    for tw in statuses:
            tw_text = tw['text']
            tw_text = re.sub(r'RT @.+:', '', tw_text)
            tw_text = re.sub(r'https:.+ ', '', tw_text)
            tw_id   = tw['id']
            tw_list.append([tw_id, tw_text])
    return tw_list

def main():
    reload(sys)
    sys.setdefaultencoding('utf8')
    twitter_obj = authTW()
    A = getSearch(twitter_obj, '#Thanksgiving')
    B = getSearch(twitter_obj, '#BlackLivesMatter')
    C = getSearch(twitter_obj, '#Hofstra')
    Tweets = []
    Tweets.append(A)
    Tweets.append(B)
    Tweets.append(C)
    with open('generalizedTweets.csv', mode='w') as tweetsFile:
        tweetWriter = csv.writer(tweetsFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        tweetWriter.writerow(['ID', 'Tweet', 'Sentiment'])	
        for tweet in Tweets:
            for i in range(len(tweet)):
                tweetWriter.writerow(tweet[i])

main()
