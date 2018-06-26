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
		self.albumName=albumName
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

def load_data():
	new_artist=None
	new_album=None
	artist_list=[]
	with open('albums.txt','r') as albums:
		for line in albums:
			#data row should consist of artist,album,year,song
			artist_field, album_field, year_field, song_field=tuple(line.strip('\n').split('\t'))
			year_field=int(year_field)
			print(artist_field, year_field)

if __name__=="__main__":
	load_data()