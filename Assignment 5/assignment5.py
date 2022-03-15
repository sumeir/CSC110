# assignment5.py
#
# Student name: Sumeir Khinda
# Student id:  V00933760

tests = 0
passed = 0

def main():
	test_is_prime()
	test_count_primes()
	test_sum_digits()

	print("TEST RESULTS: ", passed, "/", tests, sep="")


def test_is_prime():
	print("testing is_prime")
	result = is_prime(3)
	print_test("Testing with 3", result==True)
	result = is_prime(4)
	print_test("Testing with 4", result==False)
	result = is_prime(1)
	print_test("Testing with 1", result==False)
	result = is_prime(2)
	print_test("Testing with 2", result==True)
	

def test_count_primes():
	print ("testing count primes")
	result = count_primes(3, 11) 
	print_test("testing with 3, 11", result==4)
	result = count_primes(4,14)
	print_test("testing with 4, 14", result==4)
	result = count_primes(2,19)
	print_test("testing with 2, 19", result==8)
	result = count_primes(1,7)
	print_test("testing with 1, 7", result==4)


def test_sum_digits():
	print("testing sum_digits")
	result = sum_digits(4)
	print_test("testing with 4", result==4)
	result = sum_digits(469)
	print_test("testing with 469", result==19)
	result = sum_digits(23)
	print_test("testing with 469", result==5)
	result = sum_digits(5274)
	print_test("testing with 469", result==18)


# (int -> bool)
# returns True if n is prime, False otherwise
def is_prime(n):
	if n == 1:
		return False
	elif n == 2:
		return True
	else:
		for x in range(2,n):
			if n % x == 0:
				return False
		return True


# (int, int -> int)
# returns the number of prime numbers found within the
# range of the two given numbers (inclusive)
def count_primes(num1, num2):
	if num1 >= num2:
		larger = num1
		smaller = num2
	elif num2 > num1:
		smaller = num1
		larger = num2
	count = 0
	for x in range(smaller, larger+1):
		if is_prime(x) == True:
			count += 1
		else:
			count = count
	return count


# (int -> int)
# returns the sum of all the digits in the given number
# ASSUME: the value is a positive, whole number.
def sum_digits(n):
	sum = 0
	while n > 0:
		d = n % 10
		sum += d
		n = n // 10
	return sum



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
