import unittest
from Funny_string.funny_string import funnyString


class FunnyStringTest(unittest.TestCase):

    def test_tc01_acxz_funny(self):
        # Arrange
        s = "acxz"

        # Act
        result = funnyString(s)

        # Assert
        self.assertEqual(result, "Funny")

    def test_tc02_bcxz_not_funny(self):
        # Arrange
        s = "bcxz"

        # Act
        result = funnyString(s)

        # Assert
        self.assertEqual(result, "Not Funny")

    def test_tc03_single_character_funny(self):
        # Arrange
        s = "a"

        # Act
        result = funnyString(s)

        # Assert
        self.assertEqual(result, "Funny")

    def test_tc04_double_same_character_funny(self):
        # Arrange
        s = "aa"

        # Act
        result = funnyString(s)

        # Assert
        self.assertEqual(result, "Funny")

    def test_tc05_ab_funny(self):
        # Arrange
        s = "ab"

        # Act
        result = funnyString(s)

        # Assert
        self.assertEqual(result, "Funny")


