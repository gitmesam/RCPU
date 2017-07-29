from RCPU.assembler.expanders.helpers import get_free_register, fill_instructions

def test_get_free_register():
    assert get_free_register(["A", "B", "C"]) == "D"
    assert get_free_register(["B", "A", "D"]) == "C"
    assert get_free_register(["B", "D"]) in ["A", "C"]
    assert get_free_register(["A", "A"]) in ["B", "C", "D"]
    assert get_free_register(["A", "B", "C", "D"]) is None

def test_fill_instructions():
    original = [
    "MOV {P}, {Q}",
    "ADD {P}, {R}",
    "PSH {P}"
    ]
    filled = [
    "MOV A, B",
    "ADD A, C",
    "PSH A"
    ]
    assert fill_instructions(original, P='A', Q='B', R='C') == filled