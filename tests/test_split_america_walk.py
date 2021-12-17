from unittest import TestCase

from mock import patch

from algos.g_split_rainbow_walk import run
from .test_utils import create_options


class TestSplitAmericaWalk(TestCase):

    @patch('algos.g_split_rainbow_walk.render')
    def test_split_america_walk(self, render):
        options = create_options(num_pixels=10, step_size=255)
        run(options)

        # for i in range(options.num_pixels):
        #     split_america_walk(options)
        #     print('iteration: %s, len(colors): %s' % ((i+1), len(options.colors)))
        #     self.assertEqual(len(options.buffer), 4)
        #     self.assertEqual(len(options.colors), (2*i) + 1)