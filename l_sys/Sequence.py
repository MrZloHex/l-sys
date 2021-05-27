class Sequence:
    def __init__(self, l_sys: str):
        self._l_sys = l_sys

    def make_seq(self, iterations: int) -> tuple:
        if self._l_sys == "coch":
            return self._curve_coch(iterations)

    def _curve_coch(self, iterations: int) -> tuple:
        axiom = "f"
        for i in range(iterations):
            instr = ""
            for char in axiom:
                instr += self._lang(char)
            axiom = instr
        return (axiom, )

    def _lang(self, key: str) -> str:
        coch_lang = {
            "f": "f+f-f-f+f",
            "+": "+",
            "-": "-"
        }
        if self._l_sys == "coch":
            return coch_lang[key]
