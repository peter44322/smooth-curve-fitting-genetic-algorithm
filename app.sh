#! /usr/bin/env python
from matplotlib import pyplot as plt
import numpy as np

import sys
from point import Point
from fitting import Fitting


def polyCoefficients(x, coeffs):
    o = len(coeffs)
    y = 0
    for i in range(o):
        y += coeffs[i]*x**i
    return y


filePath = sys.argv[1]

with open(filePath, "r") as file:
    text = file.read()

testCases = text.split("\n")
fig, axs = plt.subplots(
    int(testCases[0]), sharex=True, sharey=True, gridspec_kw={'hspace': 0})

case = 0
i = 1
while(i < len(testCases)):
    pointsNum, degree = testCases[i].split(" ")
    i += 1
    points = list(map(lambda p: Point(*p.split(' ')),
                      testCases[i:i+int(pointsNum)]))
    i += int(pointsNum)
    fitting = Fitting(points, int(degree))
    fitting.evolve()
    print("Points :", pointsNum)
    print(fitting.bestEver, "Error :", fitting.bestEver.fitness())
    x = np.linspace(-10, 10, num=100)
    axs[case].plot(x, polyCoefficients(x, fitting.bestEver.coefficients))
    axs[case].scatter(list(map(lambda x: x.x, points)),
                      list(map(lambda x: x.y, points)), c='r', s=3)
    case += 1

for ax in axs:
    ax.label_outer()

plt.show()
