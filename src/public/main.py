from ..utils.writeFile import writeSongs
from ..utils.fetchArt import fetchArt
from ..utils.fetchSongs import fetchSongs

if __name__ == '__main__':
    gens = ['samba', 'sertanejo']
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