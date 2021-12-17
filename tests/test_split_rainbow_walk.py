from unittest import TestCase

from mock import patch

from algos.g_split_rainbow_walk import run
from .test_utils import create_options


class TestSplitRainbowWalk(TestCase):

    @patch('algos.g_split_rainbow_walk.render')
    def test_split_rainbow_walk(self, render):
        options = create_options(num_pixels=10, step_size=255)
        run(options)