class Song:
    def __init__(self, artist, album, title):
        self.artist = artist
        self.album = album
        self.title = title


class MusicAccessException(Exception):
    def __init__(self, message):
        super(Exception).__init__(self, message)
