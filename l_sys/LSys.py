from l_sys.Sequence import Sequence
from l_sys.Drawer import Drawer


class LSys:
    def __init__(self, l_sys: str, iterations: int):
        self._l_sys = l_sys
        self._iterations = iterations

    def make_sequnce(self) -> tuple:
        seq = Sequence(self._l_sys)
        return seq.make_seq(self._iterations)

    def draw_sequence(self):
        drawer = Drawer(l_sys=self._l_sys)
        drawer.draw_tree(self.make_sequnce())
