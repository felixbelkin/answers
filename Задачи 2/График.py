import math

def distance_between_points(a, b):
    distance = math.sqrt((b['x'] - a['x'])**2 + (b['y'] - a['y'])**2)
    return round(distance, 3)

# Пример использования:
point_a = {'x': 1, 'y': 2}
point_b = {'x': 4, 'y': 6}

result = distance_between_points(point_a, point_b)
print(f"Расстояние между точками: {result}")
