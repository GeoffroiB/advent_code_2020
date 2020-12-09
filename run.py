from typing import List
import sys

import days


def main(args: List[str]):
    for arg in args:
        day_number = int(arg)  # may fail if not parsable
        day = getattr(days, f"Day{day_number}")()
        day.run()


DAY_NUMBER: int = 6  # default value, if not in arguments

if __name__ == "__main__":
    main(sys.argv[1:] or [str(DAY_NUMBER)])
