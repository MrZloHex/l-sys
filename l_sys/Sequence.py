class Sequence:
    def __init__(self, l_sys: str):
        self._l_sys = l_sys

    def make_seq(self, iterations: int) -> str:
        if self._l_sys == "curve_coch":
            return self._curve_coch(iterations)
        elif self._l_sys == "triangle_serpinskii":
            return self._triangle_serp(iterations)
        elif self._l_sys == "curve_serpinskii":
            return self._curve_serp(iterations)
        elif self._l_sys == "curve_drakon":
            return self._curve_drakon(iterations)

    def _curve_drakon(self, iterations: int) -> str:
        axiom = "fx"
        for i in range(iterations):
            instr = ""
            for char in axiom:
                instr += self._lang(char)
            axiom = instr
        return axiom

    def _curve_serp(self, iterations: int) -> str:
        axiom = "a"
        for i in range(iterations):
            instr = ""
            for char in axiom:
                instr += self._lang(char)
            axiom = instr
        return axiom

    def _triangle_serp(self, iterations: int) -> str:
        axiom = "f-g-g"
        for i in range(iterations):
            instr = ""
            for char in axiom:
                instr += self._lang(char)
            axiom = instr
        return axiom

    def _curve_coch(self, iterations: int) -> str:
        axiom = "f"
        for i in range(iterations):
            instr = ""
            for char in axiom:
                instr += self._lang(char)
            axiom = instr
        return axiom

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
        curve_drakon = {
            "x": "x+yf+",
            "y": "-fx-y",
            "f": "f",
            "+": "+",
            "-": "-"
        }
        if self._l_sys == "curve_coch":
            return curve_coch[key]
        elif self._l_sys == "triangle_serpinskii":
            return triangle_serp[key]
        elif self._l_sys == "curve_serpinskii":
            return curve_serp[key]
        elif self._l_sys == "curve_drakon":
            return curve_drakon[key]
