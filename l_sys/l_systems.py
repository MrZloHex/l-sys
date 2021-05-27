from l_sys.make_tree import Sequence

class L_Sys:
    def __init__(self, l_sys: str, iterations: int):
        self._l_sys = l_sys
        self._iterations = iterations

    def make_sequnce(self) -> tuple:
        seq = Sequence(self._l_sys)
        return seq.make_seq(self._iterations)





    #def draw_sequence(self):
