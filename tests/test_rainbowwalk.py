from unittest import TestCase

from mock import patch

from algos.f_rainbow_walk import run
from .test_utils import create_options


class TestRainbowwalk(TestCase):

    @patch('algos.f_rainbow_walk.render')
    def test_rainbowwalk(self, render):
        options = create_options(num_pixels=10, step_size=255)

        for i in range(options.num_pixels):
            run(options)
            self.assertEqual(len(options.buffer), 10)
            self.assertEqual(len(options.colors), i+1)
