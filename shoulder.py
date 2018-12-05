from __future__ import division
from __future__ import print_function

import numpy as np
import math


def shoulder(seq, target_slope, direction="descending", plot_it=False):
    if seq:
        if isinstance(seq, np.ndarray):
            y = seq
        else:
            y = np.array(seq)

        x = xrange(len(y))
        # calculate polynomial
        z = np.polyfit(x, y, 4)
        f = np.poly1d(z)

        # calculate new x's and y's
        x_new = np.linspace(x[0], x[-1], 1*len(y))

        previous_slope = 0 if direction == "descending" else 90
        #
        # initially for direction == "descending" we ignore all loop
        # iterations for which the slope increases. Once it starts to
        # fall we find the point where the slope exceeds the target
        #
        p = f(x_new[0])-f(x_new[1])
        deltas = []
        # use maxheap to store the deltas
        for i in range(len(x_new) - 1):
            rise = f(x_new[i])-f(x_new[i+1])
            if direction == "descending":
                print(x_new[i], 'rise', rise)
                if rise < p:
                    deltas.append((x_new[i], p-rise))
                p = rise

        # find max of delta list
        j = sorted(deltas, key=lambda x: x[1], reverse=True)[0][0] + 1
        print(j)

        if plot_it:
            import matplotlib.pyplot as plt
            y_new = f(x_new)
            plt.plot(x,y,'o', x_new, y_new)
            plt.show()



    return None




if __name__ == '__main__':
    seq = [110, 103, 98, 85, 86, 33, 24, 19, 13, 11, 6, 3, 2, 1]
    shoulder(seq, 82, plot_it=True)
