# pylint: disable=missing-docstring
from sorting import bubble, selection, insertion


def test_bubble_sort():
    data = [5, 4, 3, 2, 1]
    bubble(data)
    assert data == sorted(data)


def test_bubble_sort_no_change():
    data = [1, 2, 3, 4, 6, 7, 8]
    time_swap = bubble(data)
    assert time_swap == 0


def test_bubble_sort_random():
    data = [6, 1, 7, 8, 19, 60, -7]
    bubble(data)
    assert data == sorted(data)


def test_selection_sort():
    data = [5, 4, 3, 2, 1]
    selection(data)
    assert data == sorted(data)


def test_selection_sort_no_change():
    data = [1, 2, 3, 4, 6, 7, 8]
    time_swap = selection(data)
    assert time_swap == 0


def test_selection_sort_random():
    data = [6, 1, 7, 8, 19, 60, -7]
    selection(data)
    assert data == sorted(data)


def test_insertion_sort():
    data = [5, 4, 3, 2, 1]
    data, _ = insertion(data)
    assert data == sorted(data)


def test_insertion_sort_no_change():
    data = [1, 2, 3, 4, 6, 7, 8]
    _, time_swap = insertion(data)
    assert time_swap == len(data)


def test_insertion_sort_random():
    data = [6, 1, 7, 8, 19, 60, -7]
    data, time_swap = insertion(data)
    assert data == sorted(data)
    assert time_swap == len(data)
