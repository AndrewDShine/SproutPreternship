#!/usr/bin/env python
# coding: utf-8

# In[1]:


from queue import PriorityQueue

# Universal_Class must be saved as a .py in the same folder
from Universal_Class import Universal

# posts to Twitter in order of priority queue
def post(q):
    while not q.empty():
        item = q.get()
        try:
            # post is second element in item list and user is third
            item[1].post_to_Twitter(item[2]) 
        except:
            # will cause error if same message already tweeted
            print("Error") 


# In[2]:


def get_user_input (q):
    # list of priorities used to ensure unique priorities
    priorities = []
    # keep getting data for post until user decides to quit
    quit = False
    while (not quit):
        # get user input for tweet text
        text = input("Enter tweet text: ")
        # create universal object with inputed text
        post = Universal(text)
        # boolean for if input is valid
        valid = False
        # loop while input in invalid
        while not valid:
            priority = input("Enter priority for tweet: ")
            # check if priority is integer
            try:
                priority = int(priority)
                # make sure entered priority not in list
                if priority not in priorities:
                    valid = True
                    priorities.append(priority)
                else:
                    print("A different tweet has that priority. Enter a different priority.")
            except:
                print("Error: priority must be an integer")
        # set valid back to false for input of user
        valid = False
        while not valid:
            # get user input for which Twitter account to post to
            user = input("Enter a user (0 or 1): ")
            # check if input is 0 or 1
            try:
                user = int(user)
                if user == 0 or user == 1:
                    valid = True
                else:
                    print("Enter 0 or 1")
            except:
                print("Enter an integer (0 or 1)")
        # put data into priority queue
        q.put((priority, post, user))
        # check if user want to quit
        done = input("Would you like to post another tweet? (y or n): ")
        if (done == 'n'):
            quit = True

