"""
tests to validate functionality of the 2048 game merge functionality
"""
import pytest
import game

def test_merge_empty_line():
    assert game.merge([]) == []

def test_merge_single_item_line():
    assert game.merge([2]) == [2]

def test_merge_two_item_line_mergable():
    line = [2, 2]
    assert game.merge(line) == [4, 0]

def test_merge_three_item_line_mergable():
    line = [2, 0, 2]
    assert game.merge(line) == [4, 0, 0]

def test_merge_three_item_line_not_mergable():
    line = [2, 4, 2]
    assert game.merge(line) == [2, 4, 2]

def test_merge_five_item_line_mergable():
    line = [2, 2, 0, 4, 4]
    assert game.merge(line) == [4, 8, 0, 0, 0]

def test_merge_five_item_line_mergable2():
    line = [2, 2, 2, 2, 2]
    assert game.merge(line) == [4, 4, 2, 0, 0]
     