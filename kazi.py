import feedparser, pprint,requests, datetime, time, json, os, sys, time
from datetime import datetime, timezone, timedelta, date
from time import gmtime

TIMELIMIT = 90000 # Around 25 hours


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
            'company': offer.get('company'),
            'date': datetime.strptime(offer.get('published'), '%a, %d %b %Y %H:%M:%S %z').strftime('%d-%m-%Y'),
            'link': offer.get('link')
        }
    for offer in offers]


def main():
    myjobmag = get_myjobmag_offers()
    ngojobsinafrica = get_ngo_offers()
    

    raw_offers = myjobmag + ngojobsinafrica 

    offers = []
    for offer in raw_offers:
        offers.append(
            f'Role: *{offer.get("title")}* \n'
            f'Company: {offer.get("company")} \n'
            f'Date: {offer.get("date")} \n'
            f'Link: {offer.get("link")} \n'
            
        )

    return offers
     
print (main())
