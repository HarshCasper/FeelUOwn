from enum import IntFlags


class ModelFlags(IntFlags):
    get = 0x00000001
    """Model implements get classmethod

    def get(cls, identifier: str) -> model
    """

    batch = 0x00000002
    """Model implements list method"""

    # Reader
    songs_g = 0x00000010
    albums_g = 0x00000020
    artists_g = 0x00000040
    playlist_g = 0x00000080

    multi_quality = 0x0001000

    #: SongModel implements :meth:`.models.SongModel.list_similar_songs`
    similar_song = 0x00002000

    # TODO: maybe we should create a Model called MutableListModel
    #   to handle add/remove
    #
    # allow_fav_songs_add = False
    # allow_fav_songs_remove = False
    # allow_fav_playlists_add = False
    # allow_fav_playlists_remove = False
    # allow_fav_albums_add = False
    # allow_fav_albums_remove = False
    # allow_fav_artists_add = False
    # allow_fav_artists_remove = False
