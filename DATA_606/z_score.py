import pandas as pd
import numpy as np
import scipy.stats as st

mean = 98.2
std= 0.73
z1 = (mean*0.97 - mean) / std

# Get z score for percentile
perc = 0.03
st.norm.ppf(perc)
print(st.norm.cdf(z1)* 100)

# Chapter 5
pop_size = 2.5e7
#df = pd.DataFrame({'pop': np.arange(pop_size)})
#df['status'] = ['support'] * int(pop_size * 0.88) + ['not'] * int(pop_size*0.12)
#df = pd.DataFrame({'stat': ['support'] * int(pop_size * 0.88) + ['not'] * int(pop_size*0.12)})

arr = np.array([1] * int(pop_size * 0.88) + [0] * int(pop_size*0.12))
ps = [np.random.choice(arr, 1000).sum()/1000 for i in range(1000)]

import pdb; pdb.set_trace()
