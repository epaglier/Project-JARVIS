import sys
import gmusic_accessor
import music_player

from music_player import MusicAccessException

test_arguments = sys.argv[1:]
argument_count = len(test_arguments)

if argument_count < 2:
    raise Exception('Expected arguments: <Username> <Password> [<Title Substring>]')

if gmusic_accessor.authenticate(test_arguments[0], test_arguments[1]):
    print('Authenticated.')
else:
    raise MusicAccessException('Failed to authenticate.')

song_list = gmusic_accessor.retrieve_song_list()

if argument_count == 2:
    print(map(lambda song: song.to_string(), song_list))
else:
    first_song = music_player.find_songs_by_name(song_list, test_arguments[2])[0]
    print('Playing ' + first_song.to_string() + ' ...')
    music_player.create_player(gmusic_accessor.get_song_stream(first_song))
