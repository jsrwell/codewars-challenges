import unittest

"""
===============================================================================
                        Solution the Challenge
===============================================================================
"""


def square_it(digits: int) -> str:
    """
    Returns a square block of digits if the length of the input digits is
    a perfect square, otherwise, returns 'Not a perfect square!'.

    Args:
        digits (int): An integer representing a sequence of digits.

    Returns:
        str: A square block of digits separated by newlines if it's a perfect
        square, or 'Not a perfect square!' if it's not.
    """

    str_d = str(digits)

    # Calculate the square root of the length of the string
    root = int(len(str_d)**0.5)

    # Check if the length is a perfect square
    if root*root == len(str_d):
        # Split the string into blocks of equal size and join them
        return '\n'.join([str_d[i:i+root] for i in range(0, len(str_d), root)])
    else:
        return 'Not a perfect square!'


"""
===============================================================================
                        Tests the Challenge
===============================================================================
"""


class TestChallenge(unittest.TestCase):
    """Test functions of the challenge"""

    sample_test_cases = [
        (1, '1'),
        (222, 'Not a perfect square!'),
        (1212, '12\n12'),
        (123123123, '123\n123\n123'),
        (234562342342, 'Not a perfect square!'),
        (88989, 'Not a perfect square!'),
        (112141568, '112\n141\n568'),
    ]

    # Defina o método de teste com o nome correto (test_sample)
    def test_sample(self):
        for n, expected in self.sample_test_cases:
            print(f'square_it({n})')
            self.assertEqual(square_it(n), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)

"""
===============================================================================
                        Descriptions the Challenge
===============================================================================
"""

level = '7 kyu'
title = 'Perfect squares, perfect fun'
description = (
    'Given an integer, if the length of it\'s digits is a perfect square,'
    'return a square block of sqroot(length) * sqroot(length). If not, simply'
    ' return "Not a perfect square!".'

    'Examples:'

    '1212 returns:'

    '"12'
    '12"'
    'Note: 4 digits so 2 squared (2x2 perfect square). 2 digits on each line.'

    '123123123 returns:'

    '"123'
    '123'
    '123"'
    'Note: 9 digits so 3 squared (3x3 perfect square). 3 digits on each line.'
)
