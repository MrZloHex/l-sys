from l_sys import LSys
import time
import sys


def main():
    l_sys = LSys(l_sys="triangle_serpinskii", iterations=3)
    l_sys.draw_sequence()
    print(l_sys.make_sequnce()[0])
    time.sleep(2)
    sys.exit(0)


if __name__ == "__main__":
    main()