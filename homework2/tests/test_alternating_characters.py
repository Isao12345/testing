import unittest
from Alternating_Characters.alternating_characters import alternatingCharacters

class AlternatingCharactersTest(unittest.TestCase):

    def test_tc01_aabaab(self):
        # Arrange
        s = "AABAAB"
        # Act
        result = alternatingCharacters(s)
        # Assert
        self.assertEqual(result, 2)

    def test_tc02_all_same(self):
        # Arrange
        s = "AAAA"
        # Act
        result = alternatingCharacters(s)
        # Assert
        self.assertEqual(result, 3)

    def test_tc03_alternating(self):
        # Arrange
        s = "ABABAB"
        # Act
        result = alternatingCharacters(s)
        # Assert
        self.assertEqual(result, 0)

    def test_tc04_single_char(self):
        # Arrange
        s = "A"
        # Act
        result = alternatingCharacters(s)
        # Assert
        self.assertEqual(result, 0)

    def test_tc05_aaabbb(self):
        # Arrange
        s = "AAABBB"
        # Act
        result = alternatingCharacters(s)
        # Assert
        self.assertEqual(result, 4)

