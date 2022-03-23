"""
File: largest_digit.py
Name: Peter Lin 20220222
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
    print(find_largest_digit(12345))  # 5
    print(find_largest_digit(281))  # 8
    print(find_largest_digit(6))  # 6
    print(find_largest_digit(-111))  # 1
    print(find_largest_digit(-9453))  # 9


def find_largest_digit(n):
    """
    :param n:
    :return:
    """
    if n < 0:
        n = n * -1
    cur = 0
    ans = find_largest_digit_helper(n, cur)
    return ans


def find_largest_digit_helper(n, cur):
    if n < 10:
        if n > cur:
            cur = n
        return cur
    else:
        a = n % 10
        if a > cur:
            cur = a
        n //= 10
        return find_largest_digit_helper(n, cur)


if __name__ == '__main__':
    main()
