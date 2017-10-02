from music import music_player
from gmusicapi import Mobileclient

from music.music_player import Song

api = Mobileclient()


class GoogleSong(Song):
    def __init__(self, artist, album, title, song_id):
        Song.__init__(self, artist, album, title)
        self.song_id = song_id


def authenticate(account, password):
    return api.login(account, password, Mobileclient.FROM_MAC_ADDRESS)


def retrieve_song_list():
    if not api.is_authenticated():
        raise music_player.MusicAccessException('Please authenticate yourself first.')
    music_library = api.get_all_songs()
    song_list = []
    for song_entry in music_library:
        song_list.append(GoogleSong(song_entry["artist"],
                                    song_entry["album"],
                                    song_entry["title"],
                                    song_entry["id"]))
    return song_list
