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
        for i in range(len(x_new) - 1):
            rise = f(x_new[i])-f(x_new[i+1])
            run = x_new[i+1]-x_new[i]
            ror =  rise / run
            slope = max(0, math.degrees(math.atan(ror)))
            if direction == "descending":
                if slope:
                    if True: #slope < previous_slope:
                        print(x_new[i], 'rise', rise, 'run', run, 'ror', ror, 'slope', slope)
                        if slope < target_slope:
                            # project back the position on the original x axis
                            v = (x_new[i]+x_new[i+1])/2
                            print('v', v)
                            break
                previous_slope = slope

        if plot_it:
            import matplotlib.pyplot as plt
            y_new = f(x_new)
            plt.plot(x,y,'o', x_new, y_new)
            plt.show()



    return None




if __name__ == '__main__':
    seq = [110, 103, 98, 85, 86, 33, 24, 19, 13, 11, 6, 3, 2, 1]
    shoulder(seq, 82, plot_it=True)
