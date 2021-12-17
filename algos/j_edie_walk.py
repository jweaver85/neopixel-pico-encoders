from lib.utils import walk, render

COLOR01 = (0, 255, 0)
COLOR02 = (0, 125, 184)
COLOR03 = (190, 51, 214)


def run(options):
    if len(options.buffer) == 0:
        walk(COLOR01, COLOR02, options)
        walk(COLOR02, COLOR03, options)
        walk(COLOR03, COLOR02, options)
        walk(COLOR02, COLOR01, options)

    popped = options.buffer.pop()
    options.colors.push(popped)
    options.buffer.push(popped)

    render(options)
