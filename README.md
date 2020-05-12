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



MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
