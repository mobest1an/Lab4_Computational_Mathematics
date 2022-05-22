from maths.approximation import *
from user_io.console_inputs import get_app_mode, get_points
from user_io.plot_drawer import draw_plot


def console_mode():
    points = get_points()
    linear_function, linear_presentation_function, linear_mid_square_error = linear_approximation(points)
    square_function, square_presentation_function, square_mid_square_error = square_approximation(points)
    cubic_function, cubic_presentation_function, cubic_mid_square_error = cubic_approximation(points)
    degree_function, degree_presentation_function, degree_mid_square_error = degree_approximation(points)
    exponential_function, exponential_presentation_function, exponential_mid_square_error = exponential_approximation(points)
    ln_function, ln_presentation_function, ln_mid_square_error = ln_approximation(points)

    if linear_function is not None:
        print(f"Линейной аппроксимацией получена функция: {linear_presentation_function}, sigma = {round(linear_mid_square_error, 3)}")
    else:
        print("Линейная аппроксимация не найдена!")
        linear_mid_square_error = 999
    if square_function is not None:
        print(f"Квадратичной аппроксимацией получена функция: {square_presentation_function}, sigma = {round(square_mid_square_error, 3)}")
    else:
        print("Квадратичная аппроксимация не найдена!")
        square_mid_square_error = 999
    if cubic_function is not None:
        print(f"Кубической аппроксимацией получена функция: {cubic_presentation_function}, sigma = {round(cubic_mid_square_error, 3)}")
    else:
        print("Кубическая аппроксимация не найдена!")
        cubic_mid_square_error = 999
    if degree_function is not None:
        print(f"Степенной аппроксимацией получена функция: {degree_presentation_function}, sigma = {round(degree_mid_square_error, 3)}")
    else:
        print("Степенная аппроксимация не найдена!")
        degree_mid_square_error = 999
    if exponential_function is not None:
        print(f"Экспоненциальной аппроксимацией получена функция: {exponential_presentation_function}, sigma = {round(exponential_mid_square_error, 3)}")
    else:
        print("Экспоненциальная аппроксимация не найдена!")
        exponential_mid_square_error = 999
    if ln_function is not None:
        print(f"Логарифмической аппроксимацией получена функция: {ln_presentation_function}, sigma = {round(ln_mid_square_error, 3)}")
    else:
        print("Логарифмическая аппроксимация не найдена!")
        ln_mid_square_error = 999

    r = min(linear_mid_square_error, square_mid_square_error, cubic_mid_square_error, degree_mid_square_error, exponential_mid_square_error, ln_mid_square_error)

    print(f"Минимальное среднеквадратичное отклонение: {round(r, 3)}")
    if r == linear_mid_square_error:
        print("Наилучшая аппроксимация: линейная")
    elif r == square_mid_square_error:
        print("Наилучшая аппроксимация: квадратичная")
    elif r == cubic_mid_square_error:
        print("Наилучшая аппроксимация: кубическая")
    elif r == degree_mid_square_error:
        print("Наилучшая аппроксимация: степенная")
    elif r == exponential_mid_square_error:
        print("Наилучшая аппроксимация: экспоненциальная")
    elif r == ln_mid_square_error:
        print("Наилучшая аппроксимация: логарфимическая")

    draw_plot(points, linear_function, square_function, cubic_function, degree_function, exponential_function, ln_function)


def file_mode():
    pass


if __name__ == "__main__":
    app_mode = get_app_mode()
    if app_mode == 1:
        console_mode()
    else:
        file_mode()
