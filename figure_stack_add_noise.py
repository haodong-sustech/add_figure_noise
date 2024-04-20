import numpy as np
import imageio.v2 as io
from math import floor
import matplotlib.pyplot as plt

data = io.volread('parallel3d_stack.tif')
height = floor(data.shape[2]/10)
ext = height * 2

p1, s1 = np.mean(data[:, :, 0:height]), np.std(data[:, :, 0:height])
ext_z = np.random.normal(p1, s1, (data.shape[0], data.shape[1], ext))

data_ext = np.append(ext_z, data, axis=2)
data_ext = np.append(data_ext, ext_z, axis=2)

io.volsave('parallel3d_stack_ext.tif', data_ext)


