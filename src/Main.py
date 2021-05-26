import turtle as draw


def init():
    draw.speed(15)
    draw.color("black", "white")


def l_sys_main():
    init()
    draw.begin_fill()
    while True:
        draw.forward(200)
        draw.left(170)
        if abs(draw.pos()) < 1:
            break
    draw.end_fill()
    draw.done()

