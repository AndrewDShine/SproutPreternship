#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy
from IPython.html.widgets.interaction import interact
from ipywidgets import interact

class Universal:
    
    # fields specific to posting on Twitter
    status = ""
    in_reply_to_status_id = ""
    auto_populate_reply_metadata = ""
    exclude_reply_user_ids = ""
    attachment_url = ""
    media_ids = ""
    possibly_sensitive = ""
    place_id = ""
    latitude = ""
    longitude = ""
    display_coordinates = ""
    trim_user = ""
    enable_dmcommands = ""
    fail_dmcommands = ""
    card_uri = ""
    
    # constructor for Twitter
    # as of now, user sends in the text for the tweet and can still change any of the other parameters
    # however, each additional parameter already has a default value as seen below
    def __init__(self, tweet_text = None, reply = None, metadata = True, exclude_reply = True, 
                 attachment = None, media = None, sensitivity = False, lat = 27.2046, 
                 long = 77.4977, place = None, display = True, trim = False, 
                 enable = False, fail = True, card = None):
        self.text = tweet_text
        self.in_reply_to_status_id = reply
        self.auto_populate_reply_metadata = metadata
        self.exclude_reply_user_ids = exclude_reply
        self.content = attachment
        self.media_ids = media
        self.possibly_sensitive = sensitivity
        self.latitude = lat
        self.longitude = long
        self.place_id = place
        self.display_coordinates = display
        self.trim_user = trim
        self.enable_dmcommands = enable
        self.fail_dmcommands = fail
        self.card_uri = card
    
    # this function is able to change the fields of the class based on user input
    # it is the equivalent of a .set method
    def interactive_Tweet(self, tweet_text, reply, metadata, 
                 attachment, media, sensitivity, lat, 
                 long, place, display, trim, 
                 enable, fail): 
        self.text = tweet_text
        self.in_reply_to_status_id = reply
        self.auto_populate_reply_metadata = metadata
        self.content = attachment
        self.media_ids = media
        self.possibly_sensitive = sensitivity
        self.latitude = lat
        self.longitude = long
        self.place_id = place
        self.display_coordinates = display
        self.trim_user = trim
        self.enable_dmcommands = enable
        self.fail_dmcommands = fail
        
    # this function calls the interact method on the interactive_Tweet method
    # it allows the user to input information to change the fields in the class
    def interact(self): 
        interact(self.interactive_Tweet, tweet_text = "Enter tweet text here", 
                 reply = "Enter usernames here or leave blank", 
                metadata = False, attachment = "Enter Twitter url here or leave blank", 
                 media = "Enter media ids here or leave blank", 
                sensitivity = False, lat = "Enter coordinate for latitude", 
                 long = "Enter coordinate for longitude", 
                place = "Enter place id (number) or leave blank", display = True, trim = False, 
                enable = False, fail = True)
        
    # this function is used to interact with the Twitter API and post a tweet
    def post_to_Twitter(self, user):
        # Twitter login credentials needed for user authentication
        # there are currently two accounts that this program can post to
        # the first one is Ashley's personal Twitter account
        # the second one is a test account that we made, it's username is @test18734847
        consumer_key = ['eEn8jAiNupIU9xw2eL12auAAP','bLouERJhNJ68I12yAQtHDD0hf']
        consumer_secret_key = ['SbUFHQqVeu7MtGsWrrweqTWizYbvdJV6aEbK1zFKnStNswtFHu', 
                               'iR2iyjQsuvJdlI7D1BVsaY8SYGxaUqamuILmmZb2YzKSYKzNKw']
        access_token = ['2935650300-KJP9rCX1t8WB94GB9ZamTFNJEED76GmqJPk6Xmk', 
                        '1326605654388338689-T5ixwBNNbEfdsZUs5a6d2xV9wqF4TJ']
        access_token_secret = ['NCy7PT0CZmAnlkjXO5iFUkCnBDZKkgjmh1eXAX4ZpcX6n', 
                               'RT6imWNvxoySMoDarnozUgmDcwEzLSzcp1yNCUtgzv8t1']
    
        # OAuth is taken care of in these three lines of code
        # the access token from above is set for authentication, allowing the user to interact with the API
        auth = tweepy.OAuthHandler(consumer_key[user], consumer_secret_key[user])
        auth.set_access_token(access_token[user], access_token_secret[user])
        api = tweepy.API(auth)
    
        # this line actually posts the tweet to Twitter
        status = api.update_status(status = self.text)

