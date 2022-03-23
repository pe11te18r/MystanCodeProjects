"""
File: coin_flip_runs.py
Name: Peter Lin
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
    """
    Algorithm:set up the boundary condition first, use function 'random_world' to flip the coins,
    and use while true to count the repetition times.
    """
    print('Let\'s flip a coin!')
    a = int(input('Number of runs: '))
    rolls = ''
    roll1 = random_world()
    rolls += roll1
    count = 0
    is_in_a_row = False
    while True:
        roll2 = random_world()
        rolls += roll2  # 串上擲幣結果
        if roll1 == roll2:
            if not is_in_a_row:  # 如果是第一次重複，才可以加count
                count += 1
                is_in_a_row = True  # 如果下一次又出現重複，就不會再加上count
        else:
            is_in_a_row = False
            roll1 = roll2
        if count == a:  # break the function if finished
            print(str(rolls))
            break


def random_world():
    """
    :return: string, the outcome of flipping coins
    """
    roll = r.choice(range(2))
    if roll == 1:
        return 'H'
    else:  # if roll == 0
        return 'T'


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
    main()
