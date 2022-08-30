from lib.utils import randColor, rand, render

"""
idea:
    pick a random index and populate it with a color
    options.stepsize should be used to determine the number of random colors initially?

    [R][0][G]
    [R][R][G]
    states are updated LTR (left to right) and either the next or previous color can win,
    it doesn't really matter

    needs to keep track of chosen colors

    recycle state:
    no changes were made (boolean changed)




states:
    [0][0][R][0][0][G][0][0][0][B][0][0] {R,G,B}
    [0][R][R][R][G][G][G][0][B][B][B][0]
    [R][R][R][R][G][G][G][G][B][B][B][B]
    [R][R][R][R][G][G][G][G][B][B][B][B] <- recycle state, pick new colors
    [R][X][R][R][G][G][G][Y][B][Z][B][B] {X,Y,Z}
    [X][X][X][R][G][G][Y][Y][Y][Z][Z][B]
    [X][X][X][R][G][Y][Y][Y][Y][Z][Z][Z]
    [X][X][X][X][Y][Y][Y][Y][Y][Z][Z][Z]
    [X][X][X][X][Y][Y][Y][Y][Y][Z][Z][Z] <- recycle state, pick new colors




"""
chosen_colors = set()


def pick_colors_and_set(options):
    num_seeds = 4  # TODO: make this configurable
    for _ in range(num_seeds):
        chosen_colors.add(randColor())

    for c in chosen_colors:
        index = rand(options.num_pixels)
        # print('inserting %s at index: %s' % (c, index))
        options.colors[index] = c

    render(options)
    
def calc_sleep(options):
    if options.step > 5:
        options.step = 5
    float_step = float(options.step)
    sleep_modifier = float(.01)  # (this is why we need sleep)
    value = float_step * sleep_modifier
    return value


def run(options):
    global chosen_colors
    updated = False

    while len(options.colors) < options.num_pixels:
        options.colors.push((0, 0, 0))

    if not len(chosen_colors):
        pick_colors_and_set(options)

    i = 0
    while i < options.num_pixels:
        color = options.colors[i]
        # print('chosen_colors: %s\ncolor: %s\ni: %s'%(chosen_colors, color, i))
        if color in chosen_colors:
            # check left
            left = i - 1
            right = i + 1
            if left >= 0 and options.colors[left] not in chosen_colors:
                options.colors[left] = color
                updated = True

            if right < options.num_pixels and options.colors[right] not in chosen_colors:
                options.colors[right] = color
                updated = True
                i = i + 1
        i = i + 1
    if not updated:
        chosen_colors.clear()
        calculated_sleep = calc_sleep(options)
        options.sleepytime = calculated_sleep

    render(options)
