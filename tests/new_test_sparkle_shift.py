from unittest import TestCase

from mock import patch

from algos.n_sparkle_shift import run, render

from .test_utils import create_options


class TestSparkleShift(TestCase):

    @patch('algos.n_sparkle_shift.render')
    def test_sparkle_shift(self, mock_render):
        options = create_options(num_pixels=100, step_size=1)
        run(options)
        mock_render.reset_mock()
        options.pixels.reset_mock()

        # for i in range(options.num_pixels):
        #     run(options)
        #     self.assertEqual(len(options.colors), options.num_pixels)
        #     self.assertEqual(mock_render.call_count, options.num_pixels)
        #     options.pixels.write.assert_called_once()
        #     options.pixels.reset_mock()
        #     mock_render.reset_mock()
        run(options)
        self.assertEqual(len(options.colors), options.num_pixels)
        self.assertEqual(mock_render.call_count, options.num_pixels)

    def test_sparkle_shift_render(self):
        options = create_options(num_pixels=10, step_size=1)
        options.pixels = list(['', ''])
        items = ['foo', 'bar']
        options.colors = items

        render(0, options)
        self.assertEqual(options.pixels[0], options.colors[0])

        render(1, options)
        self.assertEqual(options.pixels[1], options.colors[1])