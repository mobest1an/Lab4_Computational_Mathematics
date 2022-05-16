from maths.data import Point


def get_app_mode():
    while True:
        try:
            app_mode = int(input('Выберите метод ввода данных (1 - клавиатура, 2 - файл): '))
            if app_mode == 1 or app_mode == 2:
                return app_mode
            else:
                print('Неправильный формат ввода!')
        except ValueError:
            print('Неправильный формат ввода!')


def get_points():
    n = 0
    while n <= 0:
        try:
            n = int(input('Ведите количество точек: '))
        except ValueError:
            print('Неправильный формат ввода!')

    points = []
    print("Введите точки через пробел: ")
    while len(points) != n:
        try:
            for i in range(n):
                input_points = list(map(float, input().strip().split()))
                points.append(Point(input_points[0], input_points[1]))
        except:
            print('Неправильный формат ввода!')

    return points
