# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 23:33:29 2025

@author: nila2
"""

# -*- coding: utf-8 -*-
"""
3x2 Subplots — Two Colors, Black Error Bars, Manual Above/Below Annotations
Author: Tanvir
"""

import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams.update(mpl.rcParamsDefault)

# ---------- COLORS ----------
COLOR_RED  = '#d62728'
COLOR_BLUE = '#0343df'
#COLOR_ERR  = 'black'

# ---------- FONT SCALING ----------
BASE_FONT = 15
SCALE_AXIS_LABEL   = 1.2
SCALE_TITLE        = 1.3
SCALE_LEGEND       = 0.85
SCALE_LEGEND_TITLE = 1.05
SCALE_TICK         = 1.0
SCALE_ANNOTATION   = 0.9

plt.rcParams.update({
    'text.usetex': True,
    'font.family': 'serif',
    'font.serif': ['Computer Modern Roman'],
    'mathtext.fontset': 'cm',
    'font.size': BASE_FONT * SCALE_TICK,
    'axes.titlesize': BASE_FONT * SCALE_TITLE,
    'axes.labelsize': BASE_FONT * SCALE_AXIS_LABEL,
    'legend.fontsize': BASE_FONT * SCALE_LEGEND,
    'xtick.labelsize': BASE_FONT * SCALE_TICK,
    'ytick.labelsize': BASE_FONT * SCALE_TICK
})

#------------------- DATA (from your 6-panel figure) -------------------
# (a) Length × Modulus (GPa)
a_x = [2, 300]
a_red  = [-1.47, -0.65]     # Length = 1 mm
a_blue = [-1.87, -2.21]     # Length = 5 mm
a_red_err  = [0.11, 0.11]
a_blue_err = [0.11, 0.16]
a_p = 0.0166

# (b) Length × Thickness (µm)
b_x = [1, 100]
b_red  = [-1.72, -0.40]     # Length = 1 mm
b_blue = [-2.18, -1.91]     # Length = 5 mm
b_red_err  = [0.20, 0.15]
b_blue_err = [0.18, 0.16]
b_p = 0.0256

# (c) Length × Displacement (µm)
c_x = [1, 50]
c_red  = [-2.36, 0.24]      # Length = 1 mm
c_blue = [-4.12, 0.04]     # Length = 5 mm
c_red_err  = [0.25, 0.20]
c_blue_err = [0.30, 0.22]
c_p = 0.0032

# (d) Length × Width (µm)
d_x = [1, 100]
d_red  = [-1.90, -0.2]     # Length = 1 mm
d_blue = [-2.31, -1.77]     # Length = 5 mm
d_red_err  = [0.14, 0.14]
d_blue_err = [0.14, 0.14]
d_p = 0.0184

# (e) Width × Modulus (GPa)
e_x = [2, 300]
e_red  = [-2.43, -1.78]     # Width = 1 µm
e_blue = [-0.91, -1.08]     # Width = 100 µm
e_red_err  = [0.1964, 0.1964]
e_blue_err = [0.1964, 0.1964]
e_p = 0.0647

# (f) Width × Displacement (µm)
f_x = [1, 100]
f_red  = [-4.13, -2.35]     # Displacement = 1 µm
f_blue = [ -0.08,  0.35]     # Displacement = 50 µm
f_red_err  = [0.22, 0.22]
f_blue_err = [0.22, 0.22]
# P < 0.0001 in legend

# ------------------- helpers -------------------
def annotate_manual(ax, x, y, err, color, positions, offset_x=[6,-5], offset_y=6, font_scale=1.0):
    """
    Place a text label for each point either 'above' or 'below' its errorbar.
    offset_x: list of horizontal pixel offsets (positive → right, negative → left)
    offset_y: vertical offset (points)
    """
    if offset_x is None:
        offset_x = [0] * len(x)

    ymin, ymax = ax.get_ylim()
    pad = 0.02 * (ymax - ymin)

    for xi, yi, ei, pos, ox in zip(x, y, err, positions, offset_x):
        y_above = min(yi + ei, ymax - pad)
        y_below = max(yi - ei, ymin + pad)

        fontsize = BASE_FONT * SCALE_ANNOTATION * font_scale
        if pos == 'above':
            ax.annotate(f"{yi:.2f}", (xi, y_above), xytext=(ox, offset_y),
                        textcoords='offset points', ha='center', va='bottom',
                        color=color, fontweight='bold', fontsize=fontsize)
        elif pos == 'below':
            ax.annotate(f"{yi:.2f}", (xi, y_below), xytext=(ox, -offset_y),
                        textcoords='offset points', ha='center', va='top',
                        color=color, fontweight='bold', fontsize=fontsize)

def set_scaled_legend(ax, title_text, loc='best'):
    ax.legend(title=title_text, loc=loc, frameon=True,
              fontsize=BASE_FONT * SCALE_LEGEND,
              title_fontsize=BASE_FONT * SCALE_LEGEND_TITLE)

def set_ticks_clean(ax, xs):
    ax.set_xscale('log')
    ax.set_xticks(xs)
    ax.set_xticklabels([str(v) for v in xs])
    ax.get_xaxis().set_minor_formatter(plt.NullFormatter())
    ax.get_xaxis().set_major_formatter(plt.FixedFormatter([str(v) for v in xs]))

# ------------------- figure -------------------
fig, axs = plt.subplots(3, 2, figsize=(11, 12.9))

# (a)
ax = axs[0,0]
ax.errorbar(a_x, a_red,  yerr=a_red_err,  fmt='o-', color=COLOR_RED,
            ecolor=COLOR_RED, capsize=6, elinewidth=1.5, mfc=COLOR_RED, mec=COLOR_RED, label='L = 1 mm', clip_on=True)
ax.errorbar(a_x, a_blue, yerr=a_blue_err, fmt='o-', color=COLOR_BLUE,
            ecolor=COLOR_BLUE, capsize=6, elinewidth=1.5, mfc=COLOR_BLUE, mec=COLOR_BLUE, label='L = 5 mm', clip_on=True)
set_ticks_clean(ax, a_x)
ax.set_xlabel("Modulus (GPa)"); ax.set_ylabel("Log(Strain) LS Means")
ax.set_ylim(-2.6, -0.4); set_scaled_legend(ax, rf"$P = {a_p:.4f}$", loc='upper left')
ax.set_title(r"\textbf{(a) Length $\times$ Modulus}")
annotate_manual(ax, a_x, a_red,  a_red_err,  COLOR_RED,  ['above','below'])
annotate_manual(ax, a_x, a_blue, a_blue_err, COLOR_BLUE, ['below','below'])

# (b)
ax = axs[0,1]
ax.errorbar(b_x, b_red,  yerr=b_red_err,  fmt='o-', color=COLOR_RED,
            ecolor=COLOR_RED, capsize=6, elinewidth=1.5, mfc=COLOR_RED, mec=COLOR_RED, label='L = 1 mm', clip_on=True)
ax.errorbar(b_x, b_blue, yerr=b_blue_err, fmt='o-', color=COLOR_BLUE,
            ecolor=COLOR_BLUE, capsize=6, elinewidth=1.5, mfc=COLOR_BLUE, mec=COLOR_BLUE, label='L = 5 mm', clip_on=True)
set_ticks_clean(ax, b_x)
ax.set_xlabel("Thickness (µm)"); ax.set_ylabel("Log(Strain) LS Means")
ax.set_ylim(-2.6, -0.2); set_scaled_legend(ax, rf"$P = {b_p:.4f}$", loc='best')
ax.set_title(r"\textbf{(b) Length $\times$ Thickness}")
annotate_manual(ax, b_x, b_red,  b_red_err,  COLOR_RED,  ['above','below'])
annotate_manual(ax, b_x, b_blue, b_blue_err, COLOR_BLUE, ['below','below'])

# (c)
ax = axs[1,0]
ax.errorbar(c_x, c_red,  yerr=c_red_err,  fmt='o-', color=COLOR_RED,
            ecolor=COLOR_RED, capsize=6, elinewidth=1.5, mfc=COLOR_RED, mec=COLOR_RED, label='L = 1 mm', clip_on=True)
ax.errorbar(c_x, c_blue, yerr=c_blue_err, fmt='o-', color=COLOR_BLUE,
            ecolor=COLOR_BLUE, capsize=6, elinewidth=1.5, mfc=COLOR_BLUE, mec=COLOR_BLUE, label='L = 5 mm', clip_on=True)
set_ticks_clean(ax, c_x)
ax.set_xlabel("Displacement (µm)"); ax.set_ylabel("Log(Strain) LS Means")
ax.set_ylim(-4.5, 1); set_scaled_legend(ax, rf"$P = {c_p:.4f}$", loc='upper left')
ax.set_title(r"\textbf{(c) Length $\times$ Displacement}")
annotate_manual(ax, c_x, c_red,  c_red_err,  COLOR_RED,  ['above','above'])
annotate_manual(ax, c_x, c_blue, c_blue_err, COLOR_BLUE, ['above','below'])

# (d)
ax = axs[1,1]
ax.errorbar(d_x, d_red,  yerr=d_red_err,  fmt='o-', color=COLOR_RED,
            ecolor=COLOR_RED, capsize=6, elinewidth=1.5, mfc=COLOR_RED, mec=COLOR_RED, label='L = 1 mm', clip_on=True)
ax.errorbar(d_x, d_blue, yerr=d_blue_err, fmt='o-', color=COLOR_BLUE,
            ecolor=COLOR_BLUE, capsize=6, elinewidth=1.5, mfc=COLOR_BLUE, mec=COLOR_BLUE, label='L = 5 mm', clip_on=True)
set_ticks_clean(ax, d_x)
ax.set_xlabel("Width (µm)"); ax.set_ylabel("Log(Strain) LS Means")
ax.set_ylim(-2.7, -0.01); set_scaled_legend(ax, rf"$P = {d_p:.4f}$", loc='upper left')
ax.set_title(r"\textbf{(d) Length $\times$ Width}")
annotate_manual(ax, d_x, d_red,  d_red_err,  COLOR_RED,  ['above','below'])
annotate_manual(ax, d_x, d_blue, d_blue_err, COLOR_BLUE, ['below','above'])

# (e)
ax = axs[2,0]
ax.errorbar(e_x, e_red,  yerr=e_red_err,  fmt='o-', color=COLOR_RED,
            ecolor=COLOR_RED, capsize=6, elinewidth=1.5, mfc=COLOR_RED, mec=COLOR_RED, label='W = 1 µm', clip_on=True)
ax.errorbar(e_x, e_blue, yerr=e_blue_err, fmt='o-', color=COLOR_BLUE,
            ecolor=COLOR_BLUE, capsize=6, elinewidth=1.5, mfc=COLOR_BLUE, mec=COLOR_BLUE, label='W = 100 µm', clip_on=True)
set_ticks_clean(ax, e_x)
ax.set_xlabel("Modulus (GPa)"); ax.set_ylabel("Log(Strain) LS Means")
ax.set_ylim(-2.9, -0.6); set_scaled_legend(ax, rf"$P = {e_p:.4f}$", loc='lower right')
ax.set_title(r"\textbf{(e) Width $\times$ Modulus}")
annotate_manual(ax, e_x, e_red,  e_red_err,  COLOR_RED,  ['below','above'])
annotate_manual(ax, e_x, e_blue, e_blue_err, COLOR_BLUE, ['below','above'])

# (f)
ax = axs[2,1]
ax.errorbar(f_x, f_red,  yerr=f_red_err,  fmt='o-', color=COLOR_RED,
            ecolor=COLOR_RED, capsize=6, elinewidth=1.5, mfc=COLOR_RED, mec=COLOR_RED, label='D = 1 µm', clip_on=True)
ax.errorbar(f_x, f_blue, yerr=f_blue_err, fmt='o-', color=COLOR_BLUE,
            ecolor=COLOR_BLUE, capsize=6, elinewidth=1.5, mfc=COLOR_BLUE, mec=COLOR_BLUE, label='D = 50 µm', clip_on=True)
set_ticks_clean(ax, f_x)
ax.set_xlabel("Width (µm)"); ax.set_ylabel("Log(Strain) LS Means")
ax.set_ylim(-5.5, 0.8)
set_scaled_legend(ax, r"$P < 0.0001$", loc='lower right')
ax.set_title(r"\textbf{(f) Width $\times$ Displacement}")
annotate_manual(ax, f_x, f_red,  f_red_err,  COLOR_RED,  ['above','below'])
annotate_manual(ax, f_x, f_blue, f_blue_err, COLOR_BLUE, ['below','below'])

# ---- final touches ----
for ax in axs.flat:
    for s in ax.spines.values():
        s.set_visible(True); s.set_linewidth(1.2)
    ax.grid(False)

plt.tight_layout(h_pad=1.6, w_pad=1.0)
plt.savefig("Figure_4.pdf", format="pdf", bbox_inches="tight")
plt.savefig("Figure_4.png", format="png", bbox_inches="tight", dpi=600)
plt.show()
