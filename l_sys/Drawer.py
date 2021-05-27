import turtle as draw

class Drawer:
    def __init__(self, l_sys: str):
        draw.screensize(400, 250, "black")
        draw.setposition(-400, -250)
        # draw.left(90)
        draw.speed(50)
        draw.color("white", "black")
        draw.hideturtle()
        self._l_sys = l_sys

    def draw_tree(self, sequence: str):
        if self._l_sys == "coch":
            for seq in sequence[0]:
                self._draw_coch(seq)

    def _draw_coch(self, seq: str):
        if seq == "f":
            draw.forward(10)
        elif seq == "+":
            draw.left(90)
        elif seq == "-":
            draw.right(90)