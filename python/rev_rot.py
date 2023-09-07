import unittest

"""
===============================================================================
                        Solution the Challenge
===============================================================================
"""


def is_cubes_divisible_by_2(chunk: str) -> bool:
    """
    Check if the sum of cubes of digits in a chunk is divisible by 2.

    Args:
        chunk (str): A string containing digits.

    Returns:
        bool: True if the sum of cubes is divisible by 2, False otherwise.
    """
    sum_of_cubes = sum(int(digit) ** 3 for digit in chunk)
    return sum_of_cubes % 2 == 0


def rotate_chunk(chunk: str) -> str:
    """
    Rotate a chunk to the left by one position.

    Args:
        chunk (str): A string containing digits.

    Returns:
        str: The rotated chunk.
    """
    return chunk[1:] + chunk[0]


def rev_rot(strng: str, sz: int) -> str:
    """
    Reverse or rotate chunks of a string based on specified conditions.

    Args:
        strng (str): The input string of digits.
        sz (int): The size of each chunk.

    Returns:
        str: The modified string with reversed or rotated chunks.
    """
    if sz <= 0 or not strng:
        return ""

    if sz > len(strng):
        return ""

    result = ""
    chunks = [strng[i:i+sz] for i in range(0, len(strng), sz)]

    for chunk in chunks:
        if len(chunk) == sz:
            if is_cubes_divisible_by_2(chunk):
                result += chunk[::-1]
            else:
                result += rotate_chunk(chunk)

    return result


"""
===============================================================================
                        Tests the Challenge
===============================================================================
"""


class TestChallenge(unittest.TestCase):
    """Test functions of the challenge"""

    def test_challenge(self):
        self.assertEqual(rev_rot("1234", 0), "")
        self.assertEqual(rev_rot("", 0), "")
        self.assertEqual(rev_rot("1234", 5), "")
        s = "733049910872815764"
        self.assertEqual(rev_rot(s, 5), "330479108928157")


if __name__ == "__main__":
    unittest.main(verbosity=2)

"""
===============================================================================
                        Descriptions the Challenge
===============================================================================
"""

level = '6 kyu'
title = 'Reverse or rotate?'
description = (
    'The input is a string str of digits. Cut the string into chunks (a chunk'
    'here is a substring of the initial string) of size sz (ignore the last'
    'chunk if its size is less than sz).'
    'If a chunk represents an integer such as the sum of the cubes of its'
    'digits is divisible by 2, reverse that chunk; otherwise rotate it to'
    'the left by one position. Put together these modified chunks and return'
    'the result as a string.'
    'If'
    'sz is <= 0 or if str is empty return ""'
    'sz is greater (>) than the length of str it is impossible to take a chunk'
    'of size sz hence return "".'
    'Examples:'
    'revrot("123456987654", 6) --> "234561876549"'
    'revrot("123456987653", 6) --> "234561356789"'
    'revrot("66443875", 4) --> "44668753"'
    'revrot("66443875", 8) --> "64438756"'
    'revrot("664438769", 8) --> "67834466"'
    'revrot("123456779", 8) --> "23456771"'
    'revrot("", 8) --> ""'
    'revrot("123456779", 0) --> ""'
    'revrot("563000655734469485", 4) --> "0365065073456944"'
    'Example of a string rotated to the left by one position:'
    's = "123456" gives "234561".'
)
