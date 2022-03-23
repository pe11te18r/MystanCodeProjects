from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
Name: 
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

"""
    Algorithm: go from (3,4) to (6,3), pick up the beeper, and back to (3,4) facing East by definite route
"""


def main():
    pick_the_paper()
    back()


def pick_the_paper():
    """
        pre-condition:(3,4) facing East w/o beeper
        post-condition:(6,3) facing West w/ beeper
    """
    go_down()
    for i in range(3): # from(3,3) to (6,3)
        move()
    turn_around()
    pick_beeper()


def go_down():
    """
        pre-condition:(3,4) facing East w/o beeper
        post-condition:(3,3) facing East w/o beeper
    """
    turn_right()
    move()
    turn_left()


def back():
    """
        pre-condition:(6,3) facing West w/ beeper
        post-condition:(3,4) facing East w/ beeper
    """
    for i in range(3): # from(6,3) to (3,3)
        move()
    go_up()
    put_beeper()


def go_up():
    """
        pre-condition:(3,3) facing West w/ beeper
        post-condition:(3,4) facing East w/ beeper
    """
    turn_right()
    move()
    turn_right()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
