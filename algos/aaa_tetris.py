import time

from lib.utils import randSelect, render

"""
idea:
    tetris colors, each color has a fixed width. 
    starting LTR, randomly pick a color and shift that color right until it hits the end or the last color.
"""
BLACK = (0, 0, 0)
colors = [
    {
        'width': 2,  # Cyan
        'value': (0, 255, 255)
    },
    {
        'width': 3,  # Yellow
        'value': (255, 255, 0)
    },
    {
        'width': 4,  # Purple
        'value': (128, 0, 128)
    },
    {
        'width': 5,  # Green
        'value': (0, 255, 0)
    },
    {
        'width': 6,  # Red
        'value': (255, 0, 0)
    },
    {
        'width': 7,  # Blue
        'value': (0, 0, 255)
    },
    {
        'width': 8,  # Orange
        'value': (255, 127, 0)
    },
]
chosen_color = None
reset = False


def continue_reset(strand_colors: list):
    retval = any(color['value'] in strand_colors for color in colors)
    return retval


def check_for_score(color: dict, options, start: int, end: int):
    lookahead = end + 1

    # if match is found blink them three times, and black them out
    if lookahead < len(options.colors) and color['value'] == options.colors[lookahead]:
        end += color['width']

        iteration = 0
        while iteration < 10:
            i = start
            iteration += 1
            while i < end:
                options.colors[i] = color['value'] if options.colors[i] == BLACK else BLACK
                i += 1
            render(options)
            time.sleep(.1)

        i = start
        while i < end:
            options.colors[i] = BLACK
            i += 1
        render(options)


def run(options):
    global colors
    global chosen_color
    global reset

    while len(options.colors) < options.num_pixels:
        options.colors.push(BLACK)

    if reset:
        options.colors.push(BLACK)
        chosen_color = None
        reset = continue_reset(options.colors)

    elif not chosen_color:
        chosen_color = randSelect(colors)
        i = 0
        while i < chosen_color['width'] and options.colors[i] is BLACK:
            options.colors[i] = chosen_color['value']
            i += 1
    else:
        start = 0
        while options.colors[start] == BLACK:
            start += 1

        end = start + chosen_color['width']

        if end == options.num_pixels or options.colors[end] != BLACK:
            check_for_score(chosen_color, options, start, end)
            chosen_color = None
        else:
            color = options.colors[start]
            options.colors[start] = BLACK
            options.colors[end] = color

    if BLACK not in options.colors:
        reset = True

    render(options)
