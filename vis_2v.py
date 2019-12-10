import numpy as np
import matplotlib.pyplot as plt

print('Input crd file name >>>>')
f_name_crd = input().rstrip() # 可視化するファイル名

print('Input v file name >>>>')
f_name_v = input().rstrip() # 可視化するファイル名

np_crd_x = np.loadtxt(f_name_crd,
                    delimiter=",",
                    skiprows=0,
                    usecols=(0)
                    )
np_crd_y = np.loadtxt(f_name_crd,
                    delimiter=",",
                    skiprows=0,
                    usecols=(1)
                    )

np_v_x = np.loadtxt(f_name_v,
                    delimiter=",",
                    skiprows=0,
                    usecols=(0)
                    )
np_v_y = np.loadtxt(f_name_v,
                    delimiter=",",
                    skiprows=0,
                    usecols=(1)
                    )

plt.quiver(np_crd_x[961::3],np_crd_y[961::3],np_v_x[961::3],np_v_y[961::3],angles='xy',scale_units='xy',scale=1)
plt.axes().set_aspect('equal')
#plt.savefig("sample.ps",format = 'ps')
plt.savefig("sample.png",format = 'png', dpi=1000)
plt.show()
