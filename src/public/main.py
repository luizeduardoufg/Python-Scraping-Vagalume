from ..utils.writeFile import writeSongs
from ..utils.fetchArt import fetchArt
from ..utils.fetchSongs import fetchSongs
from ..utils.clearData import clearData

def getSongs(gens = []):
    if not gens:
        print('Empty list')
        return
    for gen in gens:
        print(f'Genrer: {gen}')
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
    getSongs()
    clearData()
    