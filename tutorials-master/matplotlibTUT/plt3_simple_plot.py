# View more python tutorials on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

# 3 - simple plot
"""
Please note, this script is for python3+.
If you are using python2+, please modify it accordingly.
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1000, 100)
y = 6000 * 350 / (300 + x)
# y = x**2
plt.plot(x, y)

x = np.linspace(0, 1000, 100)
y = 6000 * 300 / (300 + x)
# y = x**2
plt.plot(x, y)
plt.show()
