from lib.utils import randSelect, render

COLOR01 = (255, 0, 0)
COLOR02 = (255, 85, 0)
COLOR03 = (255, 230, 0)
COLOR04 = (0, 255, 0)
COLOR05 = (0, 255, 68)
COLOR06 = (0, 255, 208)
COLOR07 = (0, 110, 255)
COLOR08 = (0, 0, 255)
COLOR09 = (157, 0, 255)
COLOR10 = (255, 0, 200)

colors = [
    COLOR01,
    COLOR02,
    COLOR03,
    COLOR04,
    COLOR05,
    COLOR06,
    COLOR07,
    COLOR08,
    COLOR09,
    COLOR10,
]


def get_index(item):
    global colors
    i = 0
    while i < len(colors):
        if colors[i] == item:
            return i
        i += 1


def run(options):
    global colors
    while len(options.colors) < options.num_pixels:
        options.colors.push(randSelect(colors))

    i = 0
    while i < options.num_pixels:
        strand_color = options.colors[i]
        prev_val = get_index(strand_color)
        next_val = (prev_val + 1) % len(colors)
        options.colors[i] = colors[next_val]
        i += 1
    render(options)
