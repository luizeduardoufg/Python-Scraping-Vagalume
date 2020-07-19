import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json
import ast
from urllib.request import Request, urlopen
import os

def writeJSON(path, song):
    with open(path, 'w', encoding='utf8') as outfile: 
        json.dump(song, outfile, indent = 4, ensure_ascii = False)

def writeTXT(path, song):
    with open(path, 'w', encoding='utf8') as outfile: 
        json.dump(song, outfile, indent = 4, ensure_ascii = False)

def writeSongs(art, songs, gen):
    # For ignoring SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    for song in songs:
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

            #Save the json created with the file name as title + .json (same for txt)
            #Path of the json file inside Generos\nome-do-genero\nome-do-artista\nome-da-musica.json
            json_path = os.path.join(os.getcwd(), f"Gêneros\\{gen}\\{art}\\{song}.json")

            #Path of the json file inside Generos\nome-do-genero\nome-do-artista\nome-da-musica.txt
            txt_path = os.path.join(os.getcwd(), f"Gêneros\\{gen}\\{art}\\{song}.txt")

            #Path of the artist folder inside Generos\nome-do-genero
            art_path = os.path.join(os.getcwd(), f"Gêneros\\{gen}\\{art}")

            #Boolean to verify if already exists a dir with the artist name
            art_dir = os.path.isdir(art_path)

            if art_dir:
                writeJSON(json_path, song_json)
                writeTXT(txt_path, song_json)
            else:
                os.makedirs(art_path)
                writeJSON(json_path, song_json)
                writeTXT(txt_path, song_json)

            print("Writing song file: " + song)
        except:
            print('Song \'' + song + ' \' is wrong.')

    print('———-Extraction of data is complete. Check json and txt files.———-')