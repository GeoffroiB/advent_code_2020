from typing import List
import sys

import days


def main(args: List[str]):
    day = getattr(days, f"Day{int(args[0])}")()
    day.run()


DAY_NUMBER: int = 3  # default value, if not in arguments

if __name__ == "__main__":
    main(sys.argv[1:] or [str(DAY_NUMBER)])
