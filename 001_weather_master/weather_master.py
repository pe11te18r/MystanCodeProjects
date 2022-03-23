"""
File: weather_master.py
Name: Peter Lin
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

QUIT = -100


def main():
	"""
	average算法：用summation累加input、用times累計input次數。
	"""
	print('stanCode \"Weather Master 4.0"')
	temp = int(input('Next Temperature: (or -100 to quit)?'))
	if temp == QUIT:
		print('No temperatures were entered.')
	else:
		maximum = temp
		minimum = temp
		summation = temp
		times = 1
		cold = 0
		if temp < 16:
			cold += 1
		while True:
			temp = int(input('Next Temperature: (or -100 to quit)?'))
			if temp == QUIT:
				break
			else:
				if temp > maximum:
					maximum = temp
				if temp < minimum:
					minimum = temp
				if temp < 16:
					cold += 1
				summation += temp
				times += 1
		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = ' + str(minimum))
		average = summation / times
		print('Average = ' + str(average))
		print(str(cold) + ' cold day(s)')









###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
