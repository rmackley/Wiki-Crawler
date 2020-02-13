# Wiki-Crawler

Very basic command line wiki crawler
- Takes number of rounds and optional english wiki page url from user and randomly selects links to follow
- Only works on English wiki pages

****
Possible features I'd like to add at some point
- web interface
- text snippets from each page selected

****
python wiki_crawler.py -h
usage: wiki_crawler.py [-h] [--url URL] rounds

Go down the Wiki rabbit hole.

positional arguments:
  rounds      How many links would you like to see

optional arguments:
  -h, --help  show this help message and exit
  --url URL   Link to starting page. Needs to be the whole URL
