import unittest

"""
===============================================================================
                        Solution the Challenge
===============================================================================
"""


def switch_it_up(number: int) -> str:
    """Switch-Case in Python"""

    match number:
        case 0:
            return 'Zero'
        case 1:
            return 'One'
        case 2:
            return 'Two'
        case 3:
            return 'Three'
        case 4:
            return 'Four'
        case 5:
            return 'Five'
        case 6:
            return 'Six'
        case 7:
            return 'Seven'
        case 8:
            return 'Eight'
        case 9:
            return 'Nine'
        case _:
            return 'The number is not from 0 to 9!'


"""
===============================================================================
                        Tests the Challenge
===============================================================================
"""


class TestChallenge(unittest.TestCase):
    """Test functions of the challenge"""

    def test_challenge(self):
        self.assertEqual(switch_it_up(0), "Zero")
        self.assertEqual(switch_it_up(9), "Nine")


if __name__ == "__main__":
    unittest.main(verbosity=2)

"""
===============================================================================
                        Descriptions the Challenge
===============================================================================
"""

level = '8 kyu'
title = 'Switch it Up!'
description = (
    'When provided with a number between 0-9, return it in words.'

    'Input :: 1'

    'Output :: "One".'

    'If your language supports it, try using a switch statement.'
)
