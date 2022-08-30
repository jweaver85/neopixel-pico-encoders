import board
import neopixel
import digitalio
import rotaryio
import analogio
import timer
import os
import sys

from lib.options import Options
from lib.queue import queue

# dynamic imports!
algos = list([])
files = os.listdir('algos')
modules = [f[:-3] for f in files if f.endswith(".py") and f[0] != "_"]
for module in modules:
    if module == 'a_mic':
        continue
    __import__('algos.'+ module, 'algos.'+ module)
    algos.append(sys.modules["algos." + module])

# Update this to match the number of NeoPixel LEDs connected to your board.
# TODO: buy another strip and see if the board can drive more than on strip (shared colors and buffers!)
num_pixels = 60
options = Options(
    num_pixels,  # pixels in this LED strip
    1,  # step size for walks
    0.01,  # brightness
    0.01,  # sleepytime (unused?)
    neopixel.NeoPixel(board.GP0, num_pixels),  # neopixel object
    queue([], num_pixels),  # colors to be rendered (buffer 1)
    queue([], None),  # buffer (buffer 2) to consumed by buffer 1
    False  # debug mode (for logging purposes
)
options.pixels.brightness = options.brightness
options.pixels.auto_write = False

algo_index = 0

step_enc = rotaryio.IncrementalEncoder(board.GP16, board.GP17)
step_enc_prev = -1

brightness_enc = rotaryio.IncrementalEncoder(board.GP19, board.GP20)
brightness_enc_prev = -1

algo_button = digitalio.DigitalInOut(board.GP18)
algo_button.switch_to_input(pull=digitalio.Pull.DOWN)
algo_button_prev = False

microphone = analogio.AnalogIn(board.GP27)

def updateAlgorithm():
    global algo_button
    global algo_button_prev
    global algo_index
    global algos

    if algo_button.value and algo_button.value != algo_button_prev:
        algo_button_prev = algo_button.value
        new_algo_index = (algo_index + 1) % (len(algos) + 1)

        if algo_index != new_algo_index:
            options.buffer.clear()
            options.sleepytime = 0

        algo_index = new_algo_index

        if options.debug: print("algo_button pressed! Current algo_index: " + str(algo_index))

    if not algo_button.value:
        algo_button_prev = algo_button.value

    return algo_index


def updateBrightness():
    global brightness_enc
    global brightness_enc_prev
    global options
    global microphone

    # print((microphone.value,))
    position = brightness_enc.position
    if position != brightness_enc_prev:
        if position > brightness_enc_prev:
            calculated = float(options.brightness + 0.05)
            brightness_enc_prev = position
            if calculated < 1.01:
                options.brightness = calculated
        else:
            calculated = float(options.brightness - 0.05)
            brightness_enc_prev = position
            if calculated > 0:
                options.brightness = calculated
            if calculated < 0:
                options.brightness = .01
    return options.brightness


def updateStep():
    global step_enc
    global step_enc_prev
    global options

    position = step_enc.position
    if position != step_enc_prev:
        options.buffer.clear()
        if position > step_enc_prev:
            calculated = float(options.step + 1)
            step_enc_prev = position
            if calculated < 128:
                options.step = calculated
        else:
            calculated = float(options.step - 1)
            step_enc_prev = position
            if calculated > 0:
                options.step = calculated
    return options.step


async def do_work():  # setup == "do_work"
    global algos
    global algo_index
    global options

    updateAlgorithm()
    options.brightness = updateBrightness()
    options.step = updateStep()

    if algo_index == len(algos):
        options.pixels.fill((0, 0, 0))
        options.pixels.write()
    else:
        options.pixels.brightness = options.brightness
        algos[algo_index].run(options)


def setup():  # namespace == "setup"
    timer.schedule(hz=100, coroutine_function=do_work)


if __name__ == '__main__':
    setup()
    timer.run()
