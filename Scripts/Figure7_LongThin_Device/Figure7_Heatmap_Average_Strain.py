# -*- coding: utf-8 -*-
"""
Created on Tue May 20 12:46:30 2025

@author: ryasmin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# === Load Excel Data ===
file_path = r"C:\Users\nila2\OneDrive - University Of Oregon\Rubiya PhD All\COMSOL Design\Experiments\TRY\TipMidTop.xlsx"  # Make sure this file is in your working directory
xls = pd.ExcelFile(file_path)
df = xls.parse("Sheet1")

# === Define Grid Dimensions ===
rows, cols = 6, 6  # 60 total values
plt.rcParams.update({
    'text.usetex': True,
    'font.family': 'serif',
    'font.serif': ['Computer Modern Roman'],
    'mathtext.fontset': 'cm',
    
})

# === Reshape Each Region ===
tip_grid = df["Tip"].values[:rows * cols].reshape((rows, cols))
mid_grid = df["Mid"].values[:rows * cols].reshape((rows, cols))
top_grid = df["Top"].values[:rows * cols].reshape((rows, cols))

# === Compute Averaged Grid ===
avg_grid = (tip_grid + mid_grid + top_grid) / 3

# === Convert to Percentage (Normalized to Max) ===
avg_grid_percent = (avg_grid / np.max(avg_grid)) * 100

# === Plot Heatmap with Region Labels ===
fig, ax = plt.subplots(figsize=(6, 5))
im = ax.imshow(avg_grid_percent, cmap='turbo', origin='lower')

# Colorbar
cbar = plt.colorbar(im, ax=ax)
cbar.set_label("Avg. strain \%")

# Annotate Tip, Mid, Top on Y-axis (inferred: rows 0–1 = Tip, 2–3 = Mid, 4–5 = Top)
ax.text(-1.5, 0.5, 'Tip', va='center', ha='right', fontsize=12, fontweight='bold', color='black', rotation=90)
ax.text(-1.5, 2.5, 'Mid', va='center', ha='right', fontsize=12, fontweight='bold', color='black', rotation=90)
ax.text(-1.5, 4.5, 'Top', va='center', ha='right', fontsize=12, fontweight='bold', color='black', rotation=90)

# Horizontal lines to separate regions
ax.hlines([1.5, 3.5], xmin=-0.5, xmax=cols - 0.5, colors='white', linestyles='--', linewidth=1.5)

# Axis ticks
ax.set_xticks([0, cols-1])
ax.set_xticklabels(['1', str(cols)])
ax.set_yticks([0, rows-1])
ax.set_yticklabels(['1', str(rows)])

# Final labels
ax.set_title("Average Strain (Tip–Mid–Top)")
plt.title(r"\textbf{Average Strain (Tip–Mid–Top)}")
ax.grid(visible=True, color='black', linewidth=0.5)
ax.grid(False)

# === Optional: Save the Figure ===
# plt.savefig("avg_strain_tip_mid_top.png", dpi=300, bbox_inches='tight')
plt.tight_layout()
plt.savefig("Heatmap_Short_Figure7d.png", dpi=600, bbox_inches='tight')
plt.savefig("Heatmap_Short_Figure7d.pdf", dpi=600, bbox_inches='tight')
plt.show()

