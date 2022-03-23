"""
File: rocket.py
Name: Peter Lin 20201003
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
	"""
	Algorithm: divide the rocket into six parts: head, belt, upper, lower, belt, head
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():  # i對應行數，分別印出對應數目的blank space, slash, and backslash
	for i in range(SIZE):
		for j in range(SIZE-i):
			print(' ', end='')
		for j in range(i+1):
			print('/', end='')
		for j in range(i+1):
			print('\\', end='')
		print()


def belt():  # belt的=數為常數兩倍，+頭尾各一
	print('+', end='')
	for i in range(SIZE*2):
		print('=', end='')
	print('+', end='')
	print()


def upper():  # 將upper分成三部分：頭尾的|、兩邊的降冪數量（從常數-1至0）的.、中間升冪數量（從1至常數）的/\
	for i in range(SIZE):
		print('|', end='')
		for j in range((SIZE-1)-i):
			print('.', end='')
		for j in range(i+1):
			print('/\\',end='')
		for j in range((SIZE-1)-i):
			print('.', end='')
		print('|', end='')
		print()


def lower():  # 將lower分成三部分：頭尾的|、兩邊升冪數量（從0至常數-1）的.、中間降冪數量（從常數至1）的\/
	for i in range(SIZE):
		print('|', end='')
		for j in range(i):
			print('.', end='')
		for j in range(SIZE-i):
			print('\\/', end='')
		for j in range(i):
			print('.', end='')
		print('|', end='')
		print()


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()