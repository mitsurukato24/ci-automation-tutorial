from src.adder import add


def test_add_positive() -> None:  # 正の数同士の足し算を検証するテストです
    assert add(1, 2) == 3  # add(1, 2) が 3 を返すことを検証します

def test_add_negative() -> None:  # 負の数同士の足し算を検証するテストです
    assert add(-1, -1) == -2  # add(-1, -1) が -2 を返すことを検証します
