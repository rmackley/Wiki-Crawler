# Wiki-Crawler

Very basic command line wiki crawler
- Start point defaults to the featured article on the english wikipedia homepage
- Takes number of rounds and optional english wiki page url as start point from user
- Only works on English wiki pages

****
python wiki_crawler.py -h
usage: wiki_crawler.py [-h] [--url URL] rounds

Go down the Wiki rabbit hole.

positional arguments:
  rounds      How many links would you like to see

optional arguments:
  -h, --help  show this help message and exit
  --url URL   Link to starting page. Needs to be the whole URL

****
Possible future features:
- text snippets from each page selected
- multi-language support
