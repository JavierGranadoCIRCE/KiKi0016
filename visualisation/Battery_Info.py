import numpy as np
import matplotlib.pyplot as plt
import pickle
import pandas as pd
import seaborn as sns

y = x = [1851,2159,	2236,1433,1708,	1073,	635,	869,	1053,	787,	879,	718,	861,	856,	690,	787,	533,	558,	1013,	1016,	853,	869,	841,	859,	916,	708,	875,	730,	756,	741,	702,	703,	647,	616,	624,	965,	1050,	701,	650,	615,	598,	326,	170,	464,	361,	471,	507,	545,	596,	505,	491,	520,	509,	525,	523,	489,	531,	520,	540,	562,	524,	487,	498,	495,	541,	522,	507,	519,	544,	546,	526,	486,	560,	502,	487,	480,	530,	452,	492,	487,	479,	514,	449,	745,	1008,	1062,	1114,	1047,	827,	666,	1835,	827,	1038,	1077,	816,	931,	815,	857,	875,	1637,	1314,	1145,	1154,	812,	771,	1001,	824,	988,	1027,	849,	540,	857,	934,	730,	1283,	1157,	1092,	922,	1934,	1155,	795,	785,	939,	1800]


df1 = pd.Series(y)
plt.figure(dpi=200)
plt.hist(df1, density = True, edgecolor ='w', label = 'Number of Cycles')
sns.kdeplot(y,label = 'Distribution Rate')
 

plt.legend()

plt.show()

