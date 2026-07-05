# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 00:09:57 2026

@author: nila2
"""


import matplotlib.pyplot as plt

# --------- style ---------
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
    'legend.fontsize': BASE_FONT * 0.9,
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

# ==============================
# DATA
# ==============================

# (a)
xa_labels = ["1,2", "1,300", "100,2", "100,300"]
xa = [1,2,3,4]

ya_red  = [-2.62, -2.23, -2.24, -1.32]
ea_red  = [0.18]*4

ya_blue = [-1.78, -1.16, -0.05, -1.01]
ea_blue = [0.12]*4

p_a = 0.0073

# (b)
xb_labels = ["1,2", "1,300", "5,2", "5,300"]
xb = [1,2,3,4]

yb_red = [-2.98, -1.74, -3.74, -4.50]
eb_red = [0.22,0.20,0.22,0.22]

yb_blue = [0.04, 0.44, 0.01, 0.08]
eb_blue = [0.10]*4

p_b = 0.0594

# ==============================
# Figure
# ==============================
fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.0))
plt.subplots_adjust(hspace=0.48)

# ---------- (a) ----------
ax = axes[0]

# markers + errorbars only
ax.errorbar(xa, ya_red, yerr=ea_red, fmt='o', color=COLOR_RED,
            ecolor=COLOR_ERR, capsize=6, elinewidth=1.3, markersize=5,
            mfc=COLOR_RED, mec=COLOR_RED, label='W = 1 µm')

ax.errorbar(xa, ya_blue, yerr=ea_blue, fmt='o', color=COLOR_BLUE,
            ecolor=COLOR_ERR, capsize=6, elinewidth=1.3, markersize=5,
            mfc=COLOR_BLUE, mec=COLOR_BLUE, label='W = 100 µm')

# dashed broken lines
ax.plot(xa[:2], ya_red[:2],  '--', color=COLOR_RED)
ax.plot(xa[2:], ya_red[2:], '--', color=COLOR_RED)

ax.plot(xa[:2], ya_blue[:2],  '--', color=COLOR_BLUE)
ax.plot(xa[2:], ya_blue[2:], '--', color=COLOR_BLUE)

ax.set_xticks(xa)
ax.set_xticklabels(xa_labels)
ax.set_xlabel(r"Thickness (µm) , Modulus (GPa)")
ax.set_ylabel(r"Log(Strain) LS Means")
ax.set_ylim(-3.5, 1.3)

ax.set_title(r"\textbf{(a) Thickness $\times$ Modulus $\times$ Width}")

leg = ax.legend(title=f"Width (µm)\nP = {p_a:.4f}", loc='upper left')

annotate_vals(ax, xa, ya_red,  ea_red,  COLOR_RED,
              ('below','above','above','below'))
annotate_vals(ax, xa, ya_blue, ea_blue, COLOR_BLUE,
              ('above','above','above','above'))

# ---------- (b) ----------
ax = axes[1]

ax.errorbar(xb, yb_red, yerr=eb_red, fmt='o', color=COLOR_RED,
            ecolor=COLOR_ERR, capsize=6, elinewidth=1.3, markersize=5,
            mfc=COLOR_RED, mec=COLOR_RED, label='D = 1 µm')

ax.errorbar(xb, yb_blue, yerr=eb_blue, fmt='o', color=COLOR_BLUE,
            ecolor=COLOR_ERR, capsize=6, elinewidth=1.3, markersize=5,
            mfc=COLOR_BLUE, mec=COLOR_BLUE, label='D = 50 µm')

# dashed broken lines
ax.plot(xb[:2], yb_red[:2],  '--', color=COLOR_RED)
ax.plot(xb[2:], yb_red[2:], '--', color=COLOR_RED)

ax.plot(xb[:2], yb_blue[:2],  '--', color=COLOR_BLUE)
ax.plot(xb[2:], yb_blue[2:], '--', color=COLOR_BLUE)

ax.set_xticks(xb)
ax.set_xticklabels(xb_labels)
ax.set_xlabel(r"Length (mm) , Modulus (GPa)")
ax.set_ylabel(r"Log(Strain) LS Means")
ax.set_ylim(-5.2, 0.9)

ax.set_title(r"\textbf{(b) Length $\times$ Modulus $\times$ Displacement}")

leg = ax.legend(title=f"Displacement (µm)\nP = {p_b:.4f}", loc='lower left')

annotate_vals(ax, xb, yb_red,  eb_red,  COLOR_RED,
              ('above','above','below','below'))
annotate_vals(ax, xb, yb_blue, eb_blue, COLOR_BLUE,
              ('above','below','above','above'))

# ---------- save ----------
plt.tight_layout()
plt.savefig("Figure_5.png", dpi=1000, bbox_inches='tight')
plt.savefig("Figure_5.pdf", dpi=1000, bbox_inches='tight')
plt.show()