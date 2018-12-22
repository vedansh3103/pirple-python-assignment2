# Using functions

Genre= "Korean Pop"
Artist= "BTS"
Year= 2016

def SongGenre():
  print("Genre of the song: ")
  print(Genre)

def SongArtist():
  print("Artist of the song: ")
  print(Artist)

def ReleaseYear():
  print("Year the song was released: ")
  print(Year)

def Members(x):
  return(bool(x==7))

SongGenre()
SongArtist()
ReleaseYear()       

a=int(input("Enter the number of members in BTS: "))
b=Members(a)
print(b)