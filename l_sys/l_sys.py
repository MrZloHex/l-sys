class LSys:
    """
    Instantiate a l-system sequence maker

    """

    def __init__(self, l_sys: str, iterations: int):
        """
        Constructor of class

        :param l_sys: Name of l-system. E.g. 'koch curve'
        :type l_sys: str
        :param iterations: Amount of iterations for final sequence
        :type iterations: int
        """

        self._l_sys = l_sys
        self._iterations = iterations

    def make_seq(self) -> str:
        """
        Make sequence of your l-system

        :return: Sequence of instructions
        :rtype: str
        """

        if self._l_sys == "curve_coch":
            return self._curve_coch()
        elif self._l_sys == "triangle_serpinskii":
            return self._triangle_serp()
        elif self._l_sys == "curve_serpinskii":
            return self._curve_serp()
        elif self._l_sys == "curve_drakon":
            return self._curve_drakon()
        elif self._l_sys == "pifagors_tree":
            return self._pifagors_tree()

    def _pifagors_tree(self) -> str:
        """
        Making sequence for binary (Pythagoras) tree

        :return: instructions
        :rtype: str
        """

        axiom = "0"
        for i in range(self._iterations):
            instr = ""
            for char in axiom:
                instr += self._lang(char)
            axiom = instr
        return axiom

    def _curve_drakon(self) -> str:
        """
        Making sequence for dragon curve

        :return: instructions
        :rtype: str
        """

        axiom = "fx"
        for i in range(self._iterations):
            instr = ""
            for char in axiom:
                instr += self._lang(char)
            axiom = instr
        return axiom

    def _curve_serp(self) -> str:
        """
        Making sequence for Sierpinski curve

        :return: instructions
        :rtype: str
        """

        axiom = "a"
        for i in range(self._iterations):
            instr = ""
            for char in axiom:
                instr += self._lang(char)
            axiom = instr
        return axiom

    def _triangle_serp(self) -> str:
        """
        Making sequence for Sierpinski triangle

        :return: instructions
        :rtype: str
        """

        axiom = "f-g-g"
        for i in range(self._iterations):
            instr = ""
            for char in axiom:
                instr += self._lang(char)
            axiom = instr
        return axiom

    def _curve_coch(self) -> str:
        """
        Making sequence for Koch curve

        :return: instructions
        :rtype: str
        """

        axiom = "f"
        for i in range(self._iterations):
            instr = ""
            for char in axiom:
                instr += self._lang(char)
            axiom = instr
        return axiom

    def _lang(self, key: str) -> str:
        """
        Set of dictionaries with rules for l-systems

        :param key: instructions for transforming
        :type key: str
        :return: transformed instruction
        :rtype: str
        """
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
        pif_tree = {
            "1": "11",
            "0": "1[0]0",
            "[": "[",
            "]": "]"
        }
        if self._l_sys == "curve_coch":
            return curve_coch[key]
        elif self._l_sys == "triangle_serpinskii":
            return triangle_serp[key]
        elif self._l_sys == "curve_serpinskii":
            return curve_serp[key]
        elif self._l_sys == "curve_drakon":
            return curve_drakon[key]
        elif self._l_sys == "pifagors_tree":
            return pif_tree[key]