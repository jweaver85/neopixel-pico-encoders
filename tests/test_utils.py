from unittest import TestCase
from mock import Mock

from lib.options import Options
from lib.queue import queue
from lib.utils import render, rand, randColor, translate


class TestUtils(TestCase):

    def test_RenderNoErros(self):
        neopixel = Mock()
        options = create_options(neopixels_mock=neopixel)
        render(options)

    def test_Rand(self):
        for iteration in range(100000):
            value = rand()
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 255)

    def testRandColor(self):
        for iteration in range(100000):
            color = randColor()
            # X
            self.assertGreaterEqual(color[0], 0)
            self.assertLessEqual(color[0], 255)
            # Y
            self.assertGreaterEqual(color[1], 0)
            self.assertLessEqual(color[1], 255)
            # Z
            self.assertGreaterEqual(color[2], 0)
            self.assertLessEqual(color[2], 255)

    def testTranslateStartEqualToEnd(self):
        start = end = rand()
        step_size = rand()
        retval = translate(start, end, step_size)
        self.assertEqual(retval, end)
    #
    # def testTranslateStartLargerThanEndReturnsEnd(self):
    #     start = end = rand()
    #     start += 1
    #     step_size = -1
    #     retval = translate(start, end, step_size)
    #     print('start: %s, end: %s, stepsize: %s, retval: %s' % (start, end, step_size, retval))
    #     self.assertEqual(retval, end)
    #
    # def testTranslateStartLargerThanEnd(self):
    #     start = end = rand()
    #     start += 1
    #     step_size = rand()
    #     retval = translate(start, end, step_size)
    #     print('start: %s, end: %s, stepsize: %s, retval: %s' % (start, end, step_size, retval))
    #     self.assertEqual(retval, end)


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
        False  # debug mode (for logging purposes
    )