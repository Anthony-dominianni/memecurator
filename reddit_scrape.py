import praw
import requests
import shutil
import os
import datetime

"""
Open a reddit instance
"""
reddit = praw.Reddit(client_id='clientid',
                     client_secret='clientsecret',
                     user_agent='useragent',
                     username='username',
                     password='password')

dank_memes = reddit.subreddit('dankmemes')

""" 
Make a new directory for today's dankest memes
"""

path = '/Users/anthonydominianni/Desktop/ComeUp/donaldSlump/Pictures'
today = datetime.datetime.now().strftime("%Y-%m-%d")
newfolder = path + '/' + today

try:
	os.mkdir(newfolder)
	print(newfolder + " created")
except FileExistsError:
	print(newfolder + " already exists")

"""
Download pictures like a boss
"""
for submission in dank_memes.top(limit=10, time_filter='week'):
	if (not submission.stickied and not submission.is_video):
		r = requests.get(submission.url, stream=True)
		if r.status_code == 200:
			with open(newfolder + '/' + submission.title + '.jpg', 'wb') as f:
				r.raw.decode_content = True
				shutil.copyfileobj(r.raw, f)

