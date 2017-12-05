from abc import ABCMeta, abstractmethod


class MusicService(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def play_song(self, song_name, artist_name=""):
        pass

    @abstractmethod
    def play_artist(self, artist_name):
        pass

    @abstractmethod
    def play_album(self, album_name, artist_name="", shuffle=False):
        pass

    @abstractmethod
    def play_playlist(self, playlist_name, shuffle=False):
        pass

    @abstractmethod
    def pause_music(self):
        pass

    @abstractmethod
    def resume_music(self):
        pass

    @abstractmethod
    def stop_music(self):
        pass


class MusicException(Exception):

    def __init__(self, parameter):
        self.parameter = parameter
