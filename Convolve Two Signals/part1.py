
#..............PROJECT1 / PART1...........................

import numpy as np
from pylab import figure, show
from numpy import arange, sin, pi
from matplotlib.pylab import *


t = arange(0.0, 1.0, 0.001)

fig = figure()

ax1 = fig.add_subplot(2,2,1)
signal1=10* sin(2*pi*5*t)
ax1.plot(t,signal1)
ax1.grid(True)
ax1.set_ylim( (-20,20) )
ax1.set_ylabel('5 Hz')
ax1.set_title('Signal 1 [Amp=10, Frq=5Hz]')

for label in ax1.get_xticklabels():
    label.set_color('r')


ax2 = fig.add_subplot(2,2,2)
signal2=200* sin(2*pi*50*t)
ax2.plot(t,signal2)
ax2.grid(True)
ax2.set_ylim( (-250,250) )
ax2.set_ylabel('50 Hz')
ax2.set_title('Signal 2 [Amp=200, Frq=50Hz]')


for label in ax2.get_xticklabels():
    label.set_color('r')


ax3 = fig.add_subplot(2,2,3)
signal3=np.convolve(signal1,signal2,mode="same")
ax3.plot(t,signal3)
ax3.grid(True)
ax3.set_ylim( (-8000,8000) )
ax3.set_ylabel('Convolution')
ax3.set_title('Signal 3 [Convolution of Signal 1 and 2]')



show()

fig.savefig('part1.pdf')
