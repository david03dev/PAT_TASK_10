class Song:
    def __init__(self, title="song1", genre="random", url="defautl_url"):
        self.title = title
        self.genre = genre
        self.url = url

    def __str__(self):
        return f"Title: {self.title}, Genre: {self.genre}, URL: {self.url}"


class Playlist:
    def __init__(self, genre="playlist"):
        self.genre = genre
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added song: {song.title}")

    def remove_song(self, title):
        for song in self.songs:
            if song.title == title:
                self.songs.remove(song)
                print(f"Removed song: {title}")
                return
        print(f"Song with title '{title}' not found.")

    def list_songs(self):
        print(f"Playlist Genre: {self.genre}")
        for song in self.songs:
            print(song)

    def search_song(self, title):
        for song in self.songs:
            if song.title == title:
                print(f"Found song: {song}")
                return
        print(f"Song with title '{title}' not found.")


class MusicPlayer:
    def __init__(self):
        self.playlists = {}
        self.current_song = None
        self.is_playing = False
        self.initialize_default_playlist()

    def initialize_default_playlist(self):
        # Create a default playlist and add a default song
        default_playlist = Playlist("default")
        default_song = Song(title="song1", genre="random")
        default_playlist.add_song(default_song)
        self.playlists["default"] = default_playlist

    def create_playlist(self, genre="playlist"):
        if genre not in self.playlists:
            self.playlists[genre] = Playlist(genre)
            print(f"Created playlist for genre: {genre}")
        else:
            print(f"Playlist for genre '{genre}' already exists.")

    def add_song_to_playlist(self, genre, title="song1", song_genre="random", url=""):
        if genre in self.playlists:
            song = Song(title, song_genre, url)
            self.playlists[genre].add_song(song)
        else:
            print(f"Playlist for genre '{genre}' does not exist.")

    def remove_song_from_playlist(self, genre, title="song1"):
        if genre in self.playlists:
            self.playlists[genre].remove_song(title)
        else:
            print(f"Playlist for genre '{genre}' does not exist.")

    def list_playlists(self):
        if not self.playlists:
            print("No playlists available.")
            return
        for genre, playlist in self.playlists.items():
            print(f"Genre: {genre}")
            playlist.list_songs()

    def search_song(self, title="song1"):
        found = False
        for playlist in self.playlists.values():
            playlist.search_song(title)
            found = True
        if not found:
            print(f"Song with title '{title}' not found in any playlist.")

    def play_song(self, title="song1"):
        for playlist in self.playlists.values():
            for song in playlist.songs:
                if song.title == title:
                    self.current_song = song
                    self.is_playing = True
                    print(f"Playing: {song}")
                    return
        print(f"Song with title '{title}' not found.")

    def pause(self):
        if self.is_playing:
            self.is_playing = False
            print("Paused.")
        else:
            print("No song is currently playing.")

    def fast_forward(self):
        if self.is_playing:
            print("Fast forwarded.")
        else:
            print("No song is currently playing.")

    def back_forward(self):
        if self.is_playing:
            print("Back to previous position.")
        else:
            print("No song is currently playing.")

    def show_options(self):
        print("\nOptions:")
        print("1. Create Playlist")
        print("2. Add Song to Playlist")
        print("3. Remove Song from Playlist")
        print("4. List Playlists")
        print("5. Search Song")
        print("6. Play Song")
        print("7. Pause")
        print("8. Fast Forward")
        print("9. Back Forward")
        print("10. Exit")


def main():
    player = MusicPlayer()
    while True:
        player.show_options()
        choice = input("Enter your choice: ")

        if choice == '1':
            genre = input("Enter genre for the new playlist (default 'playlist'): ") or "playlist"
            player.create_playlist(genre)
        elif choice == '2':
            genre = input("Enter genre of the playlist: ")
            title = input("Enter song title (default 'song1'): ") or "song1"
            song_genre = input("Enter song genre (default 'random'): ") or "random"
            url = input("Enter song URL: ")
            player.add_song_to_playlist(genre, title, song_genre, url)
        elif choice == '3':
            genre = input("Enter genre of the playlist: ")
            title = input("Enter song title to remove (default 'song1'): ") or "song1"
            player.remove_song_from_playlist(genre, title)
        elif choice == '4':
            player.list_playlists()
        elif choice == '5':
            title = input("Enter song title to search (default 'song1'): ") or "song1"
            player.search_song(title)
        elif choice == '6':
            title = input("Enter song title to play (default 'song1'): ") or "song1"
            player.play_song(title)
        elif choice == '7':
            player.pause()
        elif choice == '8':
            player.fast_forward()
        elif choice == '9':
            player.back_forward()
        elif choice == '10':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
