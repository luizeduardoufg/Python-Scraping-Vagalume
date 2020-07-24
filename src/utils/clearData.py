import os
import json
from ..utils.languageDetc import lg_detect
from ..utils.jsonCompact import compact as json_comptact

#get all subfolders form directory
def getSubfolders(dir):
    subfolders = list()
    for subfolder in os.listdir(dir):
        subfolders.append(subfolder)
    return subfolders

def onlyJson(mus):
    if mus.split('.')[1] == 'json':
        return True
    else:
        return False

def clearData():
    #get Gêneros path
    dir = os.path.join(os.getcwd(),'Gêneros')

    #get all subfolders of Gênero folder
    genrers = getSubfolders(dir)

    #for each subfolder
    for gen in genrers:
        #get all artist folders
        genDir = os.path.join(dir, gen)
        arts = getSubfolders(genDir)

        #get all musics from artist folder
        for art in arts:
            artDir = os.path.join(genDir, art)
            mus = os.listdir(artDir)
            #filter only json songs
            mus_aux = filter(onlyJson, mus)
            for m in mus_aux:
                # print(m)
                # print(gen, art, m)
                os.chdir(artDir)
                try:
                    with open(m, encoding='utf8') as json_file:
                        data = json.load(json_file)
                        compact_mus = json_comptact(data['Lyrics'][0])
                        # print(compact_mus)
                        if lg_detect(compact_mus) != 'pt':
                            print(gen, art, m)
                except Exception as e:
                    print(e)
