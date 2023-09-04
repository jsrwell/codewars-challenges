import unittest

"""
===============================================================================
                        Solution the Challenge
===============================================================================
"""


def check_for_factor(base: int, factor: int) -> bool:
    """
    Check if a number is a factor of another number.

    Args:
        base (int): The number to be checked for being 
        a multiple of the factor.
        factor (int): The number to be checked as a 
        potential factor of the base.

    Returns:
        bool: True if the factor is a factor of the base,
        False otherwise.
    """
    return base % factor == 0


"""
===============================================================================
                        Tests the Challenge
===============================================================================
"""


class TestChallenge(unittest.TestCase):
    """Test functions of the challenge"""

    def test_check_for_factor(self):
        self.assertTrue(check_for_factor(10, 2))
        self.assertTrue(check_for_factor(63, 7))
        self.assertTrue(check_for_factor(2450, 5))
        self.assertTrue(check_for_factor(24612, 3))
        self.assertFalse(check_for_factor(9, 2))
        self.assertFalse(check_for_factor(653, 7))
        self.assertFalse(check_for_factor(2453, 5))
        self.assertFalse(check_for_factor(24617, 3))


if __name__ == "__main__":
    unittest.main(verbosity=2)

"""
===============================================================================
                        Descriptions the Challenge
===============================================================================
"""

level = '8 kyu'
title = 'Grasshopper - Check for factor'
description = (
    'This function should test if the factor is a factor of base.'

    'Return true if it is a factor or false if it is not.'

    'About factors'
    'Factors are numbers you can multiply together to get another number.'

    '2 and 3 are factors of 6 because: 2 * 3 = 6'

    'You can find a factor by dividing numbers. If the remainder is 0 then the'
    'number is a factor.'
    'You can use the mod operator (%) in most languages to check for a'
    'remainder. For example 2 is not a factor of 7 because: 7 % 2 = 1'

    'Note: base is a non-negative number, factor is a positive number.'

    'MATHEMATICSFUNDAMENTALS'
)
