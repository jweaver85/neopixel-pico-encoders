from unittest import TestCase

from mock import patch

from algos.aaa_tetris import run

from .test_utils import create_options


class TestTetris(TestCase):

    @patch('algos.aaa_tetris.render')
    def test_tetris(self, mock_render):
        options = create_options(num_pixels=100, step_size=1)
        run(options)
        mock_render.reset_mock()
        options.pixels.reset_mock()

        for i in range(options.num_pixels):
            run(options)
            self.assertEqual(len(options.colors), options.num_pixels)
            self.assertEqual(mock_render.call_count, 1)
            options.pixels.write.assert_called_once()
            options.pixels.reset_mock()
            mock_render.reset_mock()
