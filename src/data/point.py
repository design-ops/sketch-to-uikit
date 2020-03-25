from dataclasses import dataclass
import re


@dataclass
class Point:

    x: float
    y: float

    @staticmethod
    def from_string(value: str):
        """
            Values for strings are in the format: `{0.5, 0}`
        """
        coordinates = re.findall("^{(\d+\.*\d*), (\d+\.*\d*)}$", value)[0]
        return Point(x=float(coordinates[0]), y=float(coordinates[1]))
