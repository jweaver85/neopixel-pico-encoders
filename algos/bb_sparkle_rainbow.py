import time
from lib.utils import rand, randSelect, render

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


def calc_sleep(options):
    if options.step > 5:
        options.step = 5
    float_step = float(options.step)
    sleep_modifier = float(.01)  # (this is why we need sleep)
    value = float_step * sleep_modifier
    return value


def get_index(colors, item: tuple):
    i = 0
    while i < len(colors):
        if colors[i] == item:
            return i
        i += 1

    # we didn't find the item, so pick a random index to seed
    return rand(maximum=len(colors))


def run(options):
    global colors

    if len(options.colors) < options.num_pixels:
        options.colors.clear()
        options.pixels.fill((0, 0, 0))
        options.pixels.write()
        while len(options.colors) < options.num_pixels:
            rand_c = randSelect(colors)
            print(f'random color: {rand_c}')
            options.colors.push(rand_c)

    i = 0
    while i < options.num_pixels:
        strand_color = options.colors[i]
        # print(f'strand_color: {strand_color}')
        prev_val = get_index(colors, strand_color)
        # print(f'prev_index: {prev_val}')
        next_val = (prev_val + 1) % len(colors)
        # print(f'next_index: {next_val}')
        # print(f'next_color: {colors[next_val]}')
        options.colors[i] = colors[next_val]
        i += 1
    render(options)
    calculated_sleep = calc_sleep(options)
    options.sleepytime = calculated_sleep



