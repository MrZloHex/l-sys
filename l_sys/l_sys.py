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
        self._sup_sys = (
            "Koch curve",
            "Sierpinski triangle",
            "Sierpinski curve",
            "Dragon curve",
            "Binary tree"
        )

        if l_sys in self._sup_sys:
            self._l_sys = l_sys
        else:
            print("There are no such l-system")
            self._l_sys = "Koch curve"
        self._iterations = iterations

    def make_seq(self) -> str:
        """
        Make sequence of your l-system

        :return: Sequence of instructions
        :rtype: str
        """

        if self._l_sys == "Koch curve":
            return self._curve_koch()
        elif self._l_sys == "Sierpinski triangle":
            return self._triangle_serp()
        elif self._l_sys == "Sierpinski curve":
            return self._curve_serp()
        elif self._l_sys == "Dragon curve":
            return self._curve_dragon()
        elif self._l_sys == "Binary tree":
            return self._binary_tree()

    def _binary_tree(self) -> str:
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

    def _curve_dragon(self) -> str:
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

    def _curve_koch(self) -> str:
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
        koch_curve = {
            "f": "f+f-f-f+f",
            "+": "+",
            "-": "-"
        }
        serp_triangle = {
            "f": "f-g+f+g-f",
            "g": "gg",
            "+": "+",
            "-": "-"
        }
        serp_curve = {
            "a": "b-a-b",
            "b": "a+b+a",
            "+": "+",
            "-": "-"
        }
        dragon_curve = {
            "x": "x+yf+",
            "y": "-fx-y",
            "f": "f",
            "+": "+",
            "-": "-"
        }
        bin_tree = {
            "1": "11",
            "0": "1[0]0",
            "[": "[",
            "]": "]"
        }
        if self._l_sys == "Koch curve":
            return koch_curve[key]
        elif self._l_sys == "Sierpinski triangle":
            return serp_triangle[key]
        elif self._l_sys == "Sierpinski curve":
            return serp_curve[key]
        elif self._l_sys == "Dragon curve":
            return dragon_curve[key]
        elif self._l_sys == "Binary tree":
            return bin_tree[key]
