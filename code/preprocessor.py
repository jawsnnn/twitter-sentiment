import re
import sys
import string

tweet = sys.argv[1]


def pre_process_tweets(tweet):
	# Turn tweets to lower case
	tweet = tweet.lower()

	# Ignore usernames (anything that starts with @)
	tweet = re.sub(r"\@\w+[^w]", "", tweet)
	
	# Eliminate repeated words
	tweet = re.sub(r"(\w+)\s+\1", r"\1", tweet)
		
	# Remove hashtags, just the pound signs, not the hashtag text
	tweet = re.sub(r"\#(\w+)", r" \1", tweet)

	# Remove punctuation marks
	tweet = tweet.translate(None, string.punctuation)
	
	# Eliminate extra or repeated spaces
	tweet = re.sub(r"\s+", " ", tweet)

	# Eliminate misspells. For now, this is three letters in a row
	tweet = re.sub(r"(\w)\1{1,}", r"\1\1", tweet)
	
	# Ignore words that are less than 3 letters in length
	tweet = [w for w in tweet.split() if len(w) >= 3]

	print tweet

pre_process_tweets(tweet)
