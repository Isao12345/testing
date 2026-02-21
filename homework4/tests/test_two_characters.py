import unittest
from Two_Characters.two_characters import twoCharacters

class TwoCharactersTest(unittest.TestCase):

    def test_tc01_example(self):
        # Arrange
        s = "beabeefeab"
        # Act
        result = twoCharacters(s)
        # Assert
        self.assertEqual(result, 5)

    def test_tc02_simple(self):
        # Arrange
        s = "abcabc"
        # Act
        result = twoCharacters(s)
        # Assert
        self.assertEqual(result, 4)

    def test_tc03_all_same(self):
        # Arrange
        s = "aaaa"
        # Act
        result = twoCharacters(s)
        # Assert
        self.assertEqual(result, 0)

    def test_tc04_two_valid(self):
        # Arrange
        s = "abab"
        # Act
        result = twoCharacters(s)
        # Assert
        self.assertEqual(result, 4)

    def test_tc05_no_valid_pair(self):
        # Arrange
        s = "aabb"
        # Act
        result = twoCharacters(s)
        # Assert
        self.assertEqual(result, 0)

