"""
File: hangman.py
Name: Peter Lin 20211007
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Algorithm:先把首次猜謎介面做出來，開始猜之後進入hanging進行猜謎
    """
    hangman_printing(N_TURNS)
    print('The word looks like: ', end='')
    ans = random_word()
    length = len(ans)
    empty_string = ''
    for i in range(length):
        empty_string += '-'
    print(empty_string)
    print('You have ' + str(N_TURNS) + ' guesses left.')
    guess = input('Your guess: ')
    check = len(guess)
    while not guess.isalpha() or check != 1:  # 邊界條件設定，篩選不符合格式的輸入格式
        print('illegal format.')
        guess = input('Your guess: ')
        check = len(guess)
    guess = guess.upper()  # case-insensitivity
    hanging(guess, length, ans, N_TURNS, empty_string)
    print('The word was: ' + ans)  # 無論對錯最後都要公佈答案


def hangman_printing(lives):
    print('========')
    if lives == N_TURNS:
        for i in range(6):
            print('|')
    elif lives == N_TURNS - 1:
        print('|    |')
        for i in range(5):
            print('|')
    elif lives == N_TURNS - 2:
        print('|    |')
        print('|   ( )')
        for i in range(4):
            print('|')
    elif lives == N_TURNS - 3:
        print('|    |')
        print('|   ( )')
        for i in range(2):
            print('|    #')
        for i in range(2):
            print('|')
    elif lives == N_TURNS - 4:
        print('|    |')
        print('|   ( )')
        print('|  ~ # ~')
        print('|    #')
        for i in range(2):
            print('|')
    elif lives == N_TURNS - 5:
        print('|    |')
        print('|   ( )')
        print('|  ~ # ~')
        print('|    #')
        print('|   / \\ ')
        print('|')
    elif lives == N_TURNS - 6:
        print('|    |')
        print('|  (0.0)')
        print('|  ~ # ~')
        print('|    #')
        print('|   / \\ ')
        print('|')
    else:
        print('|    |')
        print('|   (X)')
        print('|  ~ # ~')
        print('|    #')
        print('|   / \\ ')
        print('|   Lose')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def hanging(a, b, c, d, e):
    """
    :param a: str, 1 letter only
    :param b: int, the length of the answer
    :param c: str, the answer
    :param d: int, constant
    :param e: str, a string of '-'
    """
    total = 0  # 統計已經猜到的總字元數
    storage = e  # 目前的猜題狀況
    while True:
        now = ''  # 每次重新比對的空字串
        count = 0  # 本次猜的字在這個單字裡面出現次數
        for j in range(b):
            template1 = storage[j]
            template = c[j]
            if template == a:  # 在此index有本次猜的那個字：串上字串，count+1
                now += a
                count += 1
                if a != template1:  # 如果說本次猜這個字是之前還沒猜過的字，表示多猜到一個！加上總字元數統計
                    total += 1
            elif template == template1:  # 本次沒猜到，但之前猜對的字，就把它串上去
                now += template1
            else:  # 本次猜錯，之前也沒猜到，串上‘-’
                now += '-'
        if count == 0:  # 本次猜錯，命少一條
            print('There is no ' + a + '\'s in the word.')
            d -= 1
        else:  # 本次答對
            print('You are correct!')
        if total == b:  # 總字元統計數=字元長度 全部猜完！跳出猜題迴圈！
            print('You win!!')
            break
        elif d == 0:  # 機會用完死掉了，跳出猜題迴圈
            hangman_printing(d)
            print('You are completely hung : (')
            break
        else:
            hangman_printing(d)
            print('The word looks like: ' + now)
            storage = now  # 更新猜題狀況
            print('You have ' + str(d) + ' guesses left.')
            a = input('Your guess: ')  # 重新猜題
            check = len(a)
            while not a.isalpha() or check != 1:  # 邊界條件設定
                print('illegal format.')
                a = input('Your guess: ')
                check = len(a)
            a = a.upper()  # case-insensitivity


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
