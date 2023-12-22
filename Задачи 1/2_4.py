import math

def find_radius(volume):
    pi = 3.14159
    radius = (3 * volume / (4 * pi)) ** (1 / 3)
    return radius

# Пример использования:
sphere_volume = 1000  # Пример объема шара
radius = find_radius(sphere_volume)
print(f"Радиус шара: {radius:.2f} ед.")
