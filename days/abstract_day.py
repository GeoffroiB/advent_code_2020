from abc import abstractmethod, ABC
from typing import Any, Callable, List
import re

from .utils import timeExec


class AbstractDay(ABC):
    PARTS_COUNT: int = 2

    def __init__(self):
        self._day_number: int = self._parseChildClassNameForDayNumber()

    @property
    def inputs_path(self) -> str:
        return f"inputs/day_{self._day_number}.txt"

    @property
    def inputs_test_path(self) -> str:
        return f"inputs_test/day_{self._day_number}.txt"

    @abstractmethod
    def partOne(self) -> Any:
        return "To be overriden"

    @abstractmethod
    def partTwo(self) -> Any:
        return "To be overriden"

    def run(self) -> None:
        """Runs and prints results"""

        def resultToStr(index: int, dt: float, result: Any):
            return f"  Part {index + 1}:  {result:<15}  ({dt:.6f}s)"

        print(f"\nDay {self._day_number}")

        part_methods: List[Callable] = [self.partOne, self.partTwo]
        for i, part_method in enumerate(part_methods):
            print(resultToStr(i, *timeExec(part_method)))

        print("")

        return None

    def _parseChildClassNameForDayNumber(self) -> int:
        """Validate child class type name and retrieves """
        match_groups = re.match(r"Day(\d+)", type(self).__name__)

        if not match_groups:
            assert False, "Invalid child class name format [Day#]"

        day_number: int = int(match_groups.groups()[0])
        assert 0 < day_number, "Day number must be a positive value."

        return day_number
