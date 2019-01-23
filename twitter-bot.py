import tweepy
import csv
import random
from time import sleep

FILE_NAME = 'carl-sagan-quotes.txt'
HALF_HOUR = 1800

# Here you have to insert the keys that you generated.
# To get the keys go to https://developer.twitter.com/
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET) # Access the Twitter API
api = tweepy.API(auth) # Create an instance of the API.

def get_phrase():
    with open(FILE_NAME) as csv_file:

        csv_reader = csv.reader(csv_file, delimiter='^') # Set the delimiter to '^' beacause the text contains commas
        phrases = list(csv_reader)
        
        selected_phrase = random.choice(phrases)[0]
   
        # Searches until it finds a phrase that has less than 280 characters (twitter status limit)
        while len(selected_phrase) > 280:
            selected_phrase = selected_phrase = random.choice(phrases)[0]

        return selected_phrase

def tweet_phrase():
    api.update_status(get_phrase())

# Post a tweet every half hour
while True:
    print('Tweeting a phrase...')
    tweet_phrase()
    print('Phrase tweeted succesfully!')
    sleep(HALF_HOUR)
