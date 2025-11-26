# tests/test_code_python.py

import code_python

def test_bad_sum():
    assert code_python.bad_sum(1, 2, 999) == 3


def test_dead_code_example_true():
    assert code_python.dead_code_example(True) is True


def test_dead_code_example_false():
    assert code_python.dead_code_example(False) is False



def test_compute_circle_area():
    god = code_python.GodObject()
    area = god.compute_circle_area(1)
    # aire du cercle de rayon 1 ≈ pi
    assert 3.1 < area < 3.2
