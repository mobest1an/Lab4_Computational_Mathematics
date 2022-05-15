import math
import numpy as np


def calculate_system(array, n):
    max_iterations = 100000
    epsilon = 0.00001
    vector_old_ans = [0] * n
    vector_answer = [0] * n
    difference = epsilon + 1
    num = 0

    while difference > epsilon:
        for i in range(n):
            sum = 0
            for j in range(n):
                if i != j:
                    sum += array[i][j] / array[i][i] * vector_answer[j]
            vector_answer[i] = array[i][n] / array[i][i] - sum
        for i in vector_answer:
            if i is None or i == math.inf or i == -math.inf:
                print("Значения расходятся, невозможно найти ответ")
                return

        max_difference = 0.0
        for i in range(n):
            if abs(vector_old_ans[i] - vector_answer[i]) > max_difference:
                max_difference = abs(vector_old_ans[i] - vector_answer[i])
        difference = max_difference
        for i in range(n):
            vector_old_ans[i] = vector_answer[i]
        num += 1
        if num >= max_iterations:
            print("Не удалось получить ответ за максимальное количество итераций")
            return
    return vector_answer


def linear_approximation(points):
    n = len(points)
    sx = 0
    sx2 = 0
    sy = 0
    sxy = 0
    for i in range(n):
        sx += points[i].x
        sx2 += points[i].x ** 2
        sy += points[i].y
        sxy += points[i].x * points[i].y

    mid_x = sx / n
    mid_y = sy / n

    r_part1 = 0
    r_part2 = 0
    r_part3 = 0

    for i in range(n):
        r_part1 += (points[i].x - mid_x) * (points[i].y - mid_y)
        r_part2 += (points[i].x - mid_x) ** 2
        r_part3 += (points[i].y - mid_y) ** 2

    try:
        r = r_part1 / (math.sqrt(r_part2 * r_part3))
        print("Коэффициент корреляции Пирсона равен: {}".format(round(r, 3)))
    except:
        print("Не получилось посчитать коэффициент корреляции Пирсона.")

    answer = calculate_system([[sx2, sx, sxy], [sx, n, sy]], 2)
    if not answer:
        return None, None, None

    result_function = lambda x: answer[0] * x + answer[1]
    presentation_function = f"{round(answer[0], 3)}x + {round(answer[1], 3)}"

    errors = [(points[i].y - result_function(points[i].x)) ** 2 for i in range(n)]
    mid_square_error = math.sqrt(sum(errors) / n)

    return result_function, presentation_function, mid_square_error


def square_approximation(points):
    n = len(points)

    sx = 0
    sx2 = 0
    sx3 = 0
    sx4 = 0
    sy = 0
    sxy = 0
    sx2y = 0

    for i in range(n):
        sx += points[i].x
        sx2 += points[i].y ** 2
        sx3 += points[i].x ** 3
        sx4 += points[i].x ** 4
        sy += points[i].y
        sxy += points[i].x * points[i].y
        sx2y += (points[i].x ** 2) * points[i].y

    system = [
        [n, sx, sx2, sy],
        [sx, sx2, sx3, sxy],
        [sx2, sx3, sx4, sx2y]
    ]

    answer = calculate_system(system, 3)
    if not answer:
        return None, None, None

    result_function = lambda x: answer[2] * (x ** 2) + answer[1] * x + answer[0]
    presentation_function = f"{round(answer[2], 3)}x^2 + {round(answer[1], 3)}x + {round(answer[0], 3)}"

    errors = [(points[i].y - result_function(points[i].x)) ** 2 for i in range(n)]
    mid_square_error = math.sqrt(sum(errors) / n)

    return result_function, presentation_function, mid_square_error


