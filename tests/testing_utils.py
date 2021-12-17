from mock import Mock

from lib import Options
from lib.queue import queue


def create_options(
        num_pixels=60,
        step_size=1,
        brightness=.1,
        sleepytime=.01,
        neopixels_mock=Mock(),
        algorithm='rainbowwalk'
):
    return Options(
        num_pixels,  # pixels in this LED strip
        step_size,  # step size for walks
        brightness,  # brightness
        sleepytime,  # sleepytime (unused?)
        neopixels_mock,  # neopixel object
        queue([], num_pixels),  # colors to be rendered (buffer 1)
        queue([], None),  # buffer (buffer 2) to consumed by buffer 1
        algorithm,  # initial color effect to start TODO: move this to onboard storage
        False  # debug mode (for logging purposes
    )