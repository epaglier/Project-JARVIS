class Song:
    def __init__(self, artist, album, title):
        self.artist = artist
        self.album = album
        self.title = title

    def to_string(self):
        return self.artist + ': ' + self.title + ' [' + self.album + ']'


class MusicAccessException(Exception):
    def __init__(self, message):
        super(Exception).__init__(self, message)


def find_songs_by_name(song_list, title_substring):
    title_substring = title_substring.lower()
    matches = []
    for song in song_list:
        if title_substring in song.title.lower():
            matches.append(song)
    return matches
