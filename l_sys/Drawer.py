import turtle as draw
from typing import NoReturn


class Drawer:
    def __init__(self, l_sys: str):
        draw.screensize(400, 250, "black")
        draw.setposition(-400, -250)
        # draw.left(90)
        draw.speed(5000)
        draw.color("white", "black")
        draw.hideturtle()
        self._l_sys = l_sys

    def draw_tree(self, sequence: str) -> NoReturn:
        #tree_types = {
        #    'curve_coch': [self._draw_coch(seq) for seq in sequence[0]],
        #    'triangle_serpinskii': [self._draw_triangle_serp(seq) for seq in sequence[0]],
        #}
        #tree_types[self._l_sys]
         if self._l_sys == "curve_coch":
             for seq in sequence[0]:
                 self._draw_coch(seq)
         elif self._l_sys == "triangle_serpinskii":
             for seq in sequence[0]:
                 self._draw_triangle_serp(seq)

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
