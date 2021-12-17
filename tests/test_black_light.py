from unittest import TestCase

from mock import patch

from algos.l_black_light import run
from .test_utils import create_options


class TestBlackLight(TestCase):

    @patch('algos.l_black_light.render')
    def test_black_light(self, render):
        options = create_options(num_pixels=5, step_size=255)
        for i in range(options.num_pixels):
            run(options)
            self.assertEqual(len(options.buffer), options.num_pixels)
            self.assertEqual(len(options.colors), i + 1)

# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin git@github.com:jweaver85/neopixel-pico-encoders.git
# git push -u origin main
