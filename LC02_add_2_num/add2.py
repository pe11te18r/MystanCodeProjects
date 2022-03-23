"""
File: add2.py
Name: Peter Lin 20220308
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    #######################
    #                     #
    #        TODO:        #
    #                     #
    #######################
    python_l1 = []
    python_l2 = []

    cur_1 = l1
    while cur_1 is not None:
        python_l1.append(cur_1.val)
        cur_1 = cur_1.next

    cur_2 = l2
    while cur_2 is not None:
        python_l2.append(cur_2.val)
        cur_2 = cur_2.next

    num_1 = 0
    for i in range(len(python_l1)):
        digit_1 = python_l1[i]
        num_1 += digit_1 * (10 ** i)

    num_2 = 0
    for j in range(len(python_l2)):
        digit_2 = python_l2[j]
        num_2 += digit_2 * (10 ** j)

    ans = num_1 + num_2
    print(ans)

    ans_lst = []
    while ans > 9:
        x = ans % 10
        ans_lst.append(x)
        ans //= 10
    ans_lst.append(ans)
    print(ans_lst)

    ans_ll = ListNode(data=ans_lst[0])
    if len(ans_lst) > 1:
        for k in range(1, len(ans_lst)):
            node = ListNode(data=ans_lst[k])
            cur_ans = ans_ll
            while cur_ans.next is not None:
                cur_ans = cur_ans.next
            cur_ans.next = node
    return ans_ll


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
