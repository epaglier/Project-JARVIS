from .music_dependencies.gmusic_accessor import GoogleMusicAccessor
from .music_dependencies.spotify_accessor import SpotifyAccessor
from .music_dependencies.music_accessor import MusicException

_google_music = GoogleMusicAccessor("martin.tuskevicius@gmail.com", "fucaqwkieydzkiac")
_spotify = SpotifyAccessor("projectjarvisburner@gmail.com", "HelloWorld")
_current_service = _google_music
_music_targets = ["song", "track", "album", "artist", "playlist"]
_music_vocabulary = _music_targets + ["play", "stop", "pause", "resume", "shuffle", "by", "music", "spotify", "google"]


def __lowercase_words__(voice_words):
    return [word.lower() for word in voice_words]


def respond(voice_words):
    voice_words = __lowercase_words__(voice_words)
    match_strength = 0
    for word in voice_words:
        if word == "music":
            match_strength += 2
        elif word in _music_vocabulary:
            match_strength += 1
    return match_strength


def handle_input(voice_string):
    global _current_service
    voice_words = __lowercase_words__(voice_string.split(" "))
    word_count = len(voice_words)
    if word_count >= 1:
        first_word = voice_words[0]
        try:
            if first_word == "play" or first_word == "stream":
                music_target = None
                shuffle = False
                artist_specified = False
                artist_words = []
                query_words = []
                for word in voice_words[1:]:
                    if word == "artist":
                        music_target = "artist"
                        artist_specified = True
                    elif word in _music_targets:
                        music_target = word
                    elif word == "spotify":
                        if _current_service != _spotify:
                            _current_service.stop_music()
                            _current_service = _spotify
                    elif word == "google":
                        if _current_service != _google_music:
                            _current_service.stop_music()
                            _current_service = _google_music
                    elif word == "shuffle":
                        shuffle = True
                    elif word == "by":
                        artist_specified = True
                    elif artist_specified:
                        artist_words.append(word)
                    else:
                        query_words.append(word)
                query = " ".join(query_words)
                artist = " ".join(artist_words)
                if music_target == "album":
                    _current_service.play_album(query, artist, shuffle)
                elif music_target == "artist":
                    _current_service.play_artist(artist)
                elif music_target == "playlist":
                    _current_service.play_playlist(query, shuffle)
                else:
                    _current_service.play_song(query, artist)
            elif first_word == "stop":
                _current_service.stop_music()
            elif first_word == "pause":
                _current_service.pause_music()
            elif first_word == "resume":
                _current_service.resume_music()
        except MusicException, e:
            return e.parameter
    return ""
