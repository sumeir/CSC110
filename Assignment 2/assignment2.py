# assignment2.py
#
# Student name: Sumeir Khinda
# Student id:  V00933760

def main():
    print('Assignment 2')
    test_print_dog_years()
    test_print_area()
    test_print_average()
    test_small_enough_word()
    test_print_max()
    test_print_num_odd()


def test_print_dog_years():
    print_dog_years(0)  # expects 0
    print_dog_years(3)  # expects 21
    print_dog_years(8)  # expects 56

# (int -> None)
# prints the given human age in dog years
def print_dog_years(age):
    print(age * 7)

def test_print_area():
    print_area(2.7, 10.2)  # expects 27.54
    print_area(3.2, 4.3)  # expects 13.76
    print_area(2.9, 5.7)  # expects 16.53

# (float, float -> None)
# calculates the area of the rectangle rounded to two decimal places, given the length and the width.
def print_area(length, width):
    area = length * width
    print(round(area, 2))

def test_print_average():
    print_average(0.0,0.0,0.0)  # expects 0.0
    print_average(23.4,34.4,45.5)  # expects 34.4
    print_average(5.3,12.4,17.3)  # expects 11.7

# (float, float, float -> None)
# prints the average of the three numbers, rounded to one decimal place.
def print_average(num1,num2,num3):
    average = (num1 + num2 + num3)/3
    print(round(average,1))

def test_small_enough_word():
    # expects: "Error: 2 characters too large"
    small_enough_word("anthony", 5)
    # expects: "Error: 3 characters too large"
    small_enough_word("jacob", 2)
    # expects: "coco is perfectly valid"
    small_enough_word("coco", 4)

# (str, int -> None)
# compares the word with the maximum allowable number of characters that the word can contain and prints a statement depending upon the result.
def small_enough_word(word,num):
    len_word = len(word)
    X = len_word - num
    Y = word
    if len_word > num:
        print("Error:", X, "characters too large")
    elif len_word <= num:
        print(Y, "is perfectly valid")

def test_print_max():
    print_max(0,0,1)  # expects 0
    print_max(4,1,9)  # expects 9
    print_max(3,7,8)  # expects 8

# (int, int, int -> None)
# prints the biggest of the three numbers.
def print_max(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num1 and num2 > num3:
        print(num2)
    elif num3 > num1 and num3 > num2:
        print(num3)
    
def test_print_num_odd():
    # expects "0 odd numbers were found"
    print_num_odd(0,0,0)
    # expects "1 odd number was found"
    print_num_odd(3,4,8)
    # expects "2 odd numbers were found"
    print_num_odd(3,5,6)

# (int, int, int -> None)
# prints the number of odd numbers.
def print_num_odd(num1,num2,num3):
    if num1 % 2 == 1 and num2 % 2 == 1 and num3 % 2 == 1:
        print("3 odd numbers were found")
    elif num1 % 2 == 1 and num2 % 2 == 1 and num3 % 2 == 0:
        print("2 odd numbers were found")
    elif num1 % 2 == 0 and num2 % 2 == 1 and num3 % 2 == 1:
        print("2 odd numbers were found")
    elif num1 % 2 == 1 and num2 % 2 == 0 and num3 % 2 == 1:
        print("2 odd numbers were found")
    elif num1 % 2 == 1 and num2 % 2 == 0 and num3 % 2 == 0:
        print("1 odd number was found")
    elif num1 % 2 == 0 and num2 % 2 == 1 and num3 % 2 == 0:
        print("1 odd number was found")
    elif num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 1:
        print("1 odd number was found")
    elif num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0:
        print("0 odd numbers were found")

# The following code will call your main function
# It also allows our grading script to call your main
# DO NOT ADD OR CHANGE ANYTHING PAST THIS LINE
# DOING SO WILL RESULT IN A ZERO GRADE
if __name__ == '__main__':
    main()