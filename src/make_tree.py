def lang(key: str) -> str:
    lang = {
        "f": "f+f-f-f+f",
        "+": "+",
        "-": "-"
    }
    return lang[key]


def instr(iterations: int) -> tuple:
    axiom = "f"
    for i in range(iterations):
        instr = ""
        for char in axiom:
            instr += lang(char)
        axiom = instr
        #print(axiom)
    return axiom