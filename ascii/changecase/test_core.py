import unittest

from . import asciiToUpperCase


class TestAsciiToUpperCase(unittest.TestCase):
    asciiCharacters = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

    def test_uppercasing_of_a_plain_text(self):
        expected = self.asciiCharacters.upper()

        result = asciiToUpperCase(self.asciiCharacters)

        self.assertEqual(result, expected)
