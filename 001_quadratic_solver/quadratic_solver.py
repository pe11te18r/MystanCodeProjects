"""
File: quadratic_solver.py
Name: Peter Lin
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	Directly quit the operation if discriminant < 0,
	and discriminate whether there are two roots or not.
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a = '))
	b = int(input('Enter b = '))
	c = int(input('Enter c = '))
	discriminant = (b * b) - (4 * a * c)  # define discriminant
	if discriminant >= 0:
		d = math.sqrt(discriminant)  # 根號裡面需大於等於0才可作運算
		root_1 = (-b + d) / (2 * a)
		root_2 = (-b - d) / (2 * a)
		if discriminant > 0:
			print('Two roots: ' + str(root_1) + ' , ' + str(root_2))
		else:
			print('One root: ' + str(root_1))
	else:
		print('No real roots')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
