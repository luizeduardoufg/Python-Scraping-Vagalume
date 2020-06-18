import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json
import ast
import os
from urllib.request import Request, urlopen
from fetchSongs import fetchSongs
import os


gen = "Axé"
art = 'alexandre-thai'
songs = fetchSongs(art)
print(songs)

# For ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for song in songs:

    # url
    url =  'https://www.vagalume.com.br/' + art + '/' + song + '.html'

    try:
        # Making the website believe that you are accessing it using a mozilla browser
        req = Request(url, headers = { 'User-Agent' : 'Mozilla/5.0' })
        webpage = urlopen(req).read()

        # Creating a BeautifulSoup object of the html page for easy extraction of data.
        soup = BeautifulSoup(webpage, 'html.parser')
        html = soup.prettify('utf-8')
        song_json = {}
        song_json["Lyrics"] = []

        #Extract Title of the song
        for title in soup.findAll('title'):
            song_json["Title"] = title.text.strip()

        #Extract the Lyrics of the song
        for div in soup.findAll('div', attrs = {'id': 'lyrics'}):
            song_json["Lyrics"].append(div.get_text(separator='\n').strip().split("\n"))

        #Save the json created with the file name as title + .json
        if os.path.isdir(os.path.join(os.getcwd(), f"Gêneros\\{gen}\\{art}")):
            with open(os.path.join(os.getcwd(), f"Gêneros\\{gen}\\{art}\\{song}.json"), 'w', encoding='utf8') as outfile: 
                json.dump(song_json, outfile, indent = 4, ensure_ascii = False)
        else:
            os.makedirs(os.path.join(os.getcwd(), f"Gêneros\\{gen}\\{art}"))
            with open(os.path.join(os.getcwd(), f"Gêneros\\{gen}\\{art}\\{song}.json"), 'w', encoding='utf8') as outfile: 
                json.dump(song_json, outfile, indent = 4, ensure_ascii = False)
    except:
        print('Song \'' + song + ' \' is wrong.')

print('———-Extraction of data is complete. Check json file.———-')
