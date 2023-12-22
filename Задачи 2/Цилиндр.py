import math

def calculate_water_mass(radius, height):
    density_of_water = 1000  # Плотность воды в г/литр (1 кг/литр = 1000 г/литр)
    
    volume = math.pi * radius**2 * height
    water_mass = volume * density_of_water / 1000  # Перевод из граммов в килограммы
    
    return round(water_mass, 2)

cylinder_radius = 5  # радиус цилиндра
cylinder_height = 10  # высота цилиндра

result = calculate_water_mass(cylinder_radius, cylinder_height)
print(f"Масса воды в цилиндре: {result} кг")
