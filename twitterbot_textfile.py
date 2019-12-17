#!/usr/bin/python3
# import Twitter credentials from credentials.py
import tweepy
from credentials import *
from time import sleep
import sys

# Access & authorize our twitter credentials from credentials.py
auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")
auth.set_access_token("access_token", "access_token_secret")
api = tweepy.API(auth)

#Create API object

"""
The following code snippet creates an API object that you can use 
to invoke Twitter API methods. Setting wait_on_rate_limit and 
wait_on_rate_limit_notify to True makes the API object print a 
message and wait if the rate limit is exceeded
"""
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

# Open text file verne.txt (or your chosen file) for reading
my_file = open('funny.txt', 'r')

# Read lines one by one from my_file and assign to file_lines variable
file_lines = my_file.readlines()

# Close file
my_file.close()

for line in file_lines:

# Add try ... except block to catch and output errors
	try:
		print(line)

# Add if statement to ensure that blank lines are skipped
		if line != '\n':
			api.update_status(line)

# Add an else statement with pass to conclude the conditional statement\\\	
		else:
			pass
	except tweepy.TweepError as e:
		print(e.reason)

# Add sleep method to space tweets by 5 seconds each
		sleep(4500)


    	

	
	


	