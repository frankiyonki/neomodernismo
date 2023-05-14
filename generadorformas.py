import math

# Define a function to position the shapes in a square
def position_shapes(shapes):
    # Sort the shapes by area in descending order
    sorted_shapes = sorted(shapes.items(), key=lambda x: x[1]["area"], reverse=True)

    # Determine the dimensions of the square
    total_area = sum([shape["area"] for shape in shapes.values()])
    side_length = math.ceil(math.sqrt(total_area))
    x = 0
    y = 0

    # Position the shapes in the square
    for shape_name, shape_data in sorted_shapes:
        # Get the shape's dimensions
        width = shape_data["width"]
        height = shape_data["height"]

        # Position the shape
        shape_data["x"] = x
        shape_data["y"] = y

        #

