import unittest
from Grid.grid import gridChallenge

class GridChallengeTest(unittest.TestCase):

    def test_tc01_example_yes(self):
        # Arrange
        grid = [
            "abc",
            "ade",
            "efg"
        ]
        # Act
        result = gridChallenge(grid)
        # Assert
        self.assertEqual(result, "YES")

    def test_tc02_simple_no(self):
        # Arrange
        grid = [
            "ebacd",
            "fghij",
            "olmkn",
            "trpqs",
            "xywuv"
        ]
        # Act
        result = gridChallenge(grid)
        # Assert
        self.assertEqual(result, "YES")

    def test_tc03_single_row(self):
        # Arrange
        grid = ["zxy"]
        # Act
        result = gridChallenge(grid)
        # Assert
        self.assertEqual(result, "YES")

    def test_tc04_single_column(self):
        # Arrange
        grid = [
            "a",
            "b",
            "c"
        ]
        # Act
        result = gridChallenge(grid)
        # Assert
        self.assertEqual(result, "YES")

    def test_tc05_unsorted_column(self):
        # Arrange
        grid = [
            "mpxz",
            "abcd",
            "wlmf"
        ]
        # Act
        result = gridChallenge(grid)
        # Assert
        self.assertEqual(result, "NO")

