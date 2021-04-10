import numpy as np


def dotproduct(n):
    import datetime
    start = datetime.datetime.now()

    ax = np.array([np.arange(n) ** 2, np.arange(n) ** 3])
    ay = ax.transpose()
    np.dot(ax, ay)

    end = datetime.datetime.now()
    return (end - start).microseconds


print(dotproduct(1000000))
