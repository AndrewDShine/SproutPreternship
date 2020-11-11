#!/usr/bin/env python
# coding: utf-8

# In[5]:


import tweepy

class Universal:
    # common fields between Twitter and LinkedIn
    text = ""
    content = ""
    
    # fields specific to posting on Twitter
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
    
    # fields specific to posting on Facebook
    post_id = ""
    actions = ""
    admin_creator = ""
    allowed_advertising_objectives = ""
    application = ""
    backdated_time = ""
    call_to_action = ""
    can_reply_privately = ""
    caption = ""
    child_attachments = ""
    comments_mirroring_domain = ""
    coordinates = ""
    created_time = ""
    delivery_growth_optimizations = ""
    description = ""
    entities = ""
    event = ""
    expanded_height = ""
    expanded_width = ""
    feed_targeting = ""
    formatting = ""
    from_user = ""
    full_picture = ""
    height = ""
    icon = ""
    implicit_place = ""
    instagram_eligibility = ""
    instream_eligibility = ""
    is_app_share = ""
    is_eligible_for_promotion = ""
    is_expired = ""
    is_hidden = ""
    is_inline_created = ""
    is_instagram_eligible = ""
    is_popular = ""
    is_published = ""
    is_spherical = ""
    link = ""
    live_video_elibility = ""
    message = ""
    message_tags = ""
    multi_share_end_card = ""
    multi_share_optimized = ""
    name = ""
    object_id = ""
    parent_id = ""
    permalink_url = ""
    place = ""
    poll = ""
    privacy = ""
    promotable_id = ""
    properties = ""
    publishing_stats = ""
    scheduled_publish_time = ""
    shares = ""
    source = ""
    
    # constructor for Twitter
    # as of now, user sends in the text for the tweet and can still change any of the other parameters
    # however, each additional parameter already has a default value as seen below
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
        
    # this function is used to interact with the Twitter API and post a tweet
    def post_to_Twitter(self, i):
        # Twitter login credentials needed for user authentication
        consumer_key = ['eEn8jAiNupIU9xw2eL12auAAP','bLouERJhNJ68I12yAQtHDD0hf']
        consumer_secret_key = ['SbUFHQqVeu7MtGsWrrweqTWizYbvdJV6aEbK1zFKnStNswtFHu', 'iR2iyjQsuvJdlI7D1BVsaY8SYGxaUqamuILmmZb2YzKSYKzNKw']
        access_token = ['2935650300-KJP9rCX1t8WB94GB9ZamTFNJEED76GmqJPk6Xmk', '1326605654388338689-T5ixwBNNbEfdsZUs5a6d2xV9wqF4TJ']
        access_token_secret = ['NCy7PT0CZmAnlkjXO5iFUkCnBDZKkgjmh1eXAX4ZpcX6n', 'RT6imWNvxoySMoDarnozUgmDcwEzLSzcp1yNCUtgzv8t1']
    
        # OAuth is taken care of in these three lines of code
        # the access token from above is set for authentication, allowing the user to interact with the API
        auth = tweepy.OAuthHandler(consumer_key[i], consumer_secret_key[i])
        auth.set_access_token(access_token[i], access_token_secret[i])
        api = tweepy.API(auth)
    
        # this line actually posts the tweet to Twitter
        status = api.update_status(status = self.text)


# In[6]:


# calling Twitter constructor to create Universal object
test = Universal("test with media")

# post to Twitter
#test.post_to_Twitter()


# In[ ]:





# In[ ]:




