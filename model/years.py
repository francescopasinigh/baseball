from dataclasses import dataclass
from datetime import date


@dataclass
class Year:
    year:int

    def __hash__(self):
        return hash(self.year)

    def __eq__(self, other):
        return self.year == other.year