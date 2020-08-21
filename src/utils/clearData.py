import os
import json
from langdetect import detect as lg_detect
from langdetect import detect_langs
from langdetect import DetectorFactory
from ..utils.jsonCompact import compact as json_comptact
import shutil
import sys 


delete = list()
DetectorFactory.seed = 0

#get all subfolders form directory
def getSubfolders(dir):
    subfolders = list()
    for subfolder in os.listdir(dir):
        subfolders.append(subfolder)
    return subfolders

#only used in filter
def onlyJson(mus):
    if mus.split('.')[1] == 'json':
        return True
    else:
        return False


def appendTXT(mus_name):
    return mus_name.split('.')[0] + '.txt'


def verifyLanguage(mus_name, dir, compact_mus, *args):
    lang = lg_detect(compact_mus.lower())
    if lang != 'pt':
        print(*args, mus_name," is going to be moved.")
        # print(compact_mus)
        # print(lang)
        # print(detect_langs(compact_mus))
        delete.append(os.path.join(dir,mus_name))
        # op = input('Are you sure you wnat to remove?')
        # if op in ('s', 'sim', 'y', 'yes', 'ye', 'si'):
        #     delete.append(os.path.join(dir,mus_name))
        #     # delete.append(os.path.join(dir,appendTXT(mus_name)))
        # else:
        #     return


def openJSON(file, artDir, *args):
    with open(file, encoding='utf8') as json_file:
        data = json.load(json_file)
        compact_mus = json_comptact(data['Lyrics'][0])
        verifyLanguage(file, artDir, compact_mus, args)


def deleteFiles():
    for file in delete:
        print('Removing ', file)
        os.remove(file)
        delete.remove(file)


def moveFiles(mus, gen, art):
    for file in delete:
        print('Moving ', file)
        foreignDir = os.path.join(getScriptDir(), 'Foreign')
        genDir = os.path.join(foreignDir, gen)
        if not os.path.isdir(genDir):
            os.makedirs(genDir)
        artDir = os.path.join(genDir, art)
        if not os.path.isdir(artDir):
            os.makedirs(artDir)
        os.rename(file, os.path.join(artDir, mus))
        delete.remove(file)


def getScriptDir():
    return sys.path[0]

def verifyForeign(gen):
    foreignDir = os.path.join(getScriptDir(), 'Foreign')
    genDir = os.path.join(foreignDir, gen)
    if os.path.isdir(genDir):
        return False
    return True

def clearData():
    print('Searching foreign music...')
    #get Gêneros path
    dir = os.path.join(os.getcwd(),'Generos')

    #get all subfolders of Gênero folder
    genders = getSubfolders(dir)

    #for each subfolder
    for gen in genders:
        if verifyForeign(gen):
            #get all artist folders
            genDir = os.path.join(dir, gen)
            arts = getSubfolders(genDir)

            #get all musics from artist folder
            for art in arts:
                artDir = os.path.join(genDir, art)
                mus = os.listdir(artDir)
                #filter only json songs
                # mus_aux = filter(onlyJson, mus)
                # for m in mus_aux:
                for m in mus:
                    os.chdir(artDir)
                    try:
                        openJSON(m, artDir, (gen, art))
                        # deleteFiles()
                        moveFiles(m, gen, art)
                    except Exception as e:
                        print(e)
                        awnser = input(f'Exception on song: {m}. Do you want do continue?')
                        if awnser not in ('yes', 'y', 'ye', 's', 'sim', 'ok', ''):
                            exit()
                