from l_sys import LSys
import time
import sys


def main():
    l_sys = LSys(l_sys="pifagors_tree", iterations=4)
    #l_sys.draw_sequence()
    print(l_sys.make_sequnce())
    time.sleep(2)
    sys.exit(0)


if __name__ == "__main__":
    main()