"""
File: boggle.py
Name: Peter Lin 20220309
----------------------------------------
TODO:
"""

import time
import string

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    """
    TODO:
    """
    start = 0
    row_1 = input(f'1 row of letters: ')
    alphabet_1 = row_1.split(' ')
    if valid_data(alphabet_1) is not False:
        alphabet_1 = valid_data(alphabet_1)
        row_2 = input(f'2 row of letters: ')
        alphabet_2 = row_2.split(' ')
        if valid_data(alphabet_2) is not False:
            alphabet_2 = valid_data(alphabet_2)
            row_3 = input(f'3 row of letters: ')
            alphabet_3 = row_3.split(' ')
            if valid_data(alphabet_3) is not False:
                alphabet_3 = valid_data(alphabet_3)
                row_4 = input(f'4 row of letters: ')
                alphabet_4 = row_4.split()
                if valid_data(alphabet_4) is not False:
                    alphabet_4 = valid_data(alphabet_4)
                    start = time.time()
                    final_count = boggle(alphabet_1, alphabet_2, alphabet_3, alphabet_4)
                    print(f'There are {final_count} words in total.')
                else:
                    print('Illegal input')
            else:
                print('Illegal input')
        else:
            print('Illegal input')
    else:
        print('Illegal input')

    ####################
    #                  #
    #       TODO:      #
    #                  #
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def valid_data(lst):
    for i in range(len(lst)):
        ele = lst[i]
        if ele.isalpha() is True:
            if len(ele) == 1:
                ele = ele.lower()
                lst[i] = ele
            else:
                return False
    return lst


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    dictionary = {}
    index_str = string.ascii_lowercase  # 'abcdefg.....vwxyz'
    for alphabet in index_str:  # build up the index of dictionary
        dictionary[alphabet] = []
    with open(FILE, 'r') as d:
        for line in d:
            word = line.strip('\n')
            if len(word) >= 4:
                for alphabet in index_str:
                    if word.startswith(alphabet) is True:
                        dictionary[alphabet].append(word)
                        break
    return dictionary


def boggle(lst_1, lst_2, lst_3, lst_4):
    answer_lst = []
    array_2d = [lst_1, lst_2, lst_3, lst_4]
    dictionary = read_dictionary()
    for i in range(4):
        for j in range(4):
            prefix = array_2d[i][j]
            small_dic_list = dictionary[prefix]  # 資料格式為list
            used_list = [(i, j)]
            capital_ans_lst = boggle_recursion(i, j, array_2d, prefix, small_dic_list, [], used_list, answer_lst)
            for word in capital_ans_lst:
                answer_lst.append(word)
    count = len(answer_lst)
    return count


def boggle_recursion(x, y, array, cur, dic_list, ans_lst, used_list, all_answerlst):
    dic_list_copy = dic_list.copy()  # unchoose 字典退格要用的備份檔案
    for k in range(-1, 2):
        for m in range(-1, 2):
            if 0 <= x + k <= 3 and 0 <= y + m <= 3:
                if (x + k, y + m) not in used_list:
                    next_alphabet = array[x + k][y + m]
                    cur += next_alphabet
                    if has_prefix(cur, dic_list_copy) is not False:
                        used_list.append((x + k, y + m))
                        dic_list = has_prefix(cur, dic_list)
                        if cur in dic_list:
                            if cur not in ans_lst and cur not in all_answerlst:
                                print(f'Found \"{cur}\"')
                                ans_lst.append(cur)
                                boggle_recursion(x + k, y + m, array, cur, dic_list, ans_lst, used_list, all_answerlst)
                                # unchoose
                                cur = cur[:-1]
                                dic_list = has_prefix(cur, dic_list_copy)
                                used_list.pop()
                            else:
                                boggle_recursion(x + k, y + m, array, cur, dic_list, ans_lst, used_list, all_answerlst)
                                # unchoose
                                cur = cur[:-1]
                                dic_list = has_prefix(cur, dic_list_copy)
                                used_list.pop()
                        else:
                            boggle_recursion(x + k, y + m, array, cur, dic_list, ans_lst, used_list, all_answerlst)
                            # unchoose
                            cur = cur[:-1]
                            dic_list = has_prefix(cur, dic_list_copy)
                            used_list.pop()
                    else:
                        cur = cur[:-1]
                        dic_list = has_prefix(cur, dic_list_copy)

    return ans_lst


def has_prefix(sub_s, dic_list):
    """
    :param dic_list:
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    new_list = []
    for word in dic_list:
        if word.startswith(sub_s) is True:
            new_list.append(word)
    if not new_list:
        return False
    else:
        return new_list


if __name__ == '__main__':
    main()
