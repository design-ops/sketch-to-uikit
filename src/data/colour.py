#
from dataclasses import dataclass
from typing import Optional


@dataclass
class Colour:

    red: float
    green: float
    blue: float
    alpha: float

    @staticmethod
    def default():
        return Colour(red=0, green=0, blue=0, alpha=0)

    @staticmethod
    def from_dict(colour_dict: dict):
        red = colour_dict.get('red', 0)
        if not isinstance(red, (int, float)):
            raise TypeError(f"`red` should be an int or a float, not {type(red)}")
        if red < 0 or red > 1:
            raise ValueError(f"`red` value should be between 0 and 1, not {red}")
        green = colour_dict.get('green', 0)
        if not isinstance(green, (int, float)):
            raise TypeError(f"`green` should be an int or a float, not {type(green)}")
        if green < 0 or green > 1:
            raise ValueError(f"`green` value should be between 0 and 1, not {green}")
        blue = colour_dict.get('blue', 0)
        if not isinstance(blue, (int, float)):
            raise TypeError(f"`blue` should be an int or a float, not {type(blue)}")
        if blue < 0 or blue > 1:
            raise ValueError(f"`blue` value should be between 0 and 1, not {blue}")
        alpha = colour_dict.get('alpha', 0)
        if not isinstance(alpha, (int, float)):
            raise TypeError(f"`alpha` should be an int or a float, not {type(alpha)}")
        if alpha < 0 or alpha > 1:
            raise ValueError(f"`alpha` value should be between 0 and 1, not {alpha}")
        return Colour(red=float(red),
                      green=float(green),
                      blue=float(blue),
                      alpha=float(alpha))
