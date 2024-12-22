import math
import pytest
import shapes.circle as circle
import shapes.square as square
import shapes.triangle as triangle
from calculator import calculate as calc


class CircleTests:
    def test_area_of_circle(self):
        radius = 3
        expected_area = math.pi * radius ** 2
        assert circle.area(radius) == expected_area

    def test_perimeter_of_circle(self):
        radius = 3
        expected_perimeter = 2 * math.pi * radius
        assert circle.perimeter(radius) == expected_perimeter


class SquareTests:
    def test_area_of_square(self):
        assert square.area(4) == 16
        assert square.area(3) == 9

    def test_perimeter_of_square(self):
        assert square.perimeter(5) == 20
        assert square.perimeter(3) == 12


class TriangleTests:
    def test_area_of_triangle(self):
        assert triangle.area(5, 5, 5) == 10.825317547305486
        assert triangle.area(10, 24, 22) == 120

    def test_perimeter_of_triangle(self):
        assert triangle.perimeter(5, 5, 5) == 15
        assert triangle.perimeter(10, 24, 22) == 56


class CalculatorTests:
    def test_negative_or_zero_size(self):
        with pytest.raises(ValueError):
            calc("square", "perimeter", [-4])

    def test_valid_triangle_sides(self):
        with pytest.raises(ValueError):
            calc("triangle", "perimeter", [-3, 4, 0])

    def test_invalid_triangle_side_length(self):
        with pytest.raises(ValueError):
            calc("triangle", "perimeter", [4, 3, 8])

    def test_invalid_shape_type(self):
        with pytest.raises(AssertionError):
            calc("pentagon", "perimeter", [6, 6, 6])

    def test_invalid_function_type(self):
        with pytest.raises(AssertionError):
            calc("triangle", "area_calc", [6, 6, 6])

    def test_invalid_size_type(self):
        with pytest.raises(TypeError):
            calc("triangle", "perimeter", [1, "two", 3])

import circle
import square
import triangle
from calculate import calc


class TestCircle:
    def test_circle_area(self):
        assert circle.area(2) == math.pi * 2 * 2

    def test_circle_perimeter(self):
        assert circle.perimeter(2) == 2 * math.pi * 2


class TestSquare:
    def test_square_area(self):
        assert square.area(5) == 25
        assert square.area(2) == 4

    def test_square_perimeter(self):
        assert square.perimeter(4) == 16
        assert square.perimeter(2) == 8


class TestTriangle:
    def test_triangle_area(self):
        assert triangle.area(6, 6, 6) == 15.588457268119896
        assert triangle.area(8, 17, 15) == 60

    def test_triangle_perimeter(self):
        assert triangle.perimeter(6, 6, 6) == 18
        assert triangle.perimeter(8, 17, 15) == 40


class TestCalc:
    def test_not_positive_size(self):
        with pytest.raises(ValueError):
            calc("square", "perimeter", [-5])

    def test_correct_triangle_size(self):
        with pytest.raises(ValueError):
            calc("triangle", "perimeter", [-5, 5, 0])

    def test_correct_triangle_side_value(self):
        with pytest.raises(ValueError):
            calc("triangle", "perimeter", [3, 2, 5])

    def test_correct_fig(self):
        with pytest.raises(AssertionError):
            calc("tr", "perimeter", [6, 6, 6])

    def test_correct_func(self):
        with pytest.raises(AssertionError):
            calc("triangle", "per", [6, 6, 6])

    def test_correct_size(self):
        with pytest.raises(TypeError):
            calc("triangle", "perimeter", "triangle")
