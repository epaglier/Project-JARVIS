import music_player
import gmusic_accessor
import sys

# asemwejmxreddaqg

print(gmusic_accessor.authenticate('martin.tuskevicius@gmail.com', 'asemwejmxreddaqg'))

song_list = gmusic_accessor.retrieve_song_list()
song_matches = music_player.find_songs_by_name(song_list, sys.argv[1])
for song in song_matches: print (song.to_string())
