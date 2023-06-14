import numpy as np


class Multiplication:
    """
    Instantiate a multiplication operation.
    Number will be multiplied by the given operation.

    """

    def __init__(self, multiplier):
        """
        :param multiplier: the multiplier.
        :type multiplier: int.

        """
        self.multiplier = multiplier

    def multiply(self, number):
        """
        Multiply a given number by multiplier.
        :param number: The number to multiply
        :type number: int.

        """
        return np.dot(number, self.multiplier)
