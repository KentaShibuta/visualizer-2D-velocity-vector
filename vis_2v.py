import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np; np.random.seed(0)
import pandas as pd


import matplotlib.font_manager as fon
del fon.weight_dict['roman']
matplotlib.font_manager._rebuild()

plt.rcParams['font.family'] = 'Times New Roman' #全体のフォントを設定
plt.rcParams["mathtext.fontset"] = "stix" # これを入れておくと，斜体にするときれいになる．
# 軸を内側に入れる
plt.rcParams['xtick.direction'] = 'in' # x axis in
plt.rcParams['ytick.direction'] = 'in' # y axis in
plt.rcParams["font.size"] = 14
nc = 6
rl1 = 10
rl2 = 10

nc1 = nc+1
nl = rl1+1


#interface_start = (nc1 * nc1) + 4 * nc * (nl-1)

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
plt.xlabel('$\it{x}$'+' [m]')
plt.ylabel('$\it{y}$'+' [m]')
plt.quiver(np_crd_x,np_crd_y,np_v_x,np_v_y,angles='xy',scale_units='xy',scale=None, width=0.01)
'''
for i in range(4*nc):
    if i == 4*nc - 1:
        plt.plot([np_interface_x[int(i+interface_start)], np_interface_x[int(interface_start)]], [np_interface_y[int(i+interface_start)], np_interface_y[int(interface_start)]],'m-.', lw=1.0, label = "Interface")
    else:
        plt.plot([np_interface_x[int(i+interface_start)], np_interface_x[int(i+1+interface_start)]], [np_interface_y[int(i+interface_start)], np_interface_y[int(i+1+interface_start)]],'m-.', lw=1.0)
'''
for i in range(4*nc):
    if i == 4*nc - 1:
        plt.plot([np_interface_x[i], np_interface_x[0]], [np_interface_y[i], np_interface_y[0]],'m-.', lw=1.0, label = "Interface")
    else:
        plt.plot([np_interface_x[i], np_interface_x[i+1]], [np_interface_y[i], np_interface_y[i+1]],'m-.', lw=1.0)
plt.xlim(-0.3,0)
plt.ylim(-0.5,0.25)
#plt.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=0.1,labelspacing=0.1,fontsize=14)
plt.tight_layout()
plt.axes().set_aspect('equal')
plt.savefig("20200128_v_6668_2.png",format = 'png', dpi=1000)
#plt.savefig("sample.png",format = 'png', dpi=1000)
plt.show()
