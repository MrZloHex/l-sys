class Sequence:
    def __init__(self, l_sys: str):
        self._l_sys = l_sys

    def make_seq(self, iterations: int) -> tuple:
        if self._l_sys == "curve_coch":
            return self._curve_coch(iterations)
        elif self._l_sys == "triangle_serpinskii":
            return self._triangle_serp(iterations)

    def _triangle_serp(self, iterations: int) -> tuple:
        axiom = "f-g-g"
        for i in range(iterations):
            instr = ""
            for char in axiom:
                instr += self._lang(char)
            axiom = instr
        return (axiom, )

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
        triangle_serp = {
            "f": "f-g+f+g-f",
            "g": "gg",
            "+": "+",
            "-": "-"
        }
        if self._l_sys == "curve_coch":
            return coch_lang[key]
        elif self._l_sys == "triangle_serpinskii":
            return triangle_serp[key]
