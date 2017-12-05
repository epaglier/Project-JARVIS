import gmusicapi
from .music_accessor import MusicService, MusicException
import vlc
import random

_api = gmusicapi.Mobileclient()


class GoogleMusicAccessor(MusicService):
    current_player = None

    def __init__(self, username, password):
        if not _api.login(username, password, gmusicapi.Mobileclient.FROM_MAC_ADDRESS):
            raise MusicException("Google Music authentication failed.")

    def __new_player__(self, player):
        if self.current_player is not None:
            self.current_player.stop()
            self.current_player.release()
        self.current_player = player
        self.current_player.play()

    def __play_tracks__(self, tracks, track_id_key="storeId"):
        player_instance = vlc.Instance()
        track_queue = player_instance.media_list_new()
        for track in tracks:
            track_queue.add_media(_api.get_stream_url(track[track_id_key]))
        track_player = player_instance.media_list_player_new()
        track_player.set_media_list(track_queue)
        self.__new_player__(track_player)

    def play_song(self, song_name, artist_name=""):
        try:
            song = _api.search(song_name)["song_hits"][0]["track"]
        except IndexError:
            raise MusicException("Song not found.")
        self.__new_player__(vlc.MediaPlayer(_api.get_stream_url(song["storeId"])))

    def play_artist(self, artist_name):
        try:
            artist = _api.search(artist_name)["artist_hits"][0]["artist"]
        except IndexError:
            raise MusicException("Artist not found.")
        artist_tracks = _api.get_artist_info(
            artist["artistId"],
            include_albums=False,
            max_top_tracks=10,
            max_rel_artist=0)["topTracks"]
        self.__play_tracks__(artist_tracks)

    def play_album(self, album_name, artist_name="", shuffle=False):
        try:
            album = _api.search(album_name + " by " + artist_name)["album_hits"][0]["album"]
        except IndexError:
            raise MusicException("Album not found.")
        album_tracks = _api.get_album_info(album["albumId"])["tracks"]
        if shuffle:
            random.shuffle(album_tracks)
        self.__play_tracks__(album_tracks)

    def play_playlist(self, playlist_name, shuffle=False):
        try:
            playlist = _api.search(playlist_name)["playlist_hits"][0]["playlist"]
        except IndexError:
            raise MusicException("Playlist not found.")
        playlist_tracks = _api.get_shared_playlist_contents(playlist["shareToken"])[:10]
        if shuffle:
            random.shuffle(playlist_tracks)
        self.__play_tracks__(playlist_tracks, "trackId")

    def pause_music(self):
        if self.current_player is not None:
            self.current_player.pause()

    def resume_music(self):
        if self.current_player is not None:
            self.current_player.play()

    def stop_music(self):
        if self.current_player is not None:
            self.current_player.stop()
