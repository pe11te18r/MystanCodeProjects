from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
Name: 
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

"""
    Algorithm: check and repair, go down, and repeat or stop. 
               Solution to OBOB: do the whole process once and use while to repeat or stop.
"""


def main(): # the whole process of repair
    check_and_repair()
    go_down()
    next_or_stop()


def check_and_repair():
    """
    pre-condition:at the bottom of the pillar facing East, repair remained.
    post-condition:on the top of the pillar facing South, repair completed.
    """
    turn_left() # facing North
    while front_is_clear(): # if front is clear, check the beeper and move forward
        if not on_beeper():
            put_beeper()
        move()
    if not on_beeper(): # if front is not clear,check the beeper and turn around
        put_beeper()
    turn_around()
# use while function rather if function for unknown length of the pillar.


def go_down():
    """
        pre-condition:on the top of the pillar facing South.
        post-condition:at the bottom of pillar facing East.
    """
    while front_is_clear():
        move()
    turn_left()


def next_or_stop():
    """
        repeat the repair or stop by while for indefinite loop
    """
    while front_is_clear():
        move_to_next()
        check_and_repair()
        go_down()


def move_to_next(): # the fixed interval
    for i in range(4):
        move()


def turn_around():
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
