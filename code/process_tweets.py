import re
import sys
import string
import json

rawfile = sys.argv[1]

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
	tweet = string.translate(tweet, None, string.punctuation)
	#tweet = tweet.translate({ord(c):None for c in string.punctuation})
	
	# Eliminate extra or repeated spaces
	tweet = re.sub(r"\s+", " ", tweet)

	# Eliminate misspells. For now, this is three letters in a row
	tweet = re.sub(r"(\w)\1{1,}", r"\1\1", tweet)
	
	# Ignore words that are less than 3 letters in length
	tweet = [w for w in tweet.split() if len(w) >= 3]
	return tweet
counter = 0
with open(rawfile, 'rb') as fr:
	for line in fr:
		#print "PREPROCESSED: "+re.sub(r'[\r\n]', '', line)
		if re.sub(r'[\r\n]', '', line):
			try:
				data = json.loads(re.sub(r'[\r\n]', '', line))
				counter+= 1
				if data['lang'] == 'en':
					print(pre_process_tweets(data['text'].encode('utf-8')))
			except KeyError as ke:
				print("Ignoring non-english lines")
				continue
			except Exception as e:
				print(line)
				raise e
