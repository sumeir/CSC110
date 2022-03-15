# assignment3.py
#
# Student name: Sumeir Khinda
# Student id:  V00933760

tests = 0
passed = 0
THRESHOLD = 0.1

FULL_BATTERY_LIFE = 15

def main():
	print('Assignment 3')
	test_middle_value()
	test_combine_strings()
	test_get_letter_at()
	test_brightness_modifier()
	test_hours_remaining()
	print("TEST RESULTS:", passed, "/", tests)


# TEST FUNCTION DEFINITIONS:

def test_middle_value():

	print("beginning tests for middle_value...")

	a = 1
	b = 4
	c = 7
	result = middle_value(a, b, c)
	expected = 4
	print("a:", a, "b:", b, "c:", c, "result:", result, "expected", expected)
	print_test("test 1", result == expected)

	a = 2
	b = 4
	c = 3
	result = middle_value(a, b, c)
	expected = 3
	print("a:", a, "b:", b, "c:", c, "result:", result, "expected", expected)
	print_test("test 2", result == expected)

	a = 9
	b = 7
	c = 6
	result = middle_value(a, b, c)
	expected = 7
	print("a:", a, "b:", b, "c:", c, "result:", result, "expected", expected)
	print_test("test 3", result == expected)


def test_combine_strings():

	print("beginning tests for combine_strings...")

	a = "skip"
	b = "bat"
	result = combine_strings(a, b)
	expected = "batskip"
	print("a:", a, "b:", b, "result:", result, "expected:", expected)
	print_test("test 1", result == expected)

	a = "silk"
	b = "exile"
	result = combine_strings(a, b)
	expected = "silkexile"
	print("a:", a, "b:", b, "result:", result, "expected:", expected)
	print_test("test 2", result == expected)

	a = "sketch"
	b = "dilute"
	result = combine_strings(a, b)
	expected = "sketchdilute"
	print("a:", a, "b:", b, "result:", result, "expected:", expected)
	print_test("test 3", result == expected)
	

def test_get_letter_at():

	print("beginning tests for get_letter_at...")
	
	word = "disgrace"
	num = 0
	result = get_letter_at(word, num)
	expected = "d"
	print("word:", word, "num:", num, "result:", result, "expected:", expected)
	print_test("test 1", result == expected)

	word = "fruit"
	num = 2
	result = get_letter_at(word, num)
	expected = "u"
	print("word:", word, "num:", num, "result:", result, "expected:", expected)
	print_test("test 2", result == expected)

	word = "ant"
	num = 3
	result = get_letter_at(word, num)
	expected = ""
	print("word:", word, "num:", num, "result:", result, "expected:", expected)
	print_test("test 3", result == expected)


def test_brightness_modifier():

	print("beginning tests for brightness_modifier...")

	level = 0
	result = brightness_modifer(0)
	expected = 1.0
	print("level:", level, "result:", result, "expected:", expected)
	print_test("test 1", result == expected)

	level = 1
	result = brightness_modifer(1)
	expected = 0.9
	print("level:", level, "result:", result, "expected:", expected)
	print_test("test 2", result == expected)

	level = 2
	result = brightness_modifer(2)
	expected = 0.75
	print("level:", level, "result:", result, "expected:", expected)
	print_test("test 3", result == expected)

	level = 3
	result = brightness_modifer(3)
	expected = 0.5
	print("level:", level, "result:", result, "expected:", expected)
	print_test("test 4", result == expected)
	

def test_hours_remaining():

	print("beginning tests for hours_remaining...")

	battery = 80
	level = 2
	stream = True
	result = hours_remaining(80, 2, True)
	expected = 4.5
	print("battery:", battery, "level", level, "stream", stream, "result", result, "expected", expected)
	print_test("test 1", result == expected)

	battery = 90
	level = 1
	stream = False
	result = hours_remaining(90, 1, False)
	expected = 12.15
	print("battery:", battery, "level", level, "stream", stream, "result", result, "expected", expected)
	print_test("test 2", result == expected)

	battery = 40
	level = 3
	stream = True
	result = hours_remaining(40, 3, True)
	expected = 1.5
	print("battery:", battery, "level", level, "stream", stream, "result", result, "expected", expected)
	print_test("test 3", result == expected)



# FUNCTION DEFINITIONS:


# (int, int, int -> int)
# takes 3 integers and returns the integer with the middle value.
# if there's a tie, it returns any of the possible middle values.
def middle_value(a,b,c):
	if a <= b <= c or c <=b <= a:
		return b
	elif b <= a <= c or c <= a <= b:
		return a
	else:
		return c


# (str, str -> str)
# takes two phrases and appends the longer one onto the back of the shorter one
# with no space between the phrases joined.
# if the the two phrases are same in length, then it appends the second one
# onto the back of the first one.
def combine_strings(a,b):
	if len(a) > len(b):
		return b + a
	elif len(b) > len(a):
		return a + b
	else:
		return a + b


# (str, int-> str)
# takes a phrase and a number and returns the letter at the phrase at the given index.
# if the number is too large, returns an empty string.
def get_letter_at(word,num):
	if (num <= (len(word) - 1)):
	 	return word[num]
	else:
		return ""


# (int -> float)
# takes integers 0, 1, 2, or 3, representing the brightness level of a smartphone,
# and returns a decimal number representing the modifier that the brightness level
# will affect the lifetime of the battery of the device.
def brightness_modifer(level):
	if level == 0:
		return 1.0
	elif level == 1:
		return 0.9
	elif level == 2:
		return 0.75
	elif level == 3:	
		return 0.5		


# (int, int, bool -> float)
# takes the percentage of battery life left, the brightness, 
# whether the device is currently streaming video. returns the
# total hours of battery life left.
def hours_remaining(battery,level,stream):	
	hours_left= FULL_BATTERY_LIFE * (battery/100) * brightness_modifer(level)
	if stream:
		hours_left /= 2
		return(hours_left)
	else:
		return(hours_left)



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
# It also allows our grading script to call your main
# DO NOT ADD OR CHANGE ANYTHING PAST THIS LINE
# DOING SO WILL RESULT IN A ZERO GRADE
if __name__ == '__main__':
    main()
