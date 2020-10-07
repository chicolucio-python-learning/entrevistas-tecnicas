import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 10000)

functions = {'constant': np.full(len(x), 1),
             'logarithm': np.log2(x),
             'linear': x,
             'sublinear': x * np.log2(x),
             'quadractic': x**2,
             'cubic': x**3,
             'exponential': 2**x,
             }

fig, ax = plt.subplots(figsize=(8, 6), facecolor=(1.0, 1.0, 1.0))

limit = 8000

for function in functions:
    y = functions[function]
    y = np.ma.masked_where(np.logical_or(y > limit, y <= 0), y)
    ax.plot(x, y, label=function)
    ax.set_ylim(-100, limit)
    ax.legend()

fig2, ax2 = plt.subplots(figsize=(8, 6), facecolor=(1.0, 1.0, 1.0))

limit = 2 ** 62

for function in functions:
    y = functions[function]
    y = np.ma.masked_where(np.logical_or(y > limit, y <= 0), y)
    ax2.plot(x, y, label=function)
    ax2.set_yscale('log')
    ax2.set_xscale('log')
    ax2.legend()

plt.show()
fig.savefig('images/functions.png', dpi=fig.dpi, bbox_inches='tight')
fig2.savefig('images/functions_log.png', dpi=fig.dpi, bbox_inches='tight')
