# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy
import matplotlib.pyplot as plt

t=numpy.arange(0,12,0.1)
print(t)

amp = numpy.sin(t)
plt.plot(t,amp)
plt.grid(True)
plt.xlabel('Time (s)',)
plt.ylabel('Amplitude(arb. unit)')
plt.show()
