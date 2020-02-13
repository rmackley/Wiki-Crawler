from bs4 import BeautifulSoup
import requests
import random
import re
import argparse

def fetch_webpage(fetch_url):
    r = requests.get(fetch_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_random_link(soup):
    #TODO:
        #find links from tables:
        # print(soup.select("table.wikitable td a" ))

    #If using front page, select from featured article section
    if soup == "https://en.wikipedia.org/wiki/Main_Page":
        links = soup.select('#mp-tfa p a[href]')
    else:
        links = [tag['href'] for tag in soup.select('p a[href]') if re.search(r"^/wiki", tag['href'])]
    rand = random.randint(0, len(links)-1)
    link = links[rand]
    next_link = "https://en.wikipedia.org" + link
    return next_link

def get_arguments():
    parser = argparse.ArgumentParser(description="Go down the Wiki rabbit hole.")
    parser.add_argument('rounds', type=int, help="How many links would you like to see")
    parser.add_argument('--url', type=str, default="https://en.wikipedia.org/wiki/Main_Page", help="Link to starting page. Needs to be the whole URL")
    args = parser.parse_args()
    return args

def crawler():
    input = get_arguments()
    rounds = input.rounds
    start_link = input.url

    print("Start loop: ")
    for i in range(0, rounds):
        print("Round: ", i)
        s = fetch_webpage(start_link)
        start_link = get_random_link(s)
        print(start_link)

crawler()
