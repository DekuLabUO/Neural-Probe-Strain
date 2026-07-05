# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 16:32:53 2025

@author: nila2
"""

# -*- coding: utf-8 -*-
"""
2x2 Subplots (Red Data Only) — Extracted from Figure
Author: Tanvir
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.rcParams.update(mpl.rcParamsDefault)

# ---------- GLOBAL COLORS ----------
COLOR_RED = '#d62728'
COLOR_ERR = 'black'

# ---------- FONT SCALING FACTORS ----------
BASE_FONT = 15
SCALE_AXIS_LABEL = 1.2
SCALE_TITLE = 1.3
SCALE_LEGEND = 0.9
SCALE_LEGEND_TITLE = 1
SCALE_TICK = 1.0
SCALE_ANNOTATION = 0.9

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

# plt.rcParams.update({
#     'text.usetex': False,                 # disable LaTeX rendering
#     'font.family': 'serif',
#     'font.serif': ['Times New Roman'],    # use Times New Roman everywhere
#     'mathtext.fontset': 'dejavuserif',    # ensures math blends with Times

#     'font.size': BASE_FONT * SCALE_TICK,
#     'axes.titlesize': BASE_FONT * SCALE_TITLE,
#     'axes.labelsize': BASE_FONT * SCALE_AXIS_LABEL,
#     'legend.fontsize': BASE_FONT * SCALE_LEGEND,
#     'xtick.labelsize': BASE_FONT * SCALE_TICK,
#     'ytick.labelsize': BASE_FONT * SCALE_TICK
# 
# ---------------- Plot Data ----------------
plot1_x, plot1_y, plot1_p_value, plot1_se = [1, 5],   [-1.060, -2.042], 0.0007, 0.1388
plot2_x, plot2_y, plot2_p_value, plot2_se = [1, 100], [-2.104, -0.998], 0.0003, 0.1388
plot3_x, plot3_y, plot3_p_value, plot3_se = [1, 100], [-1.948, -1.155], 0.0029, 0.1388
plot4_x, plot4_y, plot4_p_value, plot4_se = [1, 50],  [-3.241,  0.139], 0.0001, 0.1388

# ---------- Annotation Helper ----------
def annotate_manual(ax, x, y, err, color, positions, font_scale=1.0, offset_x=None):
    if offset_x is None:
        offset_x = [0] * len(x)
    for xi, yi, ei, pos, ox in zip(x, y, err, positions, offset_x):
        offset_y = 10
        fontsize = BASE_FONT * SCALE_ANNOTATION * font_scale
        ymin, ymax = ax.get_ylim()
        upper = min(yi + ei, ymax - 0.02*(ymax - ymin))
        lower = max(yi - ei, ymin + 0.02*(ymax - ymin))
        if pos == 'above':
            ax.annotate(f"{yi:.3f}", xy=(xi, upper),
                        xytext=(ox, offset_y), textcoords='offset points',
                        ha='center', va='bottom', color=color,
                        fontweight='bold', fontsize=fontsize)
        elif pos == 'below':
            ax.annotate(f"{yi:.3f}", xy=(xi, lower),
                        xytext=(ox, -offset_y), textcoords='offset points',
                        ha='center', va='top', color=color,
                        fontweight='bold', fontsize=fontsize)

# ---------- Function for scaled legend ----------
def set_scaled_legend(ax, title_text, se_text, loc='best'):
    return ax.legend(
        title=f"{title_text}\n{se_text}",
        loc=loc,
        frameon=True,
        fontsize=BASE_FONT * SCALE_LEGEND,
        title_fontsize=BASE_FONT * SCALE_LEGEND_TITLE
    )

# ---------- Figure ----------
fig, axs = plt.subplots(2, 2, figsize=(11, 8.6))

# ---------- (a) Length ----------
ax = axs[0, 0]
ax.errorbar(plot1_x, plot1_y, yerr=[plot1_se]*2, fmt='o--', color=COLOR_RED,
            ecolor=COLOR_ERR, capsize=6, elinewidth=1.5, markersize=6,
            mfc=COLOR_RED, mec=COLOR_RED, label='Length', clip_on=True)
