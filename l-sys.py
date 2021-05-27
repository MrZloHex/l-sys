from l_sys import L_Sys
import time
import sys


def main():
    l_sys = L_Sys(l_sys="coch", iterations=3)
    seq = l_sys.make_sequnce()
    for s in seq:
        print(s)
    time.sleep(2)
    sys.exit(0)


if __name__ == "__main__":
    main()