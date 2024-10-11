class Song:
    def __init__(self, song_id, song_name, genre):
        self.song_id = song_id
        self.song_name = song_name
        self.genre = genre

class MusicService:
    def __init__(self):
        self.available_songs = []  
        self.queue = []            
        self.undo_stack = []     

    def add_song(self, song):
        self.available_songs.append(song)

    def play_song(self, song):
        self.queue.append(song)      
        self.undo_stack.append(song)  

    def undo_selection(self):
        if self.undo_stack:
            last_song = self.undo_stack.pop()  
            print(f"Undid selection of: {last_song.song_name}")
        else:
            print("No song to undo.")

    def next_song(self):
        if self.queue:
            current_song = self.queue.pop(0)  
            print(f"Now playing: {current_song.song_name} (Genre: {current_song.genre})")
        else:
            print("No more songs in the queue.")

    def show_available_songs(self):
        if self.available_songs:
            print(f"{'ID':<10} {'Song Name':<30} {'Genre':<20}")
            print("-" * 60)
            for song in self.available_songs:
                print(f"{song.song_id:<10} {song.song_name:<30} {song.genre:<20}")
        else:
            print("No available songs.")

def main():
    music_service = MusicService()

    while True:
        print("\nMenu:")
        print("1. Add Song")
        print("2. Play Song")
        print("3. Undo Selection")
        print("4. Next Song")
        print("5. Show Available Songs")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            song_id = input("Enter song ID: ")
            song_name = input("Enter song name: ")
            genre = input("Enter song genre: ")
            music_service.add_song(Song(song_id, song_name, genre))
            print(f"Added song: {song_name} (Genre: {genre})")

        elif choice == '2':
            if music_service.available_songs:
                music_service.show_available_songs()
                song_index = int(input("Enter the index of the song to play (0-based): "))
                if 0 <= song_index < len(music_service.available_songs):
                    music_service.play_song(music_service.available_songs[song_index])
                else:
                    print("Invalid index.")
            else:
                print("No available songs to play.")

        elif choice == '3':
            music_service.undo_selection()

        elif choice == '4':
            music_service.next_song()

        elif choice == '5':
            music_service.show_available_songs()

        elif choice == '6':
            print("Exiting the music service.")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
