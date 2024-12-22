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
