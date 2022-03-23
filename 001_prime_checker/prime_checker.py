"""
File: prime_checker.py
Name: Peter Lin
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""


def main():
	"""
	從2開始，對input一直做除法，如裹在除到自己之前就除盡即非質數，除到自己才除盡即為質數。
	"""
	print('Welcome to the prime checker!')
	while True:
		n = int(input('n: '))
		a = 2
		if n == -100:
			break
		else:
			while n % a != 0:
				a += 1
			if n == a:
				print(str(n) + ' is a prime number.')
			else:
				print(str(n) + ' is not a prime number.')
	print('Have a good one!')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
