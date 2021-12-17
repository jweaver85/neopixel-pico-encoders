from unittest import TestCase

from mock import patch

from algos.k_split_edie_walk import run
from .test_utils import create_options


class TestSplitEdieWalk(TestCase):

    @patch('algos.k_split_edie_walk.render')
    def test_split_edie_walk(self, render):
        options = create_options(num_pixels=10, step_size=255)
        run(options)
