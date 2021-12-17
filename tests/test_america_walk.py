from unittest import TestCase

from mock import patch

from algos.h_america_walk import run
from .test_utils import create_options


class TestAmericaWalk(TestCase):

    @patch('algos.h_america_walk.render')
    def test_america_walk(self, render):
        options = create_options(num_pixels=3, step_size=255)

        for i in range(3):
            run(options)
            self.assertEqual(len(options.buffer), 4)
            self.assertEqual(len(options.colors), i + 1)
