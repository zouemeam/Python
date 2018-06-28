class Song(): #classs to represent song
	#attributes title, artist, duration of song in seconds
	def __init__(self,title,artist,duration=0):
		"""This is a DocString which is equivalent to multi-line comment
		"""
		self.title=title
		self.artist=artist
		self.duration=duration


class Album():
	"""class to represent a song object
	Attributes:
		albumName(Str)
		year(Int): publication date of the album
		tracks(List[Song])
	Methods:
		add_song: adds a song to the track(list)
		"""
	def __init__(self,albumName,year, artist=None):
		self.name=albumName
		self.year=year
		if artist==None:
			self.artist=Artist("Various Artist")
		else:
			self.artist=artist
		self.tracks=[]

	def add_song(self,song,position=None):
		"""Adds a song to the track(list)
		Args:
			song(Song): a song to add
			position(Optional[Int]): if specified song will be added to that position, inserting between songs if necessary,
				otherwise, song will be added to the end of the list
		"""
		if position is None:
			self.tracks.append(song)
		else:
			self.tracks.insert(position,song)

class Artist():
	"""class to store artist details
	Attributes:
		name(Str): name of the artist
		album(List[Albums]): A list of albums by this artist

	Methods:
		add_album: adds new album to artist album list
	"""
	def __init__(self,name):
		self.name=name
		self.albums=[]

	def add_album(self,album):
		"""Adds an album to the artist
		Args:
			album(Album): adds the album object to the list, if the album already exist make sure that it is not added
				again
		"""
		self.albums.append(album)

def find_object(field,object_list):
	"""check object_list to see if an object with a name attribute equal to field exists, return it if so"""
	for item in object_list:
		if item.name==field:
			return item
	return None

def load_data():
	new_artist=None
	new_album=None
	artist_list=[]
	with open('albums.txt','r') as albums:
		for line in albums:
			#data row should consist of artist,album,year,song
			artist_field, album_field, year_field, song_field=tuple(line.strip('\n').split('\t'))
			year_field=int(year_field)
			print(artist_field, year_field,album_field,song_field)

			if new_artist is None:
				new_artist=Artist(artist_field)
				artist_list.append(new_artist)
			elif new_artist.name!=artist_field:
				# we just read details for a new artist
				#retrieve the artist object if there is one
				#otherwise create a new artist object and add it to the artist list
				new_artist=find_object(artist_field,artist_list)
				if new_artist is None:
					new_artist=Artist(artist_field)
					artist_list.append(new_artist)
				new_album=None

			if new_album is None:
				new_album=Album(album_field,year_field,new_artist)
				new_artist.add_album(new_album)
			elif new_album.name != album_field:
				#we've read new album for the current artist
				#retrieve album object if there is one
				#otherwise create new alum object and store in artisti collection
				new_album=find_object(album_field,new_artist.albums)
				if new_album is None:
					new_album=Album(album_field,year_field,new_artist)
					new_artist.add_album(new_album)
			#create new song object and add to the current album collection
			new_song=Song(song_field,new_artist) #create the new song object
			new_album.add_song(new_song) #adding the song to the album
		#after reading the last line of the text file, we will have an artist and album that haven't been store-process them now
	return artist_list


def create_checkfile(artist_list):
	"""create a check file from the object data for comparison with the original file"""
	with open("checkfile.txt",'w') as checkfile:
		for new_artist in artist_list:
			for new_album in new_artist.albums:
				for new_song in new_album.tracks:
					print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist,new_album,new_song),file=checkfile)

if __name__=="__main__":
	artists=load_data()
	print("There are {} artist".format(len(artists)))
	create_checkfile(artists)


