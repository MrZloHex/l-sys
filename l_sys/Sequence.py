class Sequence:
    def __init__(self, l_sys: str):
        self._l_sys = l_sys

    def make_seq(self, iterations: int) -> tuple:
        if self._l_sys == "curve_coch":
            return self._curve_coch(iterations)
        elif self._l_sys == "triangle_serpinskii":
            return self._triangle_serp(iterations)
        elif self._l_sys == "curve_serpinskii":
            return self._curve_serp(iterations)

    def _curve_serp(self, iterations: int) -> tuple:
        axiom = "a"
        for i in range(iterations):
            instr = ""
            for char in axiom:
                instr += self._lang(char)
            axiom = instr
        return (axiom, )

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
        curve_coch = {
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
        curve_serp = {
            "a": "b-a-b",
            "b": "a+b+a",
            "+": "+",
            "-": "-"
        }
        if self._l_sys == "curve_coch":
            return curve_coch[key]
        elif self._l_sys == "triangle_serpinskii":
            return triangle_serp[key]
        elif self._l_sys == "curve_serpinskii":
            return curve_serp[key]
