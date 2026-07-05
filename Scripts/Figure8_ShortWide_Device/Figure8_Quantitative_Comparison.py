# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 00:54:45 2025

@author: ryasmin
"""

# -*- coding: utf-8 -*-
"""
Bar chart of Avg. Strain for Tip/Mid/Top with significance stars.
- Reads Tip/Mid/Top columns
- Coerces to numeric, pads to 6x10 with NaNs if short
- Reshapes to grids, flattens, drops NaNs for stats
- Draws significance bars/stars
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# === Load Data ===
file_path = r"C:\Users\nila2\OneDrive - University Of Oregon\Rubiya PhD All\COMSOL Design\Experiments\TRY\TipMidTop_LongG5.xlsx"
sheet_name = "Sheet1"  # or 0
df = pd.read_excel(file_path, sheet_name=sheet_name)

# === Config ===
rows, cols = 6, 10  # target grid
need = rows * cols

plt.rcParams.update({
    'text.usetex': True,
    'font.family': 'serif',
    'font.serif': ['Computer Modern Roman'],
    'mathtext.fontset': 'cm',
    
})

def to_numeric_series(s):
    """Coerce to numeric; preserve NaNs (non-numeric -> NaN)."""
    return pd.to_numeric(s, errors="coerce")

def pad_and_reshape(series, r, c):
    """
    Ensure length r*c by padding with NaN if needed, then reshape.
    Does NOT drop NaNs (so counts are preserved).
    """
    vals = to_numeric_series(series).values
    # strip trailing all-NaNs at the end that come from blank rows
    # (optional; comment out if you want to keep them)
    # while vals.size > 0 and np.isnan(vals[-1]):
    #     vals = vals[:-1]

    # Keep exactly r*c elements: pad with NaN if short, truncate if long
    if vals.size < r * c:
        vals = np.concatenate([vals, np.full(r * c - vals.size, np.nan)])
    vals = vals[: r * c]
    return vals.reshape(r, c)

# --- Build grids (handles short columns) ---
tip_grid = pad_and_reshape(df["Tip"], rows, cols)
mid_grid = pad_and_reshape(df["Mid"], rows, cols)
top_grid = pad_and_reshape(df["Top"], rows, cols)

# --- Flatten and combine; drop NaNs for stats/plotting ---
tip_flat = tip_grid.flatten()
mid_flat = mid_grid.flatten()
top_flat = top_grid.flatten()

tip_clean = tip_flat[~np.isnan(tip_flat)]
mid_clean = mid_flat[~np.isnan(mid_flat)]
top_clean = top_flat[~np.isnan(top_flat)]

print(f"Counts (non-NaN): Tip={tip_clean.size}, Mid={mid_clean.size}, Top={top_clean.size}")

df_layers = pd.DataFrame({
    "Strain": np.concatenate([tip_clean, mid_clean, top_clean]),
    "Region": (["Tip"] * tip_clean.size) + (["Mid"] * mid_clean.size) + (["Top"] * top_clean.size)
})
region_order = ["Tip", "Mid", "Top"]

# === Pairwise t-tests (independent; NaNs removed) ===
p_tip_mid = ttest_ind(tip_clean, mid_clean, equal_var=False, nan_policy="omit").pvalue
p_mid_top = ttest_ind(mid_clean, top_clean, equal_var=False, nan_policy="omit").pvalue
p_tip_top = ttest_ind(tip_clean, top_clean, equal_var=False, nan_policy="omit").pvalue

def pval_to_stars(p):
    return "****" if p < 1e-4 else "***" if p < 1e-3 else "**" if p < 1e-2 else "*" if p < 0.05 else "ns"

# === Plot Bar Chart with Stars ===
plt.figure(figsize=(5, 6))
palette = ['#e41a1c', '#9e9e9e', '#1f77b4']  # red, gray, blue
ax = sns.barplot(
    data=df_layers, x="Region", y="Strain",
    order=region_order, ci="sd", estimator=np.nanmean, palette=palette
)

# Use data range to position the significance bars nicely
group_means = df_layers.groupby("Region")["Strain"].mean()
y_base = group_means.max()
y_min, y_max_data = df_layers["Strain"].min(), df_layers["Strain"].max()
yrange = y_max_data - y_min if np.isfinite(y_max_data - y_min) and (y_max_data - y_min) > 0 else 1.0

h = 0.05 * yrange   # bar height
pad = 0.03 * yrange # gap above bars

# Tip vs Mid
x1, x2 = 0, 1
y = y_base + pad
plt.plot([x1, x1, x2, x2], [y, y + h, y + h, y], lw=1.5, c='k')
plt.text((x1 + x2) / 2, y + h + 0.01 * yrange, pval_to_stars(p_tip_mid), ha='center', va='bottom')

# Mid vs Top
x1, x2 = 1, 2
y += h + pad
plt.plot([x1, x1, x2, x2], [y, y + h, y + h, y], lw=1.5, c='k')
plt.text((x1 + x2) / 2, y + h + 0.01 * yrange, pval_to_stars(p_mid_top), ha='center', va='bottom')

# Tip vs Top
x1, x2 = 0, 2
y += h + pad
plt.plot([x1, x1, x2, x2], [y, y + h, y + h, y], lw=1.5, c='k')
plt.text((x1 + x2) / 2, y + h + 0.01 * yrange, pval_to_stars(p_tip_top), ha='center', va='bottom')

# Labels
plt.ylabel("Avg. strain")
plt.title(r"\textbf{Average Strain (Tip–Mid–Top)}")
# Make sure the top annotations fit
top_ylim = y + h + 0.06 * yrange
curr_ylim = ax.get_ylim()
plt.ylim(curr_ylim[0], max(curr_ylim[1], top_ylim))

plt.tight_layout()
plt.savefig("Barchart_Long_Figure8e.png", dpi=600, bbox_inches='tight')
plt.savefig("Barchart_Long_Figure8e.pdf", dpi=600, bbox_inches='tight')
plt.show()
