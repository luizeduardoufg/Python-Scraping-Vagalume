import requests
import unidecode
import alphanumeric

#Fetch all lyrics from artist
def fetchSongs(art):
    r =requests.get('https://www.vagalume.com.br/' + art + '/index.js')
    songs = list()
    for song in r.json()['artist']['lyrics']['item']:
        songs.append(alphanumeric.alphanumeric(unidecode.unidecode(song['desc'].lower())))
    return songs