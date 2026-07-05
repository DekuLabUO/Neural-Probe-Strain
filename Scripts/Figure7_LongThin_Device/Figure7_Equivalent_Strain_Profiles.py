# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 21:43:40 2025

@author: ryasmin
"""

import pandas as pd
import matplotlib.pyplot as plt

# -------- Font / figure style --------
font_scaling = 0.5
plt.rcParams.update({
    'font.size': 26 * font_scaling,
    'axes.titlesize': 26 * font_scaling,
    'axes.labelsize': 26 * font_scaling,
    'xtick.labelsize': 16 * font_scaling,
    'ytick.labelsize': 16 * font_scaling,
    'legend.fontsize': 18 * font_scaling,
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'axes.linewidth': 1.4
})

# -------- Load data --------
file1_csv_path = 'MichiganData-45.csv'
michigan = pd.read_csv(file1_csv_path)

# Rename columns to expected names
michigan.columns = ['Tip_X', 'Tip_Y', 'Mid_X', 'Mid_Y', 'Surface_X', 'Surface_Y']

# Convert X values from mm to µm
michigan['Tip_X']     *= 1000
michigan['Mid_X']     *= 1000
michigan['Surface_X'] *= 1000

# -------- Colors (distinct) --------
col_tip = '#d62728'  # red 
col_mid = '#1f77b4'   # red
col_top = '#2ca02c'   # green

# -------- Single merged plot --------
fig, ax = plt.subplots(figsize=(5, 4))

# Add lines WITH markers (like your image)
line_kwargs = dict(linewidth=2.0, marker='o', markersize=5,
                   markeredgecolor='white', markeredgewidth=0.6)

ax.plot(michigan['Tip_X'],     michigan['Tip_Y'],     label='Tip',
        color=col_tip, **line_kwargs)
ax.plot(michigan['Mid_X'],     michigan['Mid_Y'],     label='Mid',
        color=col_mid, **line_kwargs)
ax.plot(michigan['Surface_X'], michigan['Surface_Y'], label='Top',
        color=col_top, **line_kwargs)   # Surface shown as "Top" per your convention

# Axes labels / limits
ax.set_xlabel('Distance (µm)')
ax.set_ylabel('Equivalent Strain um/um')   # exact wording requested
ax.set_xlim(0, 250)

# Box style like the image: keep full spines and slightly heavier edges
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(1.4)

# Legend in a light box (like the screenshot)
legend = ax.legend(loc='upper right', frameon=True, fancybox=True,
                   framealpha=0.9, facecolor='white', edgecolor='0.75')

# Title
ax.set_title('Equivalent Strain (Tip–Mid–Top) of the MEA')

plt.tight_layout()
plt.savefig("Equivalent_Linegraph__Short_Figure7b.pdf", format='pdf', bbox_inches='tight', dpi=1000)
plt.savefig("Equivalent_Linegraph_Short_Figure7b.png", format='png', bbox_inches='tight', dpi=1000, transparent=False)  
plt.show()
