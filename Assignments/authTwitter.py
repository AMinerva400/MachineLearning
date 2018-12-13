# Prof. Steven Lindo
# October 2017
# Data Mining Twitter - Twitter Auth example
# Required: pip install twitter
# Go to app.twitter.com to create your own app and generate keys

import twitter

def authTW():
	CONSUMER_KEY 	= 'TvCZMTQiFqfdQvTBD9pjcP7er' 
	CONSUMER_SECRET = 'jIsY3uRqcUjL7OaUgGq5ZDzmbDH89BmRdLoXuQxCPF2GwERZXT'

	OAUTH_TOKEN 		= '831305604694163456-yv1JNqaALtufztgZNvwh6Y2sWh7DReo' 
	OAUTH_TOKEN_SECRET 	= '2ZAhYp7MxvXUe40pLxq5xDF377ninAJPDUzeBdejvcYHi' 
	auth 		= twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET) 
	
	twitter_api 	= twitter.Twitter(auth = auth)
	
	return twitter_api

def authTWStream():
	CONSUMER_KEY    = 'TvCZMTQiFqfdQvTBD9pjcP7er'
        CONSUMER_SECRET = 'jIsY3uRqcUjL7OaUgGq5ZDzmbDH89BmRdLoXuQxCPF2GwERZXT'

        OAUTH_TOKEN             = '831305604694163456-yv1JNqaALtufztgZNvwh6Y2sWh7DReo'
        OAUTH_TOKEN_SECRET      = '2ZAhYp7MxvXUe40pLxq5xDF377ninAJPDUzeBdejvcYHi'
	auth 			= twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET) 
	twitter_stream_api 	= twitter.TwitterStream(auth = auth) 

	return twitter_stream_api

tw_obj = authTW()
print(tw_obj)

