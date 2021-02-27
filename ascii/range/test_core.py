import unittest

from .core import asciiRange


class TestAsciiToUpperCase(unittest.TestCase):
    def test_ranging_of_the_whole_alphabet(self):
        self.assertEqual(asciiRange('a', 'z'), 'abcdefghijklmnopqrstuvwxyz')


    def test_ranging_of_parts(self):
        self.assertEqual(asciiRange('a', 'f'), 'abcdef')
        self.assertEqual(asciiRange('g', 's'), 'ghijklmnopqrs')
        self.assertEqual(asciiRange('t', 'z'), 'tuvwxyz')


    def test_ranging_of_one_character(self):
        self.assertEqual(asciiRange('a', 'a'), 'a')
        self.assertEqual(asciiRange('m', 'm'), 'm')
        self.assertEqual(asciiRange('z', 'z'), 'z')


    def test_ranging_with_empty_arguments(self):
        self.assertEqual(asciiRange('', ''), '')
        self.assertEqual(asciiRange('', 'a'), '')
        self.assertEqual(asciiRange('a', ''), '')


    def test_ranging_with_more_than_one_character_string_arguments(self):
        self.assertEqual(asciiRange('aa', 'zz'), '')
        self.assertEqual(asciiRange('aa', 'z'), '')
        self.assertEqual(asciiRange('a', 'zz'), '')


    def test_reversed_order_of_arguments(self):
        self.assertEqual(asciiRange('z', 'x'), 'zyx')
