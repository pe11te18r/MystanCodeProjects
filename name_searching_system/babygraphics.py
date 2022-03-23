"""
File: babygraphics.py
Name: Peter Lin 20220209
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    num_year = len(YEARS)
    x_origin = GRAPH_MARGIN_SIZE
    line_length = width - 2 * GRAPH_MARGIN_SIZE
    x_coordinate = x_origin + year_index * (line_length / num_year)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    luq_x = GRAPH_MARGIN_SIZE
    luq_y = GRAPH_MARGIN_SIZE
    llq_x = GRAPH_MARGIN_SIZE
    llq_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

    ruq_x = CANVAS_WIDTH - GRAPH_MARGIN_SIZE
    ruq_y = GRAPH_MARGIN_SIZE
    rlq_x = CANVAS_WIDTH - GRAPH_MARGIN_SIZE
    rlq_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

    canvas.create_line(luq_x, 0, llq_x, CANVAS_HEIGHT)  # Y-axis
    canvas.create_line(llq_x, llq_y, rlq_x, rlq_y)  # X-axis
    canvas.create_line(luq_x, luq_y, ruq_x, ruq_y)  # X-axis (upper)

    for i in range(len(YEARS)):
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_coordinate, 0, x_coordinate, CANVAS_HEIGHT)
        canvas.create_text(x_coordinate, CANVAS_HEIGHT, text=YEARS[i], anchor=tkinter.SW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # ----- Write your code below this line ----- #
    color_index = -1
    for name in lookup_names:
        color_index += 1  # color的處理: 超過len(color)重新循環
        if color_index == len(COLORS):
            color_index = 0
        dic = {}
        for year, rank in name_data[name].items():  # dic={year:[rank,x,y]}
            index = find_index(YEARS, int(year))  # 要注意！name_data裡面的東西格式都是 str
            x = get_x_coordinate(CANVAS_WIDTH, index)
            rank = name_data[name][year]
            y = (GRAPH_MARGIN_SIZE - 1) + (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE) / 1000 * int(rank)
            dic[int(year)] = [rank, x, y]
        for ele in YEARS:  # 把超過一千名的年份資料加入dic
            ind = find_index(YEARS, ele)
            if ele not in dic:
                dic[ele] = ['*', get_x_coordinate(CANVAS_WIDTH, ind), CANVAS_HEIGHT - GRAPH_MARGIN_SIZE]
        # sorted(dic)  # dic不能這樣排序，只有list可以
        coordination_lst = []
        for key in YEARS:  # coordination_lst=[x1,y1,x2,y2,x3,y3,...]
            coordination_lst.append(dic[key][1])
            coordination_lst.append(dic[key][2])
            canvas.create_text(dic[key][1], dic[key][2], text=f'{name} {dic[key][0]}', anchor=tkinter.SW,
                               fill=COLORS[color_index])  # 顏色指令是fill 不是color
        for i in range(len(coordination_lst) // 2 - 1):
            canvas.create_line(coordination_lst[2 * i], coordination_lst[2 * i + 1], coordination_lst[2 * i + 2],
                               coordination_lst[2 * i + 3], fill=COLORS[color_index], width=LINE_WIDTH)


def find_index(lst, year):
    """
    Find out the index of the year in the list.

    Args:
        lst (List[int]): A list of the years , the aims we try to figure out the corresponding rank, sorted by order
        year (int): The year we want to find out the index of the lst

    Returns:
        i (int): the index of the year in the lst YEARS
    """
    for i in range(len(lst)):
        if lst[i] == year:
            return i


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
