# assignment9.py
#
# Student name: Sumeir Khinda
# Student id: V00933760

tests = 0
passed = 0
import Song as s
import Playlist as p

def main():
	### PART 1: Song
	test_is_longer()
	test_count_with_artist()

	### Part 2: Playlist
	test_playlist_basics()
	test_are_equal()
	test_get_status()
	test_next_song()

	print("TEST RESULTS:", passed, "/", tests)


########################
### PART 1 FUNCTIONS ###

# (Song, Song -> Song)
# return the song with the longest duration
def is_longer(s1, s2):
	if(s1.get_duration()>=s2.get_duration()):
		return s1
	else:
		return s2

# ((list of Song), str -> int)
# return a count of the number of songs
# in the list with the given artist
def count_with_artist(los, a):
	count = 0
	for i in los:
		if i.get_artist() == a:
			count += 1
	return count

def test_is_longer():
	print("testing is_longer")
	s1 = s.Song("Despacito", "Justin Bieber", 225)
	s2 = s.Song("Crazy", "Britney Spears", 245)
	s3 = s.Song("Champions", "Queen", 220)
	s4 = s.Song("The Motto", "Drake", 225)

	result = is_longer(s1, s2)
	print_test("testing with s1 and s2", result==s2)
	result = is_longer(s1, s3)
	print_test("testing with s1 and s3", result==s1)
	result = is_longer(s1, s4)
	print_test("testing with s1 and s4", result==s1)
	print()

def test_count_with_artist():
	print("testing count_with_artist")
	s1 = s.Song("Despacito", "Justin Bieber", 225)
	s2 = s.Song("Crazy", "Britney Spears", 245)
	s3 = s.Song("Champions", "Queen", 220)
	s4 = s.Song("The Motto", "Drake", 225)
	s5 = s.Song("Baby", "Justin Bieber", 216)

	list0 = []
	result = count_with_artist(list0, "Justin Bieber")
	print_test("testing with empty and Bieber", result==0)

	list1 = [s1, s2, s3, s4, s5]
	result = count_with_artist(list1, "Elton John")
	print_test("testing with list1 and Elton John", result==0)
	result = count_with_artist(list1, "Drake")
	print_test("testing with list1 and Drake", result==1)
	result = count_with_artist(list1, "Justin Bieber")
	print_test("testing with list1 and Bieber", result==2)
	print()

def test_playlist_basics():
	print("testing playlist basics")
	list1 = []
	list2 = [s.Song("Champions", "Queen", 220), \
			 s.Song("Africa", "Toto", 295), \
			 s.Song("Hey Jude", "The Beatles", 431), \
			 s.Song("Like a Prayer", "Madonna", 319)]

	list3 = [s.Song("Someone You Loved", "Lewis Capaldi", 182), \
			 s.Song("Circles", "Post Malone", 215), \
			 s.Song("Truth Hurts", "Lizzo", 173), \
			 s.Song("Only Human", "Jonas Brothers", 183), \
			 s.Song("Senorita", "Shawn Mendes", 191), \
			 s.Song("Beautiful People", "Ed Sheeren", 207), \
			 s.Song("Goodbyes", "Post Malone", 175)]

	playlist1 = p.Playlist("None", list1)
	playlist2 = p.Playlist("Oldies", list2)
	playlist3 = p.Playlist("Top 40", list3)

	# Part a:
	print(playlist1) 
	print(playlist2) 
	print(playlist3) 

	# Part b:
	playlist2.set_name("Classics")
	print(playlist2) 

	# Part c:
	result = playlist1.get_duration()
	print_test("testing with playlist1", result == 0)
	result = playlist2.get_duration()
	print_test("testing with playlist2", result == 1265)
	result = playlist3.get_duration()
	print_test("testing with playlist3", result == 1326)


	# Part d:
	playlist2.add_song(s.Song("Dream on", "Aerosmith",265))
	expected = [s.Song("Champions", "Queen", 220), \
			 s.Song("Africa", "Toto", 295), \
			 s.Song("Hey Jude", "The Beatles", 431), \
			 s.Song("Like a Prayer", "Madonna", 319), \
			 s.Song("Dream on", "Aerosmith",265)]
	print_test("testing with playlist2 and Dream on", expected==playlist2.get_songs())

	playlist3.add_song(s.Song("Circles", "Post Malone", 215))
	expected = [s.Song("Someone You Loved", "Lewis Capaldi", 182), \
			 s.Song("Circles", "Post Malone", 215), \
			 s.Song("Truth Hurts", "Lizzo", 173), \
			 s.Song("Only Human", "Jonas Brothers", 183), \
			 s.Song("Senorita", "Shawn Mendes", 191), \
			 s.Song("Beautiful People", "Ed Sheeren", 207), \
			 s.Song("Goodbyes", "Post Malone", 175)]
	print_test("testing with playlist2 and Circles", expected==playlist3.get_songs())

