from typing import List
import sys

import days


def main(args: List[str]):
    if not args:
        args = [int(input("Enter day to execute: "))]

    for arg in args:
        day_number = int(arg)  # may fail if not parsable
        day = getattr(days, f"Day{day_number}")()
        day.run()


if __name__ == "__main__":
    main(sys.argv[1:])
