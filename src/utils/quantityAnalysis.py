import os
import json
from ..utils.jsonCompact import compact as json_comptact
import re
import sys

numberArtists = 319
numberGenders = 3

def countWords(string):
    return len(re.findall(r'\w+', string))

def countLetters(string):
    return sum(c.isalpha() for c in string)

def openJSON(file, artDir, *args):
    try:
        with open(file, encoding='utf8') as json_file:
            data = json.load(json_file)
            compact_mus = json_comptact(data['Lyrics'][0])
            return compact_mus
    except:
        return ''

#get all subfolders form directory
def getSubfolders(dir):
    subfolders = list()
    for subfolder in os.listdir(dir):
        subfolders.append(subfolder)
    return subfolders


def accessArtFolder(text, logic, function):
    print(text)
    dir = os.path.join(os.getcwd(),'Generos')
    genders = getSubfolders(dir)
    average = 0
    for gen in genders:
        genDir = os.path.join(dir, gen)
        arts = getSubfolders(genDir)
        for art in arts:
            artDir = os.path.join(genDir, art)
            mus = os.listdir(artDir)
            for m in mus:
                os.chdir(artDir)
                average +=function(openJSON(m, artDir, (gen, art)))
    os.chdir(sys.path[0])
    if logic in 'numberArtists':
        return average / numberArtists
    if logic in 'numberGenders':
         return average / numberGenders
    if logic in 'global':
        return average


def averageWordsPerArt():
    return accessArtFolder('Calculating words per artist', 'numberArtists', countWords)

def averageWordsPerGen():
    return accessArtFolder('Calculating words per gender', 'numberGenders', countWords)

def averageWordsGlobal():
    return accessArtFolder('Calculating words global', 'global', countWords)

def averageLettersPerArt():
    return accessArtFolder('Calculating letters per artist', 'numberArtists', countLetters)

def averageLettersPerGen():
    return accessArtFolder('Calculating letters per gender', 'numberGenders', countLetters)

def averageLettersGlobal():
    return accessArtFolder('Calculating letters global', 'global', countLetters)