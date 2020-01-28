from bs4 import BeautifulSoup
import requests
import random
import re

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

def main():
    rounds = 13
    #Default to starting on main page of wikipedia
    start_link = "https://en.wikipedia.org/wiki/Main_Page"
    print("Start loop: ")
    for i in range(0, rounds):
        print("Round: ", i)
        s = fetch_webpage(start_link)
        start_link = get_random_link(s)
        print(start_link)


if __name__ == "__main__":
    main()
