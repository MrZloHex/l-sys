class LSys:
    """
    Instantiate a l-system sequence maker

    Instructions explained:
        'f', 'g' - draw single section
        'x', 'y' - optional variables for correct formatting l-system
        '+', '-' - constants to turn in side:
            '+' - right turn
            '-' - left turn
        '[', ']' - constants for work with position and direction of drawer:
            '[' - push position and direction       !! USE LIFO STACK !!
            ']' - pop position and direction

    Degree of turning for l-system:
        Koch curve            - 90
        Dragon curve          - 90
        Binary tree           - 45
        Sierpinski triangle   - 120
        Sierpinski curve      - 60

    """

    def __init__(self, l_sys: str, iterations: int):
        """
        Constructor of class

        :param l_sys: Name of l-system. E.g. 'koch curve'
        :type l_sys: str
        :param iterations: Amount of iterations for final sequence
        :type iterations: int
        """

        # Supporting l-systems
        self._sup_sys = (
            "Koch curve",
            "Sierpinski triangle",
            "Sierpinski curve",
            "Dragon curve",
            "Binary tree"
        )

        # Check name of l-system
        if l_sys in self._sup_sys:
            self._l_sys = l_sys
        else:
            if type(l_sys) is str:
                raise ValueError('Incorrect name of l-sys')
            else:
                raise TypeError('Incorrect type of name of l-sys')

        # Check iterations
        if type(iterations) is int:
            if iterations > 0:
                self._iterations = iterations
            else:
                raise ValueError('Iterations must be positive number')
        else:
            raise TypeError('Incorrect type of iterations')

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

        axiom = "g"
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

        axiom = "f"
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
            "f": "g-f-g",
            "g": "f+g+f",
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
            "f": "ff",
            "g": "f[+g]-g",
            "[": "[",
            "]": "]",
            "+": "+",
            "-": "-"
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
