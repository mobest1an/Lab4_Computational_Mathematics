import numpy as np
import matplotlib.pyplot as plt


def draw_plot(points, linear_function, square_function, cubic_function, degree_function, exponential_function, ln_function):
    minimum_x = 0
    maximum_x = 0

    minimum_y = 0
    maximum_y = 0

    points_x = []
    points_y = []

    for i in points:
        maximum_x = max(i.x, maximum_x)
        minimum_x = min(i.x, minimum_x)
        maximum_y = max(i.y, maximum_y)
        minimum_y = min(i.y, minimum_y)
        points_x.append(i.x)
        points_y.append(i.y)

    x = np.linspace(minimum_x - 0.5, maximum_x + 0.5, 10000)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    if linear_function is not None:
        ax.plot(x, linear_function(x), "r", linewidth=2.0, label="linear")
    if square_function is not None:
        ax.plot(x, square_function(x), "g", linewidth=2.0, label="square")
    if cubic_function is not None:
        ax.plot(x, cubic_function(x), "b", linewidth=2.0, label="cube")
    if degree_function is not None:
        ax.plot(x, degree_function(x), "pink", linewidth=2.0, label="degree")
    x = np.linspace(0.000001, maximum_x + 0.5, 10000)
    if exponential_function is not None:
        ax.plot(x, exponential_function(x), "darkred", linewidth=2.0, label="exp")
    if ln_function is not None:
        ax.plot(x, ln_function(x), "purple", linewidth=2.0, label="ln")

    ax.legend()
    ax.plot(points_x, points_y, linewidth=0, marker=".", markersize=10, markeredgecolor="black", markerfacecolor="green")

    ax.set(xlim=(minimum_x - 0.5, maximum_x + 0.5), xticks=np.arange(minimum_x, maximum_x, 0.5),
           ylim=(minimum_y - 0.5, maximum_y + 0.5), yticks=np.arange(minimum_y, maximum_y, 0.5))

    plt.show()
