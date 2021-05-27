def make_sequence(axiom: str, iterations: int) -> str:
    for i in range(iterations):
        instr = ""
        for char in axiom:
            instr += lang(char)
        axiom = instr
    return axiom


def lang(key: str) -> str:
    lang = {
        "a": "ab",
        "b": "a"
    }
    return lang[key]



def instr(iterations: int) -> tuple:
    axiom = "a"
    for i in range(iterations):
        instr = ""
        for char in axiom:
            instr += lang(char)
        axiom = instr
        yield axiom