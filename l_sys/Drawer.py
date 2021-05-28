import turtle as draw
from typing import NoReturn
from queue import LifoQueue


class Drawer:
    def __init__(self, l_sys: str, iterations: int):
        draw.screensize(400, 400, "black")
        if l_sys == "pifagors_tree":
            draw.setposition(0, -250)
            draw.setheading(90)
        elif l_sys == "curve_serpinskii":
            draw.setposition(-400, -250)
            draw.setheading(60)
        else:
            draw.setposition(-400, -200)
            draw.setheading(0)
        self._length = 10
        draw.speed(1500)
        draw.color("white", "black")
        draw.hideturtle()
        self._l_sys = l_sys
        # self.stack = LifoQueue(maxsize=50)
        self.stack = []

    def draw_tree(self, sequence: str) -> NoReturn:
        # tree_types = {
        #    'curve_coch': [self._draw_coch(seq) for seq in sequence[0]],
        #    'triangle_serpinskii': [self._draw_triangle_serp(seq) for seq in sequence[0]],
        # }
        # tree_types[self._l_sys]
        if self._l_sys == "curve_coch":
            for seq in sequence:
                self._draw_coch(seq)
        elif self._l_sys == "triangle_serpinskii":
            for seq in sequence:
                self._draw_triangle_serp(seq)
        elif self._l_sys == "curve_serpinskii":
            for seq in sequence:
               self._draw_curve_serp(seq)
        elif self._l_sys == "curve_drakon":
            for seq in sequence:
                self._draw_curve_drakon(seq)
        elif self._l_sys == "pifagors_tree":
            for seq in sequence:
                self._draw_pifs_tree(seq)


    @staticmethod
    def _draw_coch(seq: str) -> NoReturn:
        if seq == "f":
            draw.forward(10)
        elif seq == "+":
            draw.left(90)
        elif seq == "-":
            draw.right(90)

    @staticmethod
    def _draw_triangle_serp(seq: str) -> NoReturn:
        if seq in ("f", "g"):
            draw.forward(10)
        elif seq == "+":
            draw.right(120)
        elif seq == "-":
            draw.left(120)

    def _draw_curve_serp(self, seq: str) -> NoReturn:
        if seq in ("a", "b"):
            draw.forward(self._length)
        elif seq == "+":
            draw.left(60)
        elif seq == "-":
            draw.right(60)

    @staticmethod
    def _draw_curve_drakon(seq: str) -> NoReturn:
        if seq == "f":
            draw.forward(10)
        elif seq == "+":
            draw.left(90)
        elif seq == "-":
            draw.right(90)

    def _draw_pifs_tree(self, seq: str) -> NoReturn:
        if seq == "1":
            draw.forward(self._length)
        elif seq == "0":
            draw.pencolor("green")
            draw.forward(self._length)
            draw.pencolor("white")

        elif seq == "[":
            self.stack.append(draw.position())
            self.stack.append(draw.heading())
            draw.right(45)
        elif seq == "]":
            draw.penup()
            draw.setheading(self.stack.pop())
            draw.setposition(self.stack.pop())
            draw.pendown()
            draw.left(45)


