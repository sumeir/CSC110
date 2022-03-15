# assignment4.py
#
# Student name: Sumeir Khinda
# Student id:  V00933760

tests = 0
passed = 0

def main():

    test_get_factorial()
    print("") # an empty line between each test just so it looks neat
    test_get_occurrences()
    print("")
    test_count_multiples()
    print("")
    test_print_ten_multiples()
    print("")
    print("Test results:", passed, "/", tests)


def test_get_factorial():
    print("testing get_factorial...")

    result = get_factorial(0)
    print_test("test with 0", result == 1)

    result = get_factorial(7)
    print_test("test with 7", result == 5040)


def test_get_occurrences():
    print("testing get_occurrences...")

    result = get_occurrences("x","anthony")
    print_test("testing with x and anthony", result==0)
    
    result = get_occurrences("m","tianming")
    print_test("testing with m and tianming", result==1)


def test_count_multiples():
    print("testing count_multiples...")

    result = count_multiples(1, 9, 2)
    print_test("testing with 1, 9, 2", result==4)

    result = count_multiples(3, 12, 4)
    print_test("testing with 3, 12, 4", result==2)

    result = count_multiples(7, 40, 5)
    print_test("testing with 7, 40, 5", result==6)
    

def test_print_ten_multiples():
    print("testing print_ten_multiples")

    print("\nTesting with 3")
    print_ten_multiples(3) # expects final row to be 3 - 30

    print("")

    print("\nTesting with 4")
    print_ten_multiples(4) # expects final row to be 4 - 40

    print("")

    print("\nTesting with 2")
    print_ten_multiples(2) # expects final row to be 2 - 20

    print("")


# (int -> int)
# finds the factorial of a number.
def get_factorial(n):
    factorial = 1
    if n == 0:
        return 1
    else:
        for i in range(1,n+1):
            factorial *= i
    return factorial


# (str, str -> int)
# takes two strings and returns the number of times 
# the first string appears in the second string.
def get_occurrences(c, text):
    count = 0
    for i in range(0, len(text)):
        if c == text[i]:
            count += 1
    return count


# (int, int, int -> int)
# takes three whole positive numbers. the first two define a range of values to search. the
# function returns how many numbers within the range are multiples of the third number.
def count_multiples(start, end, n):
    count = 0
    for i in range(start,end):
        if i % n == 0:
            count += 1
    return count

# (int -> int)
# takes a number and prints out the first 10 multiples of all numbers from 1 up to the given number.
def print_ten_multiples(max):
    for i in range(1,max+1):
        print("\n")
        for j in range(1,11):
            print(format(i * j, "3d"), end="")


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