ax.set_xscale('log')
ax.set_xticks(plot1_x)
ax.set_xticklabels([str(x) for x in plot1_x])
ax.get_xaxis().set_minor_formatter(plt.NullFormatter())
ax.get_xaxis().set_major_formatter(plt.FixedFormatter([str(x) for x in plot1_x]))
ax.set_xlabel("Length (mm)")
ax.set_ylabel("Log(Strain) LS Means")
ax.set_ylim(-2.5, -0.8)
set_scaled_legend(ax, f"$P = {plot1_p_value}$", f"$SE = {plot1_se:.4f}$", loc='best')
ax.set_title(r"\textbf{(a)}")
annotate_manual(ax, plot1_x, plot1_y, [plot1_se]*2, COLOR_ERR, ['below', 'below'], offset_x=[6, -5])

# ---------- (b) Width ----------
ax = axs[0, 1]
ax.errorbar(plot2_x, plot2_y, yerr=[plot2_se]*2, fmt='o--', color=COLOR_RED,
            ecolor=COLOR_ERR, capsize=6, elinewidth=1.5, markersize=6,
            mfc=COLOR_RED, mec=COLOR_RED, label='Width', clip_on=True)
ax.set_xscale('log')
ax.set_xticks(plot2_x)
ax.set_xticklabels([str(x) for x in plot2_x])
ax.set_xlabel("Width (µm)")
ax.set_ylabel("Log(Strain) LS Means")
ax.set_ylim(-2.3, -0.8)
set_scaled_legend(ax, f"$P = {plot2_p_value}$", f"$SE = {plot2_se:.4f}$", loc='best')
ax.set_title(r"\textbf{(b)}")
annotate_manual(ax, plot2_x, plot2_y, [plot2_se]*2, COLOR_ERR, ['above', 'below'], offset_x=[6, -5])

# ---------- (c) Thickness ----------
ax = axs[1, 0]
ax.errorbar(plot3_x, plot3_y, yerr=[plot3_se]*2, fmt='o--', color=COLOR_RED,
            ecolor=COLOR_ERR, capsize=6, elinewidth=1.5, markersize=6,
            mfc=COLOR_RED, mec=COLOR_RED, label='Thickness', clip_on=True)
ax.set_xscale('log')
ax.set_xticks(plot3_x)
ax.set_xticklabels([str(x) for x in plot3_x])
ax.set_xlabel("Thickness (µm)")
ax.set_ylabel("Log(Strain) LS Means")
ax.set_ylim(-2.2, -1.0)
set_scaled_legend(ax, f"$P = {plot3_p_value}$", f"$SE = {plot3_se:.4f}$", loc='best')
ax.set_title(r"\textbf{(c)}")
annotate_manual(ax, plot3_x, plot3_y, [plot3_se]*2, COLOR_ERR, ['above', 'below'], offset_x=[6, -5])

# ---------- (d) Displacement ----------
ax = axs[1, 1]
ax.errorbar(plot4_x, plot4_y, yerr=[plot4_se]*2, fmt='o--', color=COLOR_RED,
            ecolor=COLOR_ERR, capsize=6, elinewidth=1.5, markersize=6,
            mfc=COLOR_RED, mec=COLOR_RED, label='Displacement', clip_on=True)
ax.set_xscale('log')
ax.set_xticks(plot4_x)
ax.set_xticklabels([str(x) for x in plot4_x])
ax.set_xlabel("Displacement (µm)")
ax.set_ylabel("Log(Strain) LS Means")
ax.set_ylim(-3.8, 0.5)
set_scaled_legend(ax, r"$P < 0.0001$", f"$SE = {plot4_se:.4f}$", loc='best')
ax.set_title(r"\textbf{(d)}")
annotate_manual(ax, plot4_x, plot4_y, [plot4_se]*2, COLOR_ERR, ['above', 'below'], offset_x=[6, -5])

# ---------- Final touches ----------
for ax in axs.flat:
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.2)
    ax.grid(False)

plt.tight_layout()
plt.savefig("Figure3_Not_Bold.pdf", format='pdf', bbox_inches='tight', dpi=600)
plt.savefig("Figure3_Not_Bold.png", format='png', bbox_inches='tight', dpi=600, transparent=False)
plt.show()
