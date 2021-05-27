import turtle as draw
from src import make_tree

#def lanп(instr: str):
    #if ins

def draw_tree(sequence: str):
    for instruction in sequence:
        lang(instruction)


def init():
    draw.screensize(400, 250, "black")
    draw.setposition(0, -250)
    draw.speed(15)
    draw.color("white", "black")


def l_sys_main():
    init()
    draw.begin_fill()
    for instr in make_tree.instr():
        draw_tree(instr)
    draw.end_fill()
