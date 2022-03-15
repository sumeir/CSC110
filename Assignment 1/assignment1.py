# assignment1.py
#
# Student name: Sumeir Khinda
# Student id:  V00933760

def main():
   print("Welcome")
   print()
   # You will call your functions here to test them:
   # print_cat()
   # print_toad()
   # print_spacer()
   print_logo()
   calc_surface_area()

# DEFINE your functions after this line:

# prints a cat
def print_cat():
	print("| /\\_/\\ |")
	print("| >^.^< |")
	print("|  / \\  |")
	print("| (|_|)~|")

# prints a toad
def print_toad():
	print("|  @ @  |")
	print("| (---) |")
	print("|( > < )|")
	print("|\"\"   \"\"|")

# spacer lines printed between each animal
def print_spacer():
	print("/-------\\")

# calls the previous two functions
def print_logo():
	print_spacer()
	print_toad()
	print_spacer()
	print_cat()
	print_spacer()
	print_toad()
	print_spacer()
	print_cat()
	print_spacer()
	print_spacer()

# calculates the surface area of the given cylinder
def calc_surface_area():
	height = 6
	diameter = 5
	pi = 3.14
	circumference = pi * diameter
	area_of_top = pi * diameter**2 / 4
	area_of_walls = circumference * height
	total_surface_area = area_of_walls + 2 * area_of_top
	print(total_surface_area)


# The following code will call your main function
# It also allows our grading script to call your main
# DO NOT ADD OR CHANGE ANYTHING PAST THIS LINE
# DOING SO WILL RESULT IN A ZERO GRADE
if __name__ == '__main__':
   main()
