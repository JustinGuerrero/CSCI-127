import random
import math
import csv
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


#-------------------------------#
#The menu will print the choices#
#_______________________________#
def menu():
    print()
    print("1. Identify longest song.")
    print("2. Identify number of songs in a given year.")
    print("3. Identify all songs by a given artist.")
    print("4. Have me choose a song for you.")
    print("5. Quit.")

f = open("music.csv", "r")
#___________________Define the function for longest song
def longest_song():
    f = open('music.csv' , 'r')
    duration_max = 0
    line_count = 0
    song_name_duration = ""
    ##make a for loop to iterate over the lines (i) in your file
    for i in f:
        songs = i.split(",")
        if line_count != 0:
            if float(songs[9]) > duration_max:
                duration_max = float(songs[9])
                song_name_duration = songs[-2]
        line_count += 1
##We place the line_count method in there to skip over the first line in the csv file to make the float numbers work
        
    print("Here is one long song name", song_name_duration)    
    print("at the length",round(duration_max))
    


def songs_by_year(year):
    f = open('music.csv' , 'r')
    yeart = 0
    songs = []
    ## create a song list for us to search through, and then make a for loop again to search through lines
    ## split the lines by comma, strip will take away the white spaces allowing code to read
    ## then do yeart += 1 to keep count and add songs to the count.
    for i in f:
        songs = i.split(",")    
        if songs[-1].strip() == str(year):
            yeart += 1
            
    print("the song(s) from the year are: " + str(yeart))

    
def all_songs_by_artist(artist):
    f = open('music.csv' , 'r')
    artist_songs = []
    line_count = 0
    ## create your song list, and line counter. initiate for loop as we've done above
    ## next we will create our if statements to give equalities.
    ## then you'll set the song_name variable equal to the row and song column
    for i in f:
        artist_row = i.split(",")
        if artist_row[2].lower() == str(artist):
            song_name = artist_row[-2]
            artist_songs.append(song_name)
    ## next thing you'll see is where we sort the songs into alphabetical order
    ## followed by printing our statements
    artist_songs.sort()
    print("\n","The songs from this Artist in Alphabetical order", "\n" ,
          "------------------------------------------------")
    ## if the artist is NOT in the library make a not equal to statement
    
    if artist_row[2].lower != str(artist):
        print(" There are no songs by this artist", "\n" ,
              "---------------------------------")
    ## this counter will make the 1, 2, 3, 4, etc for the track ids
    count = 0
    for i in artist_songs:
        print(count + 1, i)
        count += 1
        
        

def random_song():
    f = open("music.csv", 'r')
    random_number = random.randint(1,10000)
    line_count = 1
    ## above you'll see that we used random_number because random cannot be used as a variable name
    ## then you'll set your parameters (we used rows)
    ## then we set the line count - equal to the random number, so when they match it prints a song
   
    for i in f:
        songs = i.split(",")
        if line_count == random_number:
            print("\n", "Listen to this track! " , songs[-2],"by", songs[2])
        line_count += 1
    ## you'll also make a line counter here to make sure the counter is iterating through
    ## the lines
        


    
#----------------------------------------------------
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
            random_song()
        elif (choice != 5):
            print("That is not a valid option.  Please try again.")

main()
f.close()
