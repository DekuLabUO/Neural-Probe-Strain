# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 17:36:39 2026

@author: nila2
"""


import matplotlib.pyplot as plt

# ---------- Style ----------
COLOR_RED  = '#d62728'
COLOR_BLUE = '#0343df'
COLOR_ERR  = 'black'
BASE_FONT  = 15

plt.rcParams.update({
    'text.usetex': True,
    'font.family': 'serif',
    'font.serif': ['Computer Modern Roman'],
    'mathtext.fontset': 'cm',
    'font.size': BASE_FONT,
    'axes.titlesize': BASE_FONT * 1.05,
    'axes.labelsize': BASE_FONT * 1.0,
    'legend.fontsize': BASE_FONT * 0.95,
})

def annotate_vals(ax, xs, ys, es, color, where):
    for x, y, e, pos in zip(xs, ys, es, where):
        if pos == 'above':
            ax.annotate(f"{y:.2f}", (x, y + e), xytext=(0, 6),
                        textcoords='offset points', ha='center', va='bottom',
                        color=color, fontweight='bold')
        else:
            ax.annotate(f"{y:.2f}", (x, y - e), xytext=(0, -6),
                        textcoords='offset points', ha='center', va='top',
                        color=color, fontweight='bold')

# ---------- Data ----------
labels = [
    "1,1,2", "1,1,300", "1,100,2", "1,100,300",
    "100,1,2", "100,1,300", "100,100,2", "100,100,300"
]
x = list(range(1, len(labels) + 1))

y_red = [-4.63, -4.53, -4.63, -2.73, -3.62, -2.72, -0.56, -2.50]
e_red = [0.22]*8
pos_red = ['below','below','below','below','above','below','above','below']

y_blue = [-0.61, 0.07, 0.15, 0.09, 0.07, 0.40, 0.46, 0.48]
e_blue = [0.10]*8
pos_blue = ['above']*8

p_value = 0.0182

# ---------- Figure ----------
fig, ax = plt.subplots(figsize=(7.2, 6.2))

# -------- markers + errorbars only --------
ax.errorbar(x, y_red, yerr=e_red, fmt='o', color=COLOR_RED,
            ecolor=COLOR_ERR, capsize=6, elinewidth=1.3, markersize=5,
            mfc=COLOR_RED, mec=COLOR_RED, label='D = 1 µm')

ax.errorbar(x, y_blue, yerr=e_blue, fmt='o', color=COLOR_BLUE,
            ecolor=COLOR_ERR, capsize=6, elinewidth=1.3, markersize=5,
            mfc=COLOR_BLUE, mec=COLOR_BLUE, label='D = 50 µm')

# -------- dashed broken lines (RED) --------
# break: (2→3), (4→5), (6→7)
ax.plot(x[0:2], y_red[0:2], '--', color=COLOR_RED)   # 1-2
ax.plot(x[2:4], y_red[2:4], '--', color=COLOR_RED)   # 3-4
ax.plot(x[4:6], y_red[4:6], '--', color=COLOR_RED)   # 5-6
ax.plot(x[6:8], y_red[6:8], '--', color=COLOR_RED)   # 7-8

# -------- dashed broken lines (BLUE) --------
# break: (2→3), (4→5), (6→7)
ax.plot(x[0:2], y_blue[0:2], '--', color=COLOR_BLUE)  # 1-2
ax.plot(x[2:4], y_blue[2:4], '--', color=COLOR_BLUE)  # 3-4
ax.plot(x[4:6], y_blue[4:6], '--', color=COLOR_BLUE)  # 5-6
ax.plot(x[6:8], y_blue[6:8], '--', color=COLOR_BLUE)  # 7-8

# ---------- axes ----------
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=30, ha='right')
ax.set_xlabel("Width (µm) , Thickness (µm) , Modulus (GPa)")
ax.set_ylabel("Log(Strain) LS Means")
ax.set_ylim(-6.0, 1.1)

ax.set_title(r"\textbf{Width $\times$ Thickness $\times$ Modulus $\times$ Displacement}")

# ---------- legend ----------
leg = ax.legend(title=f"Displacement (µm)\nP = {p_value:.4f}",
                loc='lower right')

# ---------- annotations ----------
annotate_vals(ax, x, y_red,  e_red,  COLOR_RED,  pos_red)
annotate_vals(ax, x, y_blue, e_blue, COLOR_BLUE, pos_blue)

# ---------- final ----------
for s in ax.spines.values():
    s.set_linewidth(1.2)

ax.grid(False)

plt.tight_layout()
plt.savefig("Figure_6.png", dpi=1000, bbox_inches='tight')
plt.savefig("Figure_6.pdf", dpi=1000, bbox_inches='tight')
plt.show()