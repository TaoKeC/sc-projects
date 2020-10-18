"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
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
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
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
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    each_year_width = (width - GRAPH_MARGIN_SIZE) / len(YEARS)
    this_year_x = (each_year_width * year_index) + GRAPH_MARGIN_SIZE
    return this_year_x


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH,
                       GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT, width=LINE_WIDTH)
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i),
                           CANVAS_HEIGHT, width=LINE_WIDTH)
    for j in range(len(YEARS)):
        canvas.create_text(GRAPH_MARGIN_SIZE + (CANVAS_WIDTH - GRAPH_MARGIN_SIZE) / len(YEARS) * j + TEXT_DX,
                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[j], anchor=tkinter.NW)


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

    # Write your code below this line
    #################################
    y = (CANVAS_HEIGHT-(2*GRAPH_MARGIN_SIZE)) / 1000
    for j in range(len(lookup_names)):
        if lookup_names[j] in name_data:
            for k in range(len(YEARS)-1):
                ye = str(YEARS[k])
                ye_1 = str(YEARS[k + 1])
                ye_2 = str(YEARS[k-1])
                if str(YEARS[k]) in name_data[lookup_names[j]]:
                    if str(YEARS[k + 1]) in name_data[lookup_names[j]]:
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, k),
                                           GRAPH_MARGIN_SIZE + y * int((name_data[lookup_names[j]][ye]))
                                           , get_x_coordinate(CANVAS_WIDTH, k+1),
                                           GRAPH_MARGIN_SIZE + y * int(name_data[lookup_names[j]][ye_1]),
                                           width=LINE_WIDTH, fill=COLORS[j % len(COLORS)])
                        # this if condition responsible for the first year(1900)'s text
                        if k == 1:
                            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, k-1) + TEXT_DX,
                                               GRAPH_MARGIN_SIZE+y * int((name_data[lookup_names[j]][ye_2])),
                                               text=f'{lookup_names[j]} {name_data[lookup_names[j]][ye_2]}',
                                               anchor=tkinter.SW, fill=COLORS[j % len(COLORS)]
                                               )
                        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, k+1) + TEXT_DX,
                                           GRAPH_MARGIN_SIZE+y * int(name_data[lookup_names[j]][ye_1]),
                                           text=f'{lookup_names[j]} {name_data[lookup_names[j]][ye_1]}',
                                           anchor=tkinter.SW, fill=COLORS[j % len(COLORS)])
                    else:
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, k),
                                           GRAPH_MARGIN_SIZE + y * int((name_data[lookup_names[j]][ye]))
                                           , get_x_coordinate(CANVAS_WIDTH, k+1),
                                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH,
                                           fill=COLORS[j % len(COLORS)])
                        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, k + 1) + TEXT_DX,
                                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           text=lookup_names[j]+' *',
                                           anchor=tkinter.SW, fill=COLORS[j % len(COLORS)])

                else:
                    if str(YEARS[k + 1]) in name_data[lookup_names[j]]:
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, k), CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           get_x_coordinate(CANVAS_WIDTH, k+1),
                                           GRAPH_MARGIN_SIZE+y * int(name_data[lookup_names[j]][ye_1]),
                                           width=LINE_WIDTH, fill=COLORS[j % len(COLORS)])
                        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, k+1)+TEXT_DX,
                                           GRAPH_MARGIN_SIZE+y * int(name_data[lookup_names[j]][ye_1]),
                                           text=f'{lookup_names[j]} {name_data[lookup_names[j]][ye_1]}',
                                           anchor=tkinter.SW, fill=COLORS[j % len(COLORS)])
                    else:
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, k), CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           get_x_coordinate(CANVAS_WIDTH, k+1),
                                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH,
                                           fill=COLORS[j % len(COLORS)])
                        # this if condition responsible for the first year(1900)'s text
                        if k == 1:
                            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, k-1) + TEXT_DX,
                                               CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                               text=lookup_names[j]+' *',
                                               anchor=tkinter.SW, fill=COLORS[j % len(COLORS)]
                                               )
                        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, k+1)+TEXT_DX,
                                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           text=lookup_names[j]+' *',
                                           anchor=tkinter.SW, fill=COLORS[j % len(COLORS)])


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
