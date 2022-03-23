"""
File: anagram.py
Name: Peter Lin
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 24

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm
import string

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop


def main():
    """
    TODO: find out the anagram!!!!!!!
    """
    print(f'Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        search = input(f'Find anagrams for: ')
        start = time.time()
        if search == '-1':
            break
        else:
            dictionary = read_dictionary()
            answer = find_anagrams(search, dictionary)
            number = len(answer)
            print(f'{number} anagrams: {answer}')
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    dictionary = {}
    str = string.ascii_lowercase  # 'abcdefg.....vwxyz'
    for alphabet in str:  # build up the index of dictionary
        dictionary[alphabet] = []
    with open(FILE, 'r') as d:
        for line in d:
            word = line.strip('\n')
            for alphabet in str:
                if word.startswith(alphabet) is True:
                    dictionary[alphabet].append(word)
                    break
    return dictionary


def find_anagrams(s, dictionary):
    """
    :param dictionary: dict, dictionary to lookup
    :param s: str, the word we input
    :return: list, all anagrams of the input
    """
    anagram_list = []
    length = len(s)
    lst = []
    for i in range(length):
        lst.append(s[i])
    print(f'Searching...')
    for ele in lst:
        ans_list = dictionary[ele]
        cur = lst.copy()
        cur.remove(ele)
        find_anagrams_helper(ele, cur, ans_list, length, anagram_list)
    return anagram_list


def find_anagrams_helper(capital, lst, ans_list, length, anagram_list):
    """
    :param capital: str, the capital word of the anagram
    :param lst: list, remaining alphabet we try to concatenate orderly to find out the anagram
    :param ans_list: list, the fitting candidate in dictionary
    :param length: int, the length of the anagram
    :param anagram_list: list, the anagram
    :return: None
    """
    ans_list_copy = ans_list.copy()
    anagram = capital
    for i in range(len(lst)):
        ele = lst[i]
        anagram += ele
        if has_prefix(anagram, ans_list) is not False:
            ans_list = has_prefix(anagram, ans_list)
            if len(anagram) == length:
                if anagram in ans_list:
                    if anagram not in anagram_list:
                        print(f'Found: {anagram}')
                        anagram_list.append(anagram)
                        print(f'Searching...')
            else:
                lst.remove(ele)
                find_anagrams_helper(anagram, lst, ans_list, length, anagram_list)
                # unchoose
                lst.insert(i, anagram[-1])
                anagram = anagram[:-1]
                ans_list = has_prefix(anagram, ans_list_copy)
        else:
            # Early stopping
            anagram = anagram[:-1]
            ans_list = has_prefix(anagram, ans_list_copy)


def has_prefix(sub_s, ans_list):
    """
    :param ans_list: list, the candidate of the anagram so far
    :param sub_s: str, the prefix of the anagram
    :return: lst or Boolean, list(True) or False
    """
    new_list = []
    for word in ans_list:
        if word.startswith(sub_s) is True:
            new_list.append(word)
    if not new_list:
        return False
    else:
        return new_list


if __name__ == '__main__':
    main()
