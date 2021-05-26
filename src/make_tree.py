def make_sequence(axiom: str, iterations: int):
    for i in range(iterations):
        print(axiom)
        instr = ""
        for char in axiom:
            instr += lang(char)
        axiom = instr


def lang(key: str) -> str:
    lang = {
        "a": "ab",
        "b": "a"
    }
    return lang[key]



def instr() -> tuple:
    init_str = "a"
    make_sequence(init_str, 6)
    instr = ("f", "+")
    return instr