import math
import pytest
from calculate import calc
import circle
import square
import triangle


class TestCircle:
    def test_area(self):
        radius = 2
        expected_area = math.pi * radius ** 2
        assert circle.area(radius) == expected_area

    def test_perimeter(self):
        radius = 2
        expected_perimeter = 2 * math.pi * radius
        assert circle.perimeter(radius) == expected_perimeter


class TestSquare:
    def test_area(self):
        side_lengths = [5, 2]
        expected_areas = [side ** 2 for side in side_lengths]
        for side, expected in zip(side_lengths, expected_areas):
            assert square.area(side) == expected

    def test_perimeter(self):
        side_lengths = [4, 2]
        expected_perimeters = [4 * side for side in side_lengths]
        for side, expected in zip(side_lengths, expected_perimeters):
            assert square.perimeter(side) == expected


class TestTriangle:
    def test_area(self):
        triangles = [
            (6, 6, 6, 15.588457268119896),
            (8, 17, 15, 60)
        ]
        for a, b, c, expected in triangles:
            assert triangle.area(a, b, c) == expected

    def test_perimeter(self):
        triangles = [
            (6, 6, 6, 18),
            (8, 17, 15, 40)
        ]
        for a, b, c, expected in triangles:
            assert triangle.perimeter(a, b, c) == expected


class TestCalc:
    def test_not_positive_size(self):
        with pytest.raises(ValueError):
            calc("square", "perimeter", [-5])

    def test_correct_triangle_size(self):
        with pytest.raises(ValueError):
            calc("triangle", "perimeter", [-5, 5, 0])

    def test_valid_triangle_sides(self):
        with pytest.raises(ValueError):
            calc("triangle", "perimeter", [3, 2, 5])

    def test_invalid_shape(self):
        with pytest.raises(AssertionError):
            calc("tr", "perimeter", [6, 6, 6])

    def test_invalid_function(self):
        with pytest.raises(AssertionError):
            calc("triangle", "per", [6, 6, 6])

    def test_invalid_size_type(self):
        with pytest.raises(TypeError):
            calc("triangle", "perimeter", "triangle")
