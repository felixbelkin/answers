def combine_coordinates(x_coords, y_coords):
    if len(x_coords) != len(y_coords):
        return "Массивы разной длины. Невозможно составить координаты точек."

    coordinates = [(x_coords[i], y_coords[i]) for i in range(len(x_coords))]
    return coordinates

x_coordinates = [1, 2, 3, 4]
y_coordinates = [5, 6, 7, 8]

result = combine_coordinates(x_coordinates, y_coordinates)
print(result) 
