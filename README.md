# An Automated Job finder that posts Jobs to twitter

A **Python** project that that gets jobs from job boards and posts them on twitter using a twitter bot.

## What app will do
1. Get job listings from the job boards. 
2. Combine all the listings in a list.
3. Using Tweepy, post the items of the list at random times on twitter.

## Setting Up the project.
### Set up twitter developer account
First of all, You should open a [twitter developer](https://developer.twitter.com/) account if you don't have one. The account will provide an API that you are going to need 
in order to develop a bot. The API also manages and performs other  activities within the  Twitter account such as Tweets count, Search tweets, retweets, follow 
and many more. Check out the [Documentation](https://developer.twitter.com/en/docs)

Apply for the API, its quite straight forward. Give the reasons on how you are going to use the API and such.
Once your application is successiful, get the API KEYS and you are set.

### Write your code
- First install python
 ``` pip install python ```
- We will using a pythonlibrary called Tweepy to create the bot. Install tweepy
  ``` pip install tweepy ```
 
### Authenticate your App
This is the part that authenticates your application using the API KEYS.
 ``` 
    CONSUMER_KEY = 'your API key number here'
    CONSUMER_SECRET = 'your API secret key number here'
    ACCESS_KEY = 'your access token here'
    ACCESS_SECRET = 'your access token secret here'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET) 
```
### Write your code
- The python script gets jobs from job boards using the ` feedparser ` which gives results in json format.
  Or just write a simple code of what you want your bot to do.

- I have the hashtags the bot is attaching to the tweets in the file hastags.txt-
    This is the part that gets them 

 
``` 
with open('hashtag.txt', 'r') as f:    
    hashtag = f.readlines()

hashtag = [x.strip() for x in hashtag]
```

 ### The bot in action
![Bot in action](images/bot.png)


## Uploading the code to heroku
I will be updating on how to host the code in a cloud servives for automation


## Links
[How To Create An Automated Remote Job Finder](https://towardsdatascience.com/how-to-create-an-automated-remote-job-finder-with-python-7e20ee233e2b) 