import circle
import square
import triangle

shapes = {"circle": 1, "square": 1, "triangle": 3}

calculations = ["perimeter", "area"]

def validate_sizes(shape, dimensions):
    if any(dim <= 0 for dim in dimensions):
        raise ValueError("All dimensions must be positive numbers.")

    if shape == "triangle":
        a, b, c = dimensions
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("The provided dimensions do not form a valid triangle.")

def compute(shape, calculation, dimensions):
    assert shape in shapes
    assert calculation in calculations

    validate_sizes(shape, dimensions)

    result = eval(f"{shape}.{calculation}(*{dimensions})")
    return result

if __name__ == "__main__":
    calculation_type = ""
    shape_type = ""

    while shape_type not in shapes:
        shape_type = input(f"Please enter the name of the shape (available: {list(shapes.keys())}):\n")

    while calculation_type not in calculations:
        calculation_type = input(f"Please enter the type of calculation (available: {calculations}):\n")

    dimensions = []
    required_dimensions = shapes[shape_type]

    while len(dimensions) != required_dimensions:
        dimension_input = input(f"Enter the dimensions for the {shape_type}, separated by spaces:\n")
        dimensions = list(map(float, dimension_input.split()))

    result = compute(shape_type, calculation_type, dimensions)
    print(f"The result of the {calculation_type} of the {shape_type} is: {result}")
