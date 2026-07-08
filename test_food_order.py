"""Pytest tests for the Week 7 food order calculator."""

from food_order import food_order


def test_order1():
    assert food_order(10, 2) == 20


def test_total_food_order_equal_30():
    assert food_order(15, 2) == 30


def test_total_food_order_equal_100():
    assert food_order(25, 4) == 100


def test_total_food_order_equal_10():
    assert food_order(5, 2) == 10


def test_invalid_price():
    assert food_order(-10, 2) == "invalid price"


def test_invalid_quantity():
    assert food_order(10, 0) == "invalid quantity"
