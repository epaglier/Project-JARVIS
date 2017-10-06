import music_player
import gmusic_accessor
import sys

# asemwejmxreddaqg

if gmusic_accessor.authenticate('martin.tuskevicius@gmail.com', 'asemwejmxreddaqg'):
    print ('Authenticated.')
else:
    print ('Failed to authenticate.')

song_list = gmusic_accessor.retrieve_song_list()
song_matches = music_player.find_songs_by_name(song_list, sys.argv[1])
for song in song_matches: print (song.to_string())

song_stream = gmusic_accessor.get_song_stream(song_list[0])
print (song_stream)
