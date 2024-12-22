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
=======
figs = {"circle": 1, "square": 1, "triangle": 3}

funcs = ["perimeter", "area"]


def check_sizes(fig, sizes):

    if any(size <= 0 for size in sizes):
        raise ValueError("Sizes must be positive numbers.")

    if fig == "triangle":
        a, b, c = sizes
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("The given sizes do not form a valid triangle.")


def calc(fig, func, size):
    assert fig in figs
    assert func in funcs

    check_sizes(fig, size)

    result = eval(f"{fig}.{func}(*{size})")
    return result


if __name__ == "__main__":
    func = ""
    fig = ""

    while fig not in figs:
        fig = input(f"Enter figure name, available are {list(figs.keys())}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    size = []
    size_count = figs[fig]

    while len(size) != size_count:
        size_input = input(f"Input figure sizes, separated by space ({fig}):\n")
        size = list(map(float, size_input.split()))
