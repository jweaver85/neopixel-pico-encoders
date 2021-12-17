from unittest import TestCase

from mock import patch

from algos.d_color_walk import run
from .test_utils import create_options


class TestColorWalk(TestCase):

    @patch('algos.d_color_walk.render')
    def test_color_walk(self, render):
        options = create_options(num_pixels=10, step_size=255)
        for i in range(options.num_pixels):
            run(options)
            self.assertEqual(len(options.colors), i+1)
            self.assertEqual(len(options.buffer), 0)

