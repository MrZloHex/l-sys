import turtle as draw
from l_sys.make_tree import make_sequence

def lang(instr: str):
    if instr == "f":
        draw.forward(10)
    elif instr == "+":
        draw.left(90)
    elif instr == "-":
        draw.right(90)


def draw_tree(sequence: str):
    for instruction in sequence:
        lang(instruction)


def init():
    draw.screensize(400, 250, "black")
    draw.setposition(-400, -250)
    #draw.left(90)
    draw.speed(50)
    draw.color("white", "black")
    draw.hideturtle()


def l_sys_main():
    init()
    instr = make_sequence(4)
    draw_tree(instr)
    draw.done()

class Drawer
