# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 22:41:36 2025

@author: nila2
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 22:18:16 2025

@author: nila2
"""

# -*- coding: utf-8 -*-
"""
3D Volumetric Strain Plot — 600 dpi Export
Author: Tanvir
"""

# === IMPORT LIBRARIES ===
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl

# === LOAD EXCEL FILE ===
file_path = r"C:\Users\nila2\OneDrive - University Of Oregon\Rubiya PhD All\COMSOL Design\Experiments\TRY\LongTryDiffCutlineV2.xlsx"
xls = pd.ExcelFile(file_path)
df = xls.parse("Sheet1")

# === RENAME COLUMNS ===
df.columns = ['X', 'Y', 'Strain']

# === CLEAN DATA ===
df["X"] = pd.to_numeric(df["X"], errors='coerce')
df["Y"] = pd.to_numeric(df["Y"], errors='coerce')
df["Strain"] = pd.to_numeric(df["Strain"], errors='coerce')
df.dropna(inplace=True)

# === SYNTHETIC Z COORDINATE ===
np.random.seed(42)
df["Z"] = np.random.normal(loc=0, scale=0.02, size=len(df))

# === CONVERT TO MICROMETERS ===
df[["X", "Y", "Z"]] = df[["X", "Y", "Z"]] * 1e3

# === PUBLICATION FONT + STYLE ===
mpl.rcParams.update({
    'text.usetex': True,                     # LaTeX fonts
    'font.family': 'serif',
    'font.serif': ['Computer Modern Roman'], # Whole figure uses CM Roman
    'mathtext.fontset': 'cm',

    'font.size': 14,
    'axes.labelsize': 16,
    'axes.titlesize': 16,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'axes.linewidth': 1.2,
})

# === 3D SCATTER ===
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

sc = ax.scatter(df["X"], df["Y"], df["Z"],
                c=df["Strain"],
                cmap='turbo',
                s=8,
                edgecolors='none',
                alpha=0.9)

# === COLORBAR ===
cbar = plt.colorbar(sc, ax=ax, pad=0.1)
cbar.set_label(r"\textbf{Strain}", fontsize=14)   # bold label
cbar.formatter.set_powerlimits((0, 0))
cbar.update_ticks()

# === AXES LABELS ===
ax.set_xlabel(r"\textbf{X (µm)}", labelpad=10)
ax.set_ylabel(r"\textbf{Y (µm)}", labelpad=10)
ax.set_zlabel(r"\textbf{Z (µm)}", labelpad=10)

# === BOLD TITLE ===
ax.set_title(r"\textbf{3D Volumetric Strain Distribution}", pad=0.92)

# === FINAL LAYOUT ===
ax.grid(False)
ax.view_init(elev=10, azim=330)
plt.tight_layout()

# === SAVE AT TRUE 600 DPI ===
plt.savefig("3D_Long_Figure8a.png",
            dpi=600,
            format='png',
            bbox_inches='tight',
            transparent=False)
plt.savefig("3D_Long_Figure8a.pdf",
            dpi=600,
            format='pdf',
            bbox_inches='tight',
            transparent=False)

plt.show()
