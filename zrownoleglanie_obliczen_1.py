import numpy as np
import fast_histogram
from concurrent.futures import ThreadPoolExecutor
from functools import partial
import multiprocessing


print(multiprocessing.cpu_count())

np.random.seed(42)
vals = np.random.normal(size=[2, 100]).astype(np.float32)

splits = 6
with ThreadPoolExecutor(max_workers=splits) as pool:
    chunk = vals.shape[1] // splits
    chunk0 = [vals[0,i*chunk:(i+1)*chunk] for i in range(splits)]
    chunk1 = [vals[1,i*chunk:(i+1)*chunk] for i in range(splits)]
    f = partial(fast_histogram.histogram2d, bins=100, range=((-1,1),(-1,1)))
    results = pool.map(f, chunk0, chunk1)
    results = sum(results)
print(len(results))
print(len(vals))