from lib.utils import translate, rand


def render(index, options):
    options.pixels[index] = options.colors[index]


def run(options):
    while len(options.colors) < options.num_pixels:
        rand_c = rand()
        options.colors.push((rand_c, rand_c, rand_c))

    i = 0
    step = options.step
    for c in options.colors:
        if c == (0, 0, 0):
            rand_c = rand()
            options.colors[i] = (rand_c, rand_c, rand_c)
        else:
            c1 = translate(c[0], 0, step)
            c2 = translate(c[1], 0, step)
            c3 = translate(c[2], 0, step)
            options.colors[i] = (c1, c2, c3)
        render(i, options)
        i = i + 1
    options.pixels.write()
