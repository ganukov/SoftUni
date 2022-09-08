from Object_oriented_programming.Classes_and_Objects.Classes_and_Objects_exercise.spootify.song import Song


class Album:
    def __init__(self, name, *args):
        self.name = name

        self.published = False
        self.songs = []
        for x in args:
            self.songs.append(x)

    def add_song(self, song: Song):
        if self.published is True:
            return "Cannot add songs. Album is published."
        elif song in self.songs:
            return "Song is already in the album."
        elif song.single is True:
            return f"Cannot add {song.name}. It's a single"
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    @staticmethod
    def find_by_name(name, songs):
        for song in songs:
            if song.name == name:
                return song
        return None

    def remove_song(self, song_name):
        song = self.find_by_name(song_name, self.songs)
        if song is None:
            return "Song is not in the album."
        elif self.published is True:
            return "Cannot remove songs. Album is published."
        self.songs.remove(song)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published is True:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f'Album {self.name}\n'
        for song in self.songs:
            result += f'== {song.get_info()}\n'
        return result