def test_are_equal():
	print("testing are_equal")

	list1 = []
	list2 = [s.Song("Champions", "Queen", 220), \
			 s.Song("Africa", "Toto", 295), \
			 s.Song("Hey Jude", "The Beatles", 431), \
			 s.Song("Like a Prayer", "Madonna", 319)]
	list3 = [s.Song("Africa", "Toto", 295), \
			 s.Song("Champions", "Queen", 220), \
			 s.Song("Like a Prayer", "Madonna", 319), \
			 s.Song("Hey Jude", "The Beatles", 431)]
	list4 = [s.Song("Someone You Loved", "Lewis Capaldi", 182), \
			 s.Song("Circles", "Post Malone", 215), \
			 s.Song("Truth Hurts", "Lizzo", 173), \
			 s.Song("Only Human", "Jonas 	Brothers", 183), \
			 s.Song("Senorita", "Shawn Mendes", 191), \
			 s.Song("Beautiful People", "Ed Sheeren", 207), \
			 s.Song("Goodbyes", "Post Malone", 175)]

	playlist1 = p.Playlist("None", list1)
	playlist2 = p.Playlist("Oldies", list2)
	playlist3 = p.Playlist("Favs", list3)
	playlist4 = p.Playlist("Top 40", list4)

	print_test("testing with playlist1 and playlist2", (playlist1==playlist2)==False)
	print_test("testing with playlist3 and playlist3", (playlist2==playlist3)==True)
	print_test("testing with playlist4 and playlist3", (playlist4==playlist3)==False)
	print()

def test_get_status():
	print("Testing get_status")
	
	list1 = []
	list2 = [s.Song("Champions", "Queen", 220), \
			 s.Song("Africa", "Toto", 295), \
			 s.Song("Hey Jude", "The Beatles", 431), \
			 s.Song("Like a Prayer", "Madonna", 319)]
	list3 = [s.Song("Africa", "Toto", 295), \
			 s.Song("Champions", "Queen", 220), \
			 s.Song("Like a Prayer", "Madonna", 319), \
			 s.Song("Hey Jude", "The Beatles", 431)]
	list4 = [s.Song("Someone You Loved", "Lewis Capaldi", 182), \
			 s.Song("Circles", "Post Malone", 215), \
			 s.Song("Truth Hurts", "Lizzo", 173), \
			 s.Song("Only Human", "Jonas 	Brothers", 183), \
			 s.Song("Senorita", "Shawn Mendes", 191), \
			 s.Song("Beautiful People", "Ed Sheeren", 207), \
			 s.Song("Goodbyes", "Post Malone", 175)]

	playlist1 = p.Playlist("None", list1)
	playlist2 = p.Playlist("Oldies", list2)
	playlist3 = p.Playlist("Favs", list3)
	playlist4 = p.Playlist("Top 40", list4)

	result=playlist1.get_status(0)
	print_test("testing with playlist1 and 0", result==("None",0))
	result=playlist2.get_status(250)
	print_test("testing with playlist2 and 250", result==("Africa",30))
	result=playlist3.get_status(500)
	print_test("testing with playlist3 and 500", result==("Champions",205))
	result=playlist4.get_status(750)
	print_test("testing with playlist4 and 750", result==("Only Human",180))
	print()

def test_next_song():
	print("Testing next_song")
	list1 = [s.Song("Champions", "Queen", 220), \
			 s.Song("Africa", "Toto", 295), \
			 s.Song("Hey Jude", "The Beatles", 431), \
			 s.Song("Like a Prayer", "Madonna", 319)]
	list2 = [s.Song("Africa", "Toto", 295), \
			 s.Song("Champions", "Queen", 220), \
			 s.Song("Like a Prayer", "Madonna", 319), \
			 s.Song("Hey Jude", "The Beatles", 431)]
	list3 = [s.Song("Someone You Loved", "Lewis Capaldi", 182), \
			 s.Song("Circles", "Post Malone", 215), \
			 s.Song("Truth Hurts", "Lizzo", 173), \
			 s.Song("Only Human", "Jonas 	Brothers", 183), \
			 s.Song("Senorita", "Shawn Mendes", 191), \
			 s.Song("Beautiful People", "Ed Sheeren", 207), \
			 s.Song("Goodbyes", "Post Malone", 175)]
	
	playlist1 = p.Playlist("Oldies", list1)
	playlist2 = p.Playlist("Favs", list2)
	playlist3 = p.Playlist("Top 40", list3)

	result=playlist1.next_song("Africa")
	print_test("testing with playlist1 and Africa",result==s.Song("Hey Jude", "The Beatles", 431))
	result=playlist2.next_song("Champions")
	print_test("testing with playlist2 and Champions",result==s.Song("Like a Prayer", "Madonna", 319))
	result=playlist3.next_song("Senorita")
	print_test("testing with playlist3 and Senorita",result==s.Song("Beautiful People", "Ed Sheeren", 207))
	print()

# (str, bool -> None)
# takes the name or description of a test and whether the
# test produced the expected output (True) or not (False)
# and prints out whether that test passed or failed
# NOTE: You should not have to modify this in any way.
def print_test(test_name, result_correct):
	global tests
	global passed
	tests += 1
	if(result_correct):
		print(test_name + ": passed")
		passed += 1
	else:
		print(test_name + ": failed")

# The following code will call your main function
if __name__ == '__main__':
	main()
