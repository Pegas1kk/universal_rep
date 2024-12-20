class MediaFile:

    def __init__(self, name, size, date, owner, storage_location):
        self.name = name
        self.size = size
        self.date = date
        self.owner = owner
        self.storage_location = storage_location

    def __str__(self):
        return f"MediaFile(name='{self.name}', size={self.size} bytes, date={self.date}, owner='{self.owner}')"

    def update_metadata(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def delete(self):
        self.storage_location.delete(self)


class AudioFile(MediaFile):

    def __init__(self, name, size, date, owner, storage_location, duration, bitrate):
        super().__init__(name, size, date, owner, storage_location)
        self.duration = duration
        self.bitrate = bitrate

    def convert_to_mp3(self):
        pass


class VideoFile(MediaFile):

    def __init__(self, name, size, date, owner, storage_location, resolution, framerate):
        super().__init__(name, size, date, owner, storage_location)
        self.resolution = resolution
        self.framerate = framerate

    def crop(self, count):
        pass


class ImageFile(MediaFile):  # Исправлено имя класса

    def __init__(self, name, size, date, owner, storage_location, width, height):
        super().__init__(name, size, date, owner, storage_location)
        self.width = width
        self.height = height

    def resize(self, width, height):
        pass


class StorageLocation:

    def save(self, media_file):
        pass

    def delete(self, media_file):
        pass


class LocalStorage(StorageLocation):

    def save(self, media_file):
        pass

    def delete(self, media_file):
        pass


class CloudStorage(StorageLocation):

    def __init__(self, folder):
        self.folder = folder

    def save(self, media_file):
        pass

    def delete(self, media_file):
        pass

local_storage = LocalStorage()
cloud_storage = CloudStorage("folder Name")

audio = AudioFile("audiofile", 1024 * 1024, '17.12.69', "god", local_storage, 240, 128)
video = VideoFile("videofile", 1024 * 1024 * 10, '17.12.))', "angel1", cloud_storage, "1920x1080", 240)

print(audio)
print(video)
