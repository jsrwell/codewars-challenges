import unittest

"""
===============================================================================
                        Solution the Challenge
===============================================================================
"""


from typing import Dict

switch: Dict[int, str] = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}


def switch_it_up(number: int) -> str:
    """Adapted Switch-Case from Python"""

    return switch.get(number, "The number is not from 0 to 9!")


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
