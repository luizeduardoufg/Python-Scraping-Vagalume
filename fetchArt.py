import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json
import ast
import os
from urllib.request import Request, urlopen
import alphanumeric
import unidecode

def fetchArt(gen):
    art = list()
    # For ignoring SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url  = 'https://www.vagalume.com.br/browse/style/' + gen + '.html'
    # Making the website believe that you are accessing it using a mozilla browser
    req = Request(url, headers = { 'User-Agent' : 'Mozilla/5.0' })
    webpage = urlopen(req).read()

    # Creating a BeautifulSoup object of the html page for easy extraction of data.
    soup = BeautifulSoup(webpage, 'html.parser')
    html = soup.prettify('utf-8')

    #Extract the Lyrics of the song
    for div in soup.findAll('div', attrs = {'class': 'moreNamesContainer'}):
       art.append(div.get_text(separator='\n').strip().split('\n'))

    arts = list()
    for a in art[0]:
        arts.append(alphanumeric.alphanumeric(unidecode.unidecode(a)).lower())
    
    return arts