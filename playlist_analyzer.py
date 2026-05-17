'''
Laurel Lynn
IS 303 - A03

Inputs:
- number of songs (int)
- for each song: 
    - title (str)
    - genre (str)
    - length (float)

Processes: 
- Collect song data into dictionary
- filter by genre
- max/min: find longest song
- count songs over 3 min

Outputs: 
- Print total play time
- print: each genre with book title, length, and genre below
- print: longest song
- print number of songs over 3 min

'''

total_songs = int(input("How many songs? "))
songs = []
genre_filter = {}



for i in range(total_songs):
    
    title = input(f"Song {i+1} title: ")
    genre = input(f"Song {i+1} genre: ")
    song_length = float(input(f"Song {i+1} length: "))
    songs.append({"title": title, "genre": genre, "song length": song_length})

#accumulater for total run time 
run_time = 0
for song in songs:
    run_time += float(song["song length"])

# min/max find longest song
longest_song = songs[0]
for song in songs:
    if (song["song length"]) > longest_song["song length"]:
        longest_song = song

#Filter
for song in songs:
    genre = song["genre"]
    if genre not in genre_filter:
        genre_filter[genre] = []
    genre_filter[genre].append(song["title"])


long_songs = []
for song in songs:
    if song["song length"] > 3.00:
        long_songs.append(song)


#Output
print(f"--- Playlist Analyzer ---")
print(f"Songs in Playlist: {total_songs}")

for genre, titles in genre_filter.items():
    print(f"{genre}: {titles}")
   
print(f"Total play time: {run_time:.2f} minutes")
print(f"Longest song: {longest_song['title']} at {longest_song['song length']} minutes")
print(f"Number of songs over 3 minutes: {len(long_songs)}")
print(f"Names of songs over 3 minutes: {[song['title'] for song in long_songs]}")


