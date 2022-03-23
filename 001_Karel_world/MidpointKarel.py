from karel.stanfordkarel import *

"""
File: MidpointKarel.py
Name: 
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


"""
    Algorithm: use beepers for the boundary, narrow down gradually and find the center of square of street 1.
"""

def main():
    define_the_border()
    while not on_beeper():
        narrowing()
    """
        while 的 No區間 表示已找到中心 收尾！
    """
    pick_beeper()
    turn_around()
    if front_is_clear(): # prevention for bumping into the wall
        move()
    pick_beeper() # pick up the beeper under the Karel
    put_beeper() # put the beeper above the Karel


def define_the_border():
    """
        pre-condition: at street 1, avenue 1, facing East
        post-condition: at street 1, avenue x, facing West, and the border is degined by the beepers.
        x= the right side of the square
    """
    put_beeper()
    while front_is_clear():
        move()
    """
        while 的 No區間 表示轉向
    """
    put_beeper()
    turn_around()
    if front_is_clear(): # prevention for bumping into the wall
        move()


def narrowing():
    """
        pre-condition: Beepers are at street 1 avenue x, and street 1 avenue y
        post-condition: Beepers at street 1 avenue (x+1), and street 1 avenue (y-1)
    """
    while not on_beeper():
        move()
    pick_beeper()
    turn_around()
    move()
    put_beeper()
    move()


def turn_around():
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
