import numpy as np
import matplotlib.pyplot as plt

nc = 30
rl1 = 10
rl2 = 20

nc1 = nc+1
nl = rl1+1


interface_start = (nc1 * nc1) + 4 * nc * (nl-1)

print('Input crd file name >>>>')
f_name_crd = input().rstrip() # 可視化するファイル名

print('Input v file name >>>>')
f_name_v = input().rstrip() # 可視化するファイル名

print('Input interface plot data >>>>')
f_name_interface = input().rstrip()

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

np_interface_x = np.loadtxt(f_name_interface,
                          delimiter=',',
                          skiprows=0,
                          usecols=(0)
                          )

np_interface_y = np.loadtxt(f_name_interface,
                          delimiter=',',
                          skiprows=0,
                          usecols=(1)
                          )

plt.quiver(np_crd_x,np_crd_y,np_v_x,np_v_y,angles='xy',scale_units='xy',scale=1)
for i in range(4*nc):
    if i == 4*nc - 1:
        plt.plot([np_interface_x[int(i+interface_start)], np_interface_x[int(interface_start)]], [np_interface_y[int(i+interface_start)], np_interface_y[int(interface_start)]],'k-', lw=0.7)
    else:
        plt.plot([np_interface_x[int(i+interface_start)], np_interface_x[int(i+1+interface_start)]], [np_interface_y[int(i+interface_start)], np_interface_y[int(i+1+interface_start)]],'k-', lw=0.7)

plt.axes().set_aspect('equal')
#plt.savefig("sample.ps",format = 'ps')
plt.savefig("sample.png",format = 'png', dpi=1000)
plt.show()
