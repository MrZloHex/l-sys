import turtle as draw
from src import make_tree

def lang(instr: str):
    if instr == "a":
        draw.forward(10)
    elif instr == "b":
        draw.right(90)
        draw.forward(10)
        draw.left(90)
        draw.forward(10)


def draw_tree(sequence: str):
    pos = draw.position()
    for instruction in sequence:
        lang(instruction)
        draw.setposition(pos)


def init():
    draw.screensize(400, 250, "black")
    draw.setposition(0, -250)
    draw.left(90)
    draw.speed(15)
    draw.color("white", "black")


def l_sys_main():
    init()
    draw.begin_fill()
    for instr in make_tree.instr(5):
        draw_tree(instr)
    draw.end_fill()
