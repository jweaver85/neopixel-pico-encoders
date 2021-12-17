from unittest import TestCase

from mock import patch

from algos.j_edie_walk import (
    COLOR01, COLOR02, COLOR03, run
)
from .test_utils import create_options


class TestEdieWalk(TestCase):

    @patch('algos.j_edie_walk.render')
    def test_edie_walk_full_iteration(self, render):
        options = create_options(num_pixels=3, step_size=255)
        run(options)
        render.assert_called_once_with(options)

        # C1 -> C2, C2 -> C3, C3 -> C4, C4 -> C1
        self.assertEqual(len(options.buffer), 4)
        self.assertEqual(len(options.colors), 1)
        self.assertListEqual(list(options.colors), [COLOR02])

        run(options)
        self.assertEqual(len(options.buffer), 4)
        self.assertEqual(len(options.colors), 2)
        self.assertListEqual(list(options.colors), [COLOR03, COLOR02])

        run(options)
        self.assertEqual(len(options.buffer), 4)
        self.assertEqual(len(options.colors), 3)
        self.assertListEqual(list(options.colors), [COLOR02, COLOR03, COLOR02])

        run(options)
        self.assertEqual(len(options.buffer), 4)
        self.assertEqual(len(options.colors), 3)
        self.assertListEqual(list(options.colors), [COLOR01, COLOR02, COLOR03])

