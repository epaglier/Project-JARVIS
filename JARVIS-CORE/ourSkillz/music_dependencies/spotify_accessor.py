import spotify
import threading
import random
from .music_accessor import MusicService, MusicException

session = spotify.Session()
_login_event = threading.Event()
_track_queue = []

spotify.AlsaSink(session)
spotify.EventLoop(session).start()


def __login_listener__(session, error_type):
    _login_event.set()
    if error_type is not spotify.ErrorType.OK:
        raise MusicException("Spotify authentication failed.")


def __end_of_track_listener__(session):
    session.player.unload()
    __play_next_track__()


session.on(spotify.SessionEvent.LOGGED_IN, __login_listener__)
session.on(spotify.SessionEvent.END_OF_TRACK, __end_of_track_listener__)


def __search__(filters):
    search_result = session.search(' '.join(filters))
    search_result.load()
    return search_result


def __queue_tracks__(tracks, shuffle):
    del _track_queue[:]
    if shuffle:
        tracks = list(tracks)
        random.shuffle(tracks)
    for track in tracks:
        _track_queue.append(track)


def __play_next_track__():
    if len(_track_queue) >= 1:
        session.player.load(session.get_track(_track_queue.pop(0).load().link.uri).load())
        session.player.play()


class SpotifyAccessor(MusicService):

    def __init__(self, username, password):
        session.login(username, password)
        if not _login_event.wait(30):
            raise MusicException("Spotify authentication timed out.")

    def play_song(self, song_name, artist_name=""):
        search_filters = ["track:" + song_name]
        if artist_name != "":
            search_filters.append("artist:" + artist_name)
        try:
            __queue_tracks__([__search__(search_filters).tracks[0]], False)
        except IndexError:
            raise MusicException("Song not found.")
        __play_next_track__()

    def play_artist(self, artist_name):
        try:
            artist = __search__(["artist:" + artist_name]).artists[0]
        except IndexError:
            raise MusicException("Artist not found.")
        artist_browser = artist.browse()
        artist_browser.load()
        __queue_tracks__(artist_browser.tracks, False)
        __play_next_track__()

    def play_album(self, album_name, artist_name="", shuffle=False):
        search_filters = ["album:" + album_name]
        if artist_name != "":
            search_filters.append("artist:" + artist_name)
        try:
            album = __search__(search_filters).albums[0]
        except IndexError:
            raise MusicException("Album not found.")
        album_browser = album.browse()
        album_browser.load()
        __queue_tracks__(album_browser.tracks, shuffle)
        __play_next_track__()

    def play_playlist(self, playlist_name, shuffle=False):
        try:
            playlist = __search__(["playlist:" + playlist_name]).playlists[0].playlist
            playlist.load(45)
        except IndexError:
            raise MusicException("Playlist not found.")
        except spotify.Timeout:
            raise MusicException("Playlist search timed out.")
        __queue_tracks__(playlist.tracks, shuffle)
        __play_next_track__()

    def pause_music(self):
        session.player.pause()

    def resume_music(self):
        session.player.play(True)

    def stop_music(self):
        session.player.unload()
