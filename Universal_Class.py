#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tweepy
from json import dumps

class Universal:
    # common fields
    text = ""
    content = ""
    
    # fields specific to Twitter
    in_reply_to_status_id = ""
    auto_populate_reply_metadata = ""
    exclude_reply_user_ids = ""
    media_ids = ""
    possibly_sensitive = ""
    latitude = ""
    longitude = ""
    place_id = ""
    display_coordinates = ""
    trim_user = ""
    enable_dmcommands = ""
    fail_dmcommands = ""
    card_uri = ""
    
    # fields specific to LinkedIn
    
    
    # constructor for Twitter
    def __init__(self, tweet_text, reply = None, metadata = True, exclude_reply = True, 
                 attachment = None, media = None, sensitivity = False, lat = 27.2046, 
                 long = 77.4977, place = None, display = False, trim = False, 
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
        
    # constructor for LinkedIn
    # def __init__(self)
        
    def post_to_Twitter(self):
        # Twitter login credentials
        consumer_key = 'eEn8jAiNupIU9xw2eL12auAAP'
        consumer_secret_key = 'SbUFHQqVeu7MtGsWrrweqTWizYbvdJV6aEbK1zFKnStNswtFHu'
        access_token = '2935650300-KJP9rCX1t8WB94GB9ZamTFNJEED76GmqJPk6Xmk'
        access_token_secret = 'NCy7PT0CZmAnlkjXO5iFUkCnBDZKkgjmh1eXAX4ZpcX6n'
    
        auth = tweepy.OAuthHandler(consumer_key,consumer_secret_key)
        auth.set_access_token(access_token,access_token_secret)
        api = tweepy.API(auth)
    
        status = api.update_status(status = self.text)
    
    #def post_to_LinkedIn():
        


# Want to try and make the latitude and longitude update according to the current location of device posting the tweet -- looking into geopy (https://pypi.org/project/geopy/)

# In[4]:


# calling Twitter constructor to create Universal object
test = Universal("test 3")

# post to Twitter
#test.post_to_Twitter()


# In[ ]:




