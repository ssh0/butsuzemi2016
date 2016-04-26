#!/usr/bin/env python
# coding:utf-8
from gtk_wrapper import interactive
import matplotlib.pylab as plt


class Iterate_map():

    def mapping(self, parameters):
        self.__dict__ = parameters
        x = [self.x0]
        for i in range(self.nmax):
            t = 4.0 * self.r * x[i] * (1 - x[i])
            x.append(t)
        n = range(self.nmax + 1)
        plt.plot(n, x, label='$x_{0}\ =' + str(self.x0) + ' : '
                 + 'r\ =' + str(self.r) + ' : '
                 + 'n_{\mathrm{max}}\ =' + str(self.nmax) + '$'
                 )
        if self.r > 0.25 and self.r < 0.75:
            self.drawing()
        plt.gca().set_xlim(0, self.nmax)
        plt.gca().set_ylim(-0.05, 1.0)
        plt.xlabel('$n$')
        plt.ylabel('$x$')
        plt.title('Iterate map')
        plt.legend(loc="best")
        plt.show()

    def drawing(self):
        xfi = 1. - 1. / (4. * self.r)
        plt.plot([0, self.nmax], [xfi] * 2,
                 label=r'$x = 1 - 1 / 4r = ' + str(xfi) + '$'
                 )

if __name__ == '__main__':

    def f(x0=0.6, r=0.745, nmax=400):
        pass

    run = Iterate_map()

    def button_pushed(button):
        run.mapping(w.kwargs)

    w = interactive(f, (('x0', (0., 1.0)),
                        ('r', (0., 1.0, 3)),
                        ('nmax', (100, 500)),
                        ('Run', button_pushed)
                        ),
                    title="Figure 1"
                    )
    w.display()
