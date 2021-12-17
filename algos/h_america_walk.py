from lib.utils import walk, render

RED = (255,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)


def run(options):
    if len(options.buffer) == 0:
        walk(RED, WHITE, options)
        walk(WHITE, BLUE, options)
        walk(BLUE, WHITE, options)
        walk(WHITE, RED, options)
        
    popped = options.buffer.pop()
    options.colors.push(popped)
    options.buffer.push(popped)
    render(options)


