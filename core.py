from ytmusicapi import YTMusic


class YtEngine:
    def __init__(self, headers_path='headers_auth.json'):
        self.yt = YTMusic(headers_path)

    def export_likes(self, ignore_existing=False, playlist_name='eLikes'):
        """
        Get user's Liked Songs-playlist and export all songs from it into a user-created playlist.

        :param ignore_existing: Ignore existing export playlist and create new one.
        :param playlist_name: Name of the export playlist.
        :return:
        """
        export_playlist = [playlist.get("playlistId") for playlist in self.yt.get_library_playlists()
                           if playlist.get("title") == playlist_name]
        if len(export_playlist) > 0:
            export_playlist = self.yt.get_playlist(export_playlist[0])
            export_songs = self.yt.get_playlist(export_playlist['id'], limit=export_playlist['trackCount'])
            self.yt.remove_playlist_items(export_playlist['id'], export_songs['tracks'])
        else:
            export_playlist = self.yt.get_playlist(self.yt.create_playlist('eLikes',
                                                   'This playlist contains all of the liked songs. You can share this'
                                                   ' playlist with your friends (unlike standard likes'
                                                   ' playlist)!'))

        likes_playlist = self.yt.get_playlist('LM')
        liked_songs = self.yt.get_playlist("LM", limit=likes_playlist['trackCount'])
        self.yt.add_playlist_items(export_playlist['id'], [track['videoId']
                                                           for track in liked_songs['tracks']])