def cubic_approximation(points):
    n = len(points)

    sx = 0
    sx2 = 0
    sx3 = 0
    sx4 = 0
    sx5 = 0
    sx6 = 0
    sy = 0
    sxy = 0
    sx2y = 0
    sx3y = 0

    for i in range(n):
        sx += points[i].x
        sx2 += points[i].x ** 2
        sx3 += points[i].x ** 3
        sx4 += points[i].x ** 4
        sx5 += points[i].x ** 5
        sx6 += points[i].x ** 6
        sy += points[i].y
        sxy += points[i].x * points[i].y
        sx2y += (points[i].x ** 2) * points[i].y
        sx3y += (points[i].x ** 3) * points[i].y

    system = [
        [n, sx, sx2, sx3, sy],
        [sx, sx2, sx3, sx4, sxy],
        [sx2, sx3, sx4, sx5, sx2y],
        [sx3, sx4, sx5, sx6, sx3y]
    ]

    answer = calculate_system(system, 4)
    if not answer:
        return None, None, None

    result_function = lambda x: answer[3] * (x ** 3) + answer[2] * (x ** 2) + answer[1] * x + answer[0]
    presentation_function = f"{round(answer[3], 3)}x^3 + {round(answer[2], 3)}x^2 + {round(answer[1], 3)}x + {round(answer[0], 3)}"

    errors = [(points[i].y - result_function(points[i].x)) ** 2 for i in range(n)]
    mid_square_error = math.sqrt(sum(errors) / n)

    return result_function, presentation_function, mid_square_error


def degree_approximation(points):
    true_points = []
    for point in points:
        if point.x > 0 and point.y > 0:
            true_points.append(point)

    if len(true_points) != len(points):
        return None, None, None

    n = len(true_points)

    sx = 0
    sx2 = 0
    sy = 0
    sxy = 0

    for i in range(n):
        sx += math.log(true_points[i].x)
        sx2 += math.log(true_points[i].x) ** 2
        sy += math.log(true_points[i].y)
        sxy += math.log(true_points[i].x) * math.log(true_points[i].y)

    try:
        answer = calculate_system([[sx2, sx, sxy], [sx, n, sy]], 2)
    except:
        return None, None, None

    result_function = lambda x: np.exp(answer[1]) * (x ** answer[0])
    presentation_function = f"{round(math.exp(answer[1]), 3)}x^{round(answer[0], 3)}"

    errors = [(true_points[i].y - result_function(true_points[i].x)) ** 2 for i in range(n)]
    mid_square_error = math.sqrt(sum(errors) / n)

    return result_function, presentation_function, mid_square_error


def exponential_approximation(points):
    true_points = []
    for point in points:
        if point.y > 0:
            true_points.append(point)

    if len(true_points) != len(points):
        return None, None, None

    n = len(true_points)

    sx = 0
    sx2 = 0
    sy = 0
    sxy = 0
    for i in range(n):
        sx += true_points[i].x
        sx2 += true_points[i].x ** 2
        sy += math.log(true_points[i].y)
        sxy += true_points[i].x * math.log(true_points[i].y)

    answer = calculate_system([[sx2, sx, sxy], [sx, n, sy]], 2)
    if not answer:
        return None, None, None

    result_function = lambda x: np.exp(answer[1]) * np.exp(answer[0] * x)
    presentation_function = f"{round(math.exp(answer[1]), 3)}e^{round(answer[0], 3)}*x"

    errors = [(true_points[i].y - result_function(true_points[i].x)) ** 2 for i in range(n)]
    mid_square_error = math.sqrt(sum(errors) / n)

    return result_function, presentation_function, mid_square_error


def ln_approximation(points):
    true_points = []

    for i in points:
        if i.x > 0:
            true_points.append(i)

    if len(true_points) != len(points):
        return None, None, None

    n = len(true_points)

    sx = 0
    sx2 = 0
    sy = 0
    sxy = 0

    for i in range(n):
        sx += math.log(true_points[i].x)
        sx2 += math.log(true_points[i].y) ** 2
        sy += true_points[i].y
        sxy += math.log(true_points[i].x) * true_points[i].y

    answer = calculate_system([[sx2, sx, sxy], [sx, n, sy]], 2)
    if not answer:
        return None, None, None

    result_function = lambda x: answer[0] * np.log(x) + answer[1]
    presentation_function = f"{round(answer[0], 3)} ln(x) + {round(answer[1], 3)}"

    errors = [(true_points[i].y - result_function(true_points[i].x)) ** 2 for i in range(n)]
    mid_square_error = math.sqrt(sum(errors) / n)

    return result_function, presentation_function, mid_square_error
