class MusicList():
    def __init__(self):
        self._musics = []

    def add(self, music):
        self._musics.append(music)
        
    def list_of_all_musics(self):
        return self._musics