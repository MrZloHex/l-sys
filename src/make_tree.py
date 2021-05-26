def make_sequence(axiom: str, iterations: int):
    for i in range(iterations):
        for char in axiom:
            ap = lang(char)
            print(ap)

def lang(key: str) -> str:
    lang = {
        "a": "ab",
        "b": "a"
    }
    return lang[key]




def instr() -> tuple:
    init_str = "a"
    make_sequence(init_str, 5)
    instr = ("f", "+")
    return instr