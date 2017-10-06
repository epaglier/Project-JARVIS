from gmusicapi import Mobileclient

from music_player import MusicAccessException
from music_player import Song

api = Mobileclient()


class GoogleSong(Song):
    def __init__(self, artist, album, title, song_id):
        Song.__init__(self, artist, album, title)
        self.song_id = song_id


def authenticate(account, password):
    return api.login(account, password, Mobileclient.FROM_MAC_ADDRESS)


def retrieve_song_list():
    __check_authentication()
    music_library = api.get_all_songs()
    song_list = []
    for song_entry in music_library:
        song_list.append(GoogleSong(song_entry["artist"],
                                    song_entry["album"],
                                    song_entry["title"],
                                    song_entry["id"]))
    return song_list


def get_song_stream(song):
    __check_authentication()
    return api.get_stream_url(song.song_id)


def __check_authentication():
    if not api.is_authenticated():
        raise MusicAccessException('Please authenticate yourself first.')
