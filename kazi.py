from datetime import datetime, timezone
import time, random, feedparser, tweepy
from  config import *

TIMELIMIT = 90000 # Around 25 hours

def get_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)


def check_if_offer_is_valid(entry):
    # Not valid if older than TIMELIMIT
    now = datetime.timestamp(datetime.now(timezone.utc))
    parsed_date = entry.get('published', 'Thu, 24 Jan 1991 03:00:00 +0000')
    entry_date = datetime.strptime(parsed_date, '%a, %d %b %Y %H:%M:%S %Z').timestamp()

    if now - entry_date > TIMELIMIT:
        return False
    return True

def get_myjobmag_offers():
    rss = feedparser.parse('https://www.myjobmag.co.ke/jobsxml.xml')
    entries = rss.entries
    offers = [e for e in entries if check_if_offer_is_valid(e) is True]

    return [
        {
            'title': offer.get('title'),
            'company': offer.get('company_name'),
            'date': datetime.strptime(offer.get('published'), '%a, %d %b %Y %H:%M:%S %Z').strftime('%d-%m-%Y'),
            'link': offer.get('link'),
            'industry':offer.get('industry')
        }
    for offer in offers]


def check_if_ngo_offer_is_valid(entry):
    # Not valid if older than TIMELIMIT
    now = datetime.timestamp(datetime.now(timezone.utc))
    parsed_date = entry.get('published', 'Thu, 24 Jan 1991 03:00:00 +0000')
    entry_date = datetime.strptime(parsed_date, '%a, %d %b %Y %H:%M:%S %z').timestamp()

    if now - entry_date > TIMELIMIT:
        return False
    return True


def get_ngo_offers():
    
    rss = feedparser.parse('https://ngojobsinafrica.com/media-rss/?country=kenya')
    entries = rss.entries

    offers = [e for e in entries if check_if_ngo_offer_is_valid(e) is True]

    return [
        {
            'title': offer.get('title'),
            #'company': offer.get('job:company'),
            'date': datetime.strptime(offer.get('published'), '%a, %d %b %Y %H:%M:%S %z').strftime('%d-%m-%Y'),
            'link': offer.get('link')
        }
    for offer in offers]
    


def main():
    myjobmag = get_myjobmag_offers()
    ngojobsinafrica = get_ngo_offers()
    

    raw_offers = ngojobsinafrica  + myjobmag  # Combine both sources

    offers = []
    for offer in raw_offers:
        offers.append(
            f'Role: {offer.get("title")} \n'
            f'Industry: {offer.get("industry")} \n'
            #f'Company: {offer.get("company")} \n'
            f'Date Posted: {offer.get("date")} \n'
            f'Link: {offer.get("link")} \n'
            
        )
    
    # Get the hashtag from a file
    with open('hashtag.txt', 'r') as f:
        hashtag = f.readlines()

    # Remove the newline character
    hashtag = [x.strip() for x in hashtag]

  
    # Get the API
    api = get_api()

    # Post the itens from the list
    for offer in offers:
        # Post the tweet
        api.update_status(offer + ' '+ hashtag[0] + ' ' + hashtag[1])
        # Sleep for a random time between 1 and 5 minutes
        print('Sleeping for a random time between 1 and 5 minutes')
        time.sleep(random.randint(60, 250))
    print('Done')


if __name__ == '__main__':
    main()
