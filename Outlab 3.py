### ---------------------------------------
### CSCI 127, Joy and Beauty of Data
### Program 3: Msuic CSV Library
### Justin Guerrero
### October 14 2018 
### ---------------------------------------
### This program is designed to open a music file and
### be able to find, the longest song, the number of songs
### in a given year, and identify all songs by an artist.
### ---------------------------------------
##
### --------------------------------------


import math

##open the file.

f = open("music.csv", "r")


def menu():
    print()
    print("1. Identify longest song.")
    print("2. Identify number of songs in a given year.")
    print("3. Identify all songs by a given artist.")
    print("4. Have me choose a song for you.")
    print("5. Quit.")

# --------------------------------------
##define the stuff you're trying to do
def longest_song():
    f = open("music.csv", "r")
    song_names = []
    time = 0
    line = f.readline()
    line = f.readline()
    ## will use a while loop sequence to iterate through the songs
    while (line != ""):
        line = line.split(",")
        duration = float(line[9])
        if int(duration) + 0.5 < duration:
            duration = int(duration) +1
        else:
            duration = int(duration)
        if (int(duration) > time):
            time = int(duration)
            song_names.clear()
            song_names.append(line[-2])
        elif (int(duration == time)):
            song_name.append(line[-2])
        line = f.readine()
    output = song_names[0]
    for i in range(1, len(song_names)):
        output += " / " + song_names[i] + "\n"
    print("Title: " + output)
    print("Length to nearest second: " + str(time))
    
###cool find songs older than most of the kids in our class
def songs_by_year(year):
    f = open("music.csv", "r")
    song_name = []
    songs = 0
    line = f.readline()
    while(line != ""):
        line = line.split()
        if int(line[-1]) == year:
            songs + 1
        line = f.readline()
    print("The number of songs from " + str(year) + " is " + str(songs))


##sweet songs by an artist, spotify hire me!
    
def all_songs_by_artist(artist):
    f = open("music.csv", 'r')
    song_name = []
    line = f.readline()
    while(line != ""):
        line = line.split(",")
        if line[2].lower() == artist:
            song_name.append(line[-2])
        line = f.readline()
    song_name = sorted(song_name)
    print("\n" + "songs in Alphabetical OrDeR" + "\n" +  "------------------------")
    for i in range(len(song_name)):
        print(str((i+1)) + "" + song_name[i])

#kind of like pushing the shuffle all button except you only get one song
        
def random():
    f = open("music.csv", "r")
    line = f.readline()
    count = 0
    while(line != ""):
        count += 1
    for i in range(random.randint(1, count + 1)):
        line = f.readline()
        
    print("listen to this song: " + line.split(",")[-2] + " by " + line.split(",")[2])
    
        
  
def main():
    choice = 0
    while (choice != 5):
        menu()
        choice = int(input("Enter your choice: "))
        if (choice == 1):
            longest_song()
        elif (choice == 2):
            year = int(input("Enter desired year: "))
            songs_by_year(year)
        elif (choice == 3):
            artist = input("Enter name of artist: ").lower()
            all_songs_by_artist(artist)
        elif (choice == 4):
            random
        elif (choice != 5):
            print("That is not a valid option.  Please try again.")

# --------------------------------------

main()
f.close()
