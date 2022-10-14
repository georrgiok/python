print('Программа для нахождения расстояния между точками')


def get_2d_coordinates():
    return {"x": float(input('X: ')), "y": float(input('Y: '))}

def min_and_max(first, second):
    if first > second: return {'min': second, 'max': first}
    else: return {'min': first, 'max': second}

def length_between_points(first, second):
    x_coords = min_and_max(first['x'], second['x'])
    y_coords = min_and_max(first['y'], second['y'])

    return ((x_coords['max'] - x_coords['min']) ** 2 + (y_coords['max'] - y_coords['min']) ** 2) ** 0.5

print('Первая координата')
first_point = get_2d_coordinates()
print('Вторая координата')
second_point = get_2d_coordinates()

print(length_between_points(first_point, second_point))
