import unittest
from Caesar_Cipher.caesar_Cipher import caesarCipher

class CaesarCipherTest(unittest.TestCase):

    def test_tc01_basic_lowercase(self):
        # Arrange
        s = "abc"
        k = 3
        # Act
        result = caesarCipher(s, k)
        # Assert
        self.assertEqual(result, "def")

    def test_tc02_wrap_around(self):
        # Arrange
        s = "xyz"
        k = 3
        # Act
        result = caesarCipher(s, k)
        # Assert
        self.assertEqual(result, "abc")

    def test_tc03_mixed_case(self):
        # Arrange
        s = "AbC"
        k = 2
        # Act
        result = caesarCipher(s, k)
        # Assert
        self.assertEqual(result, "CdE")

    def test_tc04_with_symbols(self):
        # Arrange
        s = "middle-Outz"
        k = 2
        # Act
        result = caesarCipher(s, k)
        # Assert
        self.assertEqual(result, "okffng-Qwvb")

    def test_tc05_large_k(self):
        # Arrange
        s = "abc"
        k = 28
        # Act
        result = caesarCipher(s, k)
        # Assert
        self.assertEqual(result, "cde")

