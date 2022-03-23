from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
Name: 
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

"""    
    Algorithm: 
        Define one cycle as two streets
            If the rectangle has only one avenue, fill the avenue.(run the function "fill_one_avenue")
            If the rectangle has more than one avenue, fill the streets by orders.(run the function "fill_street")
         
         For the rectangle having more than one avenue, we divide into two groups by the amount of avenue:
            odd avenue and even avenue
            (the detail algorithm narrated below.)     
"""

def main():
   put_beeper() # the beeper at start
   if front_is_clear():
       fill_street()
   else: # for one avenue only
       turn_left()
       fill_one_avenue()
"""
    依照此world總共有的avenue數量來區分兩種不同的填寫方式：分為奇數個avenue 與 偶數個avenue
    
    while function 的 Yes 區間 ： 
      if 區間： fill the first street or the other streets in the rectangle having even avenues.
      else 區間：street is completed, move to the next street or stop.
      (the cycle of even avenue: move from East to West in the first street, and from West to East in the second street)
      偶數cycle的第一行就是指第1,3,5,7行（including if 區間已填好的 the first street）
    No 區間：for the rectangle having odd avenues.
      (the cycle of odd avenue: move from West to East in the first street, and from East to West in the second street)
      奇數cycle的第一行是指第2,4,6,8行（excluding if 區間已填好的 the first street）
"""
def fill_street():
    while front_is_clear(): # even avenue cycle ＆ first street :step on beeper, move → move → put
        move()
        if front_is_clear():
            move()
            put_beeper()
        else: # street 已填滿
            turn_left()
            if not front_is_clear(): # arrive at the top street
                turn_right() # 跳回到while function才會接到front is not clear往下走
            else: # move to the next street
                move()
                if not on_beeper(): # prepare for the next street, fill from West to East
                    # pre-condition: street x, avenue y facing North w/o the beeper
                    # post-condition: street x,avenue y facing West w/ the beeper
                    turn_left()
                    put_beeper()
                else: # complete one cycle
                    #  pre-condition: street n, avenue 1 facing South w/ the old beeper
                    #  post-condition: street n+2, avenue 1 facing East w/ the new beeper
                    turn_around()
                    move()
                    if front_is_clear(): # if any, move to next start w/ new beeper
                        move()
                        turn_right()
                        put_beeper()
    turn_left() # in order to check whether there is any street unfilled or not
    if front_is_clear(): # odd avenue, more than one street
        while front_is_clear(): # move to next street
            move()
            turn_left()
            while front_is_clear(): # odd avenue cycle：step on nothing, move → put → move
                move()
                put_beeper()
                if front_is_clear():
                    move()
                else: # new street completed
                    pass
            turn_left() # return to the start
            move()
            if on_beeper(): # move to next cycle
                turn_around()
                move()
                if front_is_clear(): # start of the new cycle
                    move()
                    turn_right()
                    put_beeper()
                    while front_is_clear(): # first street：step on beeper, move → move → put
                        move()
                        if front_is_clear():
                            move()
                            put_beeper()
                    turn_left()
    else: # for one street only
        pass


def fill_one_avenue():
    """
        pre-condition: at start, facing North
        post-condition: finish one avenue, facing North
    """
    while front_is_clear():
            if front_is_clear():
                move()
                if front_is_clear():
                    move()
                    put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
