# -*- coding: utf-8 -*-
"""
Created on Tue May 20 23:46:47 2025

@author: ryasmin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# === Load Data ===
file_path = r"C:\Users\nila2\OneDrive - University Of Oregon\Rubiya PhD All\COMSOL Design\Experiments\TRY\TipMidTop.xlsx" # Replace with full path if needed
sheet_name = "Sheet1"  # or 0
df = pd.read_excel(file_path, sheet_name=sheet_name)

plt.rcParams.update({
    'text.usetex': True,
    'font.family': 'serif',
    'font.serif': ['Computer Modern Roman'],
    'mathtext.fontset': 'cm',
    
})

# === Reshape Tip, Mid, Top layers ===
rows, cols = 6, 10
tip_grid = df["Tip"].values[:rows * cols].reshape((rows, cols))
mid_grid = df["Mid"].values[:rows * cols].reshape((rows, cols))
top_grid = df["Top"].values[:rows * cols].reshape((rows, cols))

# === Flatten and Combine ===
tip_flat = tip_grid.flatten()
mid_flat = mid_grid.flatten()
top_flat = top_grid.flatten()

df_layers = pd.DataFrame({
    "Strain": np.concatenate([tip_flat, mid_flat, top_flat]),
    "Region": ["Tip"] * len(tip_flat) + ["Mid"] * len(mid_flat) + ["Top"] * len(top_flat)
})

region_order = ["Tip", "Mid", "Top"]

# === Perform Pairwise t-tests ===
p_tip_mid = ttest_ind(tip_flat, mid_flat).pvalue
p_mid_top = ttest_ind(mid_flat, top_flat).pvalue
p_tip_top = ttest_ind(tip_flat, top_flat).pvalue

def pval_to_stars(p):
    if p < 0.0001:
        return "****"
    elif p < 0.001:
        return "***"
    elif p < 0.01:
        return "**"
    elif p < 0.05:
        return "*"
    else:
        return "ns"

# === Plot Bar Chart with Stars ===
# === Plot Bar Chart with Taller Bars ===
plt.figure(figsize=(5, 6))  # Increase height
palette = sns.color_palette("coolwarm", len(region_order))
ax = sns.barplot(data=df_layers, x="Region", y="Strain", order=region_order, ci="sd", palette=palette)
plt.ylim(0, df_layers["Strain"].max() * 1.25)  # Optional: expand Y range for visual clarity

# Add significance annotations manually
y_max = df_layers.groupby("Region")["Strain"].mean().max()
h = 0.0015  # height of lines

# Tip vs Mid
x1, x2 = 0, 1
y = y_max + h
plt.plot([x1, x1, x2, x2], [y, y + h, y + h, y], lw=1.5, c='k')
plt.text((x1 + x2) / 2, y + h + 0.0003, pval_to_stars(p_tip_mid), ha='center')

# Mid vs Top
x1, x2 = 1, 2
y += 2 * h
plt.plot([x1, x1, x2, x2], [y, y + h, y + h, y], lw=1.5, c='k')
plt.text((x1 + x2) / 2, y + h + 0.0003, pval_to_stars(p_mid_top), ha='center')

# Tip vs Top
x1, x2 = 0, 2
y += 2 * h
plt.plot([x1, x1, x2, x2], [y, y + h, y + h, y], lw=1.5, c='k')
plt.text((x1 + x2) / 2, y + h + 0.00001, pval_to_stars(p_tip_top), ha='center')

# Labels
plt.ylabel("Avg. strain")
plt.title(r"\textbf{Average Strain (Tip–Mid–Top)}")
plt.tight_layout()
plt.savefig("Barchart_Short_Figure7e.png", dpi=600, bbox_inches='tight')
plt.savefig("Barchart__Short_Figure7e.pdf", dpi=600, bbox_inches='tight')
plt.show()

# === Optional Save ===
# plt.savefig("avg_strain_tip_mid_top_with_stars.png", dpi=300)

