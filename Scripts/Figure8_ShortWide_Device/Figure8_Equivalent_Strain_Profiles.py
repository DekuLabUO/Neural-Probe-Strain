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
    'legend.fontsize': 20 * font_scaling,
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'axes.linewidth': 1.4
})

# -------- Load data --------
file2_csv_path = 'NeuropixelData-45.csv'
neuro = pd.read_csv(file2_csv_path)

# Rename columns to expected names
neuro.columns = ['Tip_X', 'Tip_Y', 'Mid_X', 'Mid_Y', 'Surface_X', 'Surface_Y']

# Convert X values from mm to µm
neuro['Tip_X']     *= 1000
neuro['Mid_X']     *= 1000
neuro['Surface_X'] *= 1000

# -------- Colors for lines --------
col_tip = '#1f77b4'   # blue
col_mid = '#d62728'   # red
col_top = '#2ca02c'   # green

# -------- Single merged plot (no secondary y-axis) --------
fig, ax = plt.subplots(figsize=(5, 4))

# Line style with markers (like the image)
line_kwargs = dict(
    linewidth=2.0,
    marker='o',
    markersize=5,
    markeredgecolor='white',
    markeredgewidth=0.6
)

# Plot Tip, Mid, Top(Surface) together
ax.plot(neuro['Tip_X'],     neuro['Tip_Y'],     label='Tip', color=col_tip, **line_kwargs)
ax.plot(neuro['Mid_X'],     neuro['Mid_Y'],     label='Mid', color=col_mid, **line_kwargs)
ax.plot(neuro['Surface_X'], neuro['Surface_Y'], label='Top', color=col_top, **line_kwargs)

# Labels / limits
ax.set_xlabel('Distance (µm)')
ax.set_ylabel('Equivalent Strain um/um')   # left-side y-axis title
ax.set_xlim(0, 250)

# Box-style axes (all spines visible, a bit heavier)
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(1.4)

# Legend: boxed style with three entries
ax.legend(
    loc='upper right',
    frameon=True, fancybox=True,
    framealpha=0.9, facecolor='white', edgecolor='0.75'
)

# Title
ax.set_title('Equivalent Strain (Tip–Mid–Top) of the MEA')

plt.tight_layout()
plt.savefig("Equivalent_Linegraph__Long_Figure8b.pdf", format='pdf', bbox_inches='tight', dpi=1000)
plt.savefig("Equivalent_Linegraph_Long_Figure8b.png", format='png', bbox_inches='tight', dpi=1000, transparent=False)  
plt.show()
