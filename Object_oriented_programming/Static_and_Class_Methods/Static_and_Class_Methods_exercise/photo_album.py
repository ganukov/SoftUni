class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = []

        for _ in range(pages):
            self.photos.append(list())

    @classmethod
    def from_photos_count(cls, photos_count):
        if photos_count <= 4:
            return cls

    def add_photo(self, label):
        for page in range(len(self.photos)):
            if label not in self.photos[page] and len(self.photos[page]) != 4:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page" \
                       f" {page + 1} slot {self.photos[page].index(label) + 1}"
        for each in self.photos:
            if len(each) == 4:
                return "No more free slots"

    def display(self):
        result = "-----------"
        for i in self.photos:
            for y in i:
                y = '[]'
            result += f"\n{' '.join(['[]' for each in i])}\n-----------"
        return result


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())
