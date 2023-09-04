import unittest

"""
===============================================================================
                        Solution the Challenge
===============================================================================
"""


def name_shuffler(name: str) -> str:
    """Return the name with its parts reversed.

    Args:
        name (str): The input name consisting of
        first name(s) and last name(s).

    Returns:
        str: The name with its parts reversed. 
        For example, "Well Jackson" becomes "Jackson Well".
    """
    return " ".join(name.split()[::-1])


"""
===============================================================================
                        Tests the Challenge
===============================================================================
"""


class TestChallenge(unittest.TestCase):
    """Test functions of the challenge"""

    def teste_name_shuffler(self):
        self.assertEqual(name_shuffler('john McClane'), 'McClane john')
        self.assertEqual(name_shuffler('Mary jeggins'), 'jeggins Mary')
        self.assertEqual(name_shuffler('tom jerry'), 'jerry tom')


if __name__ == "__main__":
    unittest.main(verbosity=2)

"""
===============================================================================
                        Descriptions the Challenge
===============================================================================
"""

level = '8 kyu'
title = 'Name Shuffler'
description = (
    'Write a function that returns a string in which firstname is swapped'
    'with last name.'

    'Example(Input --> Output)'

    '"john McClane" --> "McClane john"'
    'STRINGSFUNDAMENTALS'
)
