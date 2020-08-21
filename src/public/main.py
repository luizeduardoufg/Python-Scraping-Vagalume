from ..utils.writeFile import writeSongs
from ..utils.fetchArt import fetchArt
from ..utils.fetchSongs import fetchSongs
from ..utils.clearData import clearData, getScriptDir
from  ..utils.quantityAnalysis import *

def getSongs(gens = []):
    if not gens:
        print('Empty list')
        return
    for gen in gens:
        print(f'Gender: {gen}')
        arts = fetchArt(gen)
        for art in arts:
            print(f'Artist: {art}')
            try:
                songs = fetchSongs(art)
                writeSongs(art, songs, gen)
            except:
                print(f'Artist {art} is wrong.')

if __name__ == '__main__':
    # gens = ['axe', 'bossa-nova', 'forro', 'funk', 
    #         'funk-carioca', 'gospel', 'mpb', 'pagode', 
    #         'rap', 'samba', 'sertanejo']
    # getSongs(['funk-carioca'])
    # clearData()
    # print('Words per artist: ', averageWordsPerArt())
    # print('Words per gender: ', averageWordsPerGen())
    # print('Words global: ', averageWordsGlobal())   
    # print('Letters per artist: ', averageLettersPerArt())
    # print('Letters per gender: ', averageLettersPerGen())
    # print('Letters global: ', averageLettersGlobal())     
    
    