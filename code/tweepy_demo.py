# Import modules
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Define variables
access_token = "26554014-QLQsVr6xxDlzryrbF594VEvCU7jF0J2Cks2It9gO0"
access_secret = "26zcLFhbSnal6XvYMPlIcyrmCuYq0IOGVqjM9KDnqErAz"
consumer_key = "mEGMn9i2XQfLHM5nybVXpytW0"
consumer_secret = "eziOMw5eCwcAUyFihFJN4SJiqcKOYvSmeIG5aqXMl9qXSuArBF"

# Create listener to print tweets to stdout
class StdOutListener (StreamListener):
	
	def on_data(self, data):
		print(data)
		return True
	
	def on_error(self, status):
		printr(status)

if __name__ == '__main__':
	
	# Handle Twitter authorization and connect to Twitter Streaming API
	list = StdOutListener()
	auth=OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	stream = Stream(auth, list)

	# Implement filter
	stream.filter(track=['#metoo'])
