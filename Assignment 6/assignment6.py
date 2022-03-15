# assignment6.py
#
# Student name: Sumeir Khinda
# Student id:  V00933760

tests = 0
passed = 0

def main():
	test_new_double_list()
	test_double_existing_list()
	test_count_multiples()
	test_sum_positive()
	test_add_prefix()
	test_all_long_enough()
	test_growing_strings()

	print("TEST RESULTS: ", passed, "/", tests, sep="")

def test_new_double_list():
	print("testing new_double_list")
	list1 = []
	result = new_double_list(list1)
	print_test("testing list1 unchanged", list1==[])
	print_test("testing value returned with empty", result==[])

	list2 = [3, 8, 4, 7]
	result = new_double_list(list2)
	print_test("testing list2 unchanged", list2==[3,8,4,7])
	print_test("testing value returned with list2", result==[6,16,8,14])

	list3 = [5, 9, 2, 3]
	result = new_double_list(list3)
	print_test("testing list3 unchanged", list3==[5,9,2,3])
	print_test("testing value returned with list3", result==[10,18,4,6])
	print()

def test_double_existing_list():
	print("testing double_existing_list")
	list1 = []
	double_existing_list(list1)
	print_test("testing with empty list", list1==[])
	list2 = [3, 8, 4, 7]
	double_existing_list(list2)
	print_test("testing with list2", list2==[6,16,8,14])
	list3 = [5, 9, 2, 3]
	double_existing_list(list3)
	print_test("testing with list3", list3==[10,18,4,6])
	print()

def test_count_multiples():
	print("testing count_multiples")
	list1 = []
	result = count_multiples(list1, 2)
	print_test("testing with empty and 2", result==0)
	list2 = [2, 9, 18, 7]
	result = count_multiples(list2, 3)
	print_test("testing with list2 and 3", result==2)
	list3 = [2, 13, 21, 49]
	result = count_multiples(list3, 7)
	print_test("testing with list3 and 7", result==2)
	print()

def test_sum_positive():
	print("testing sum_positive")
	list1 = []
	result = sum_positive(list1)
	print_test("testing with empty", result==0)
	list2 = [2, -3, 5, 9]
	result = sum_positive(list2)
	print_test("testing with list2", result==16)
	list3 = [4, 5, -1, 18]
	result = sum_positive(list3)
	print_test("testing with list3", result==27)
	list4 = [2, -9, 0, 4]
	result = sum_positive(list4)
	print_test("testing with list4", result==6)	
	print()

def test_add_prefix():
	print("testing add_prefix")
	list1 = []
	add_prefix(list1, "un")
	print_test("testing with empty list and un", list1==[])

	list2 = ["zip", "real", "likely", "veil"]
	add_prefix(list2, "un")
	expected = ["unzip", "unreal", "unlikely", "unveil"]
	print_test("testing with list2 and un", list2==expected)

	list3 = ["fine", "lay", "spite", "tail"]
	add_prefix(list3, "re")
	expected = ["refine", "relay", "respite", "retail"]
	print_test("testing with list3 and re", list3==expected)

	list4 = ["fine", "lay", "spite", "tail"]
	add_prefix(list4, "de")
	expected = ["define", "delay", "despite", "detail"]
	print_test("testing with list4 and de", list4==expected)
	print()


def test_all_long_enough():
	print("testing all_long_enough")
	list1 = []
	result = all_long_enough(list1, 0)
	print_test("testing with empty and 0", result==True)

	list2 = ["this", "is", "so", "fun"]
	result = all_long_enough(list2, 1)
	print_test("testing with list2 and 1", result==True)

	list3 = ["cat", "dog", "horse"]
	result = all_long_enough(list3, 4)
	print_test("testing with list3 and 4", result==False)

	print()

def test_growing_strings():
	print("testing growing_strings")
	list1 = []
	result = growing_strings(list1)
	print_test("testing with empty list", result==True)
	list2 = ["ab", "abc", "abcd"]
	result = growing_strings(list2)
	print_test("testing with list2", result==True)
	list3 = ["wxyz", "xyz", "xy"]
	result = growing_strings(list3)
	print_test("testing with list3", result==False)
	list4 = ["abc", "wxyz", "ab"]
	result = growing_strings(list4)
	print_test("testing with list4", result==False)
	print()

# ((list of int) -> (list of int))
# returns a new list with each element double of the given list
def new_double_list(lon):
	new_list = []
	for i in lon:
		new_list.append(i*2)
	return new_list

# ((list of int) -> None)
# doubles the values of all the elements in a given list
def double_existing_list(lon):
	index = 0
	for i in lon:
		lon[index] = i * 2
		index += 1

# ((list of int), int -> int)
# counts the number of elements in a list which are multiples of a given number
def count_multiples(lon, n):
	count = 0
	if len(lon) == 0:
		return 0
	else:
		for i in lon:
			if i % n == 0:
				count += 1
		return count

# ((list of int) -> int)
# adds up all the positive integers of a list
def sum_positive(lon):
	new_list = []
	for i in lon:
		if i >= 0:
			new_list.append(i)
	return sum(new_list)

# ((list of str), str -> None)
# adds a prefix to all words in a list
def add_prefix(los, prefix):
	index = 0
	for i in los:
		los[index] = prefix + i
		index += 1

# ((list of str), int -> bool)
# tests if all strings in a list have a given number of characters
def all_long_enough(los, n):
	count = 0
	for i in los:
		if len(i) >= n:
			count += 1
	if len(los) == count:
		return True
	else:
		return False

# ((list of str) -> bool)
# tests if all strings in a list grow in size
def growing_strings(los):
	if len(los) == 0 or len(los) == 1:
		return True
	else:
		for i in range(len(los)-1):
			if len(los[i+1]) <= len(los[i]):
				return False
		return True

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
