import turtle as draw
from src import make_tree


def init():
    draw.screensize(400, 250, "black")
    draw.setposition(0, -250)
    draw.speed(15)
    draw.color("white", "black")


def l_sys_main():
    init()
    instr = make_tree.instr()
    draw.begin_fill()
    draw.end_fill()
