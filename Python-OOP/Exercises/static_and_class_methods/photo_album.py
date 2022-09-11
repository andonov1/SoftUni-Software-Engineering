from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__init_photos(pages)

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / cls.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label):
        for idx, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.PHOTOS_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {idx + 1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        delimiter = 11 * '-'
        content = '[]'
        result = delimiter
        for page in self.photos:
            result += f'\n{" ".join([content for photo in page])}\n{delimiter}'
        return result

    @staticmethod
    def __init_photos(pages):
        result = []
        for _ in range(pages):
            result.append([])
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
