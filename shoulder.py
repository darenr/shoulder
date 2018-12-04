from __future__ import division
from __future__ import print_function

import numpy as np
import math


def shoulder(seq, slope, direction="descending"):
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
        x_new = np.linspace(x[0], x[-1], 5*len(y))

        if direction == "descending":
            max_ror = 90
            for i in range(len(x_new) - 1):
                ror = (f(x_new[i]+1)-f(x_new[i])) / (x_new[i+1]-x_new[i])
                slope = max(0, math.degrees(math.atan(ror)))
                print(x_new[i], 'ror', ror, 'slope', slope)

        import matplotlib.pyplot as plt
        y_new = f(x_new)
        plt.plot(x,y,'o', x_new, y_new)
        plt.show()



    return None




if __name__ == '__main__':
    seq = [110, 103, 98, 85, 86, 33, 24, 19, 13, 11, 6, 3, 2, 1]
    shoulder(seq, 45)
