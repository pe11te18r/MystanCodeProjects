"""
File: similarity.py
Name: Peter Lin 20211005
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    Algorithm: use a variety "ratio" to represent the highest similarity, and "box" to represent the index
                of the upper limit of the most similar sequence, and print the substring out!
    """
    template = str(input('Please give me a DNA sequence to search: '))
    fragment = str(input('What DNA sequence would you like to match? '))
    homology = similarity(template, fragment)
    print('The best match is ' + homology)


def similarity(a, b):
    """
    :param a: str, template sequence
    :param b: str, fragment sequence
    :return: str, the most similar substring
    """
    a = a.upper()  # for case insensitive
    b = b.upper()
    ratio = 0  # 儲存符合配對的code數（極值）
    ans = ''   # 儲存substring的空字串
    for i in range(len(a)-len(b)+1):  # len(a)-len(b)+1 表示要進行配對的次數
        sim = 0  # 儲存本substring符合配對的code數
        for frag in b:  # 每次配對都需要配fragment的字元次數
            ch = a[i]
            if ch == frag:  # 配對成功 sim +1
                sim += 1
            i += 1  # 配對完就前進下一碼
        if sim > ratio:  # 如果找到極值，把極值的配對率與上限值做更新
            ratio = sim
            box = i
    ans += a[(box-len(b)):box]  # 輸出substring
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
