from Object_oriented_programming.Classes_and_Objects.Classes_and_Objects_exercise.spootify.album import Album
from Object_oriented_programming.Classes_and_Objects.Classes_and_Objects_exercise.spootify.song import Song


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    @staticmethod
    def find_name(name, albums):
        for album in albums:
            if album.name == name:
                return album
        return None

    def remove_album(self, album_name):
        album = self.find_name(album_name, self.albums)
        if album is None:
            return f"Album {album_name} is not found."
        elif album.published is True:
            return f"Album has been published. It cannot be removed."
        self.albums.remove(album)
        return f"Album {album.name} has been removed."

    def details(self):
        result = f'Band {self.name}\n'

        for x in self.albums:
            result += x.details()

        return result


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
'Album The Sound of Perseverance has been published' != 'Album The Sound of Perseverance has been published.'