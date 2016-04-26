#!/usr/bin/env python
# coding:utf-8
import matplotlib.pylab as plt
import numpy as np

def bifurcate(x0, ntransient, nplot, r0, rmax, dr):
    global x
    count = int((rmax - r0) / dr)
    fig = [_Plot(r0 + dr * n, x0, ntransient, nplot) for n in range(count + 1)]
    plt.gca().set_xlim(r0, rmax)
    plt.gca().set_ylim(np.min(x), np.max(x))
    plt.xlabel('r')
    plt.ylabel('x')
    plt.title('Bifurcation Diagram')
    plt.show()

def _Plot(r, x0, ntransient, nplot):
    global x

    def logistic(x_i, r):
        return 4.0 * r * x_i * (1.0 - x_i)

    n = ntransient + nplot * 2
    x = [x0]
    for i in np.arange(n):
        x.append(logistic(x[i], r))
    x = np.array(x)
    plt.scatter([r] * nplot, x[ntransient + 1:ntransient + nplot + 1],
                color='r', s=0.1, marker='.'
               )
    plt.scatter([r] * nplot, x[ntransient + nplot + 1:n + 1],
                color='b', s=0.1, marker='.'
               )

parameters = {'x0': 0.3,
              'ntransient': 1000,
              'nplot': 50,
              'r0': 0.7,
              'rmax': 1.,
              'dr': 0.0005}

bifurcate(**parameters)
