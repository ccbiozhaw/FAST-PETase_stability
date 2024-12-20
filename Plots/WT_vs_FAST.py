import pylustrator

pylustrator.start()

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rcParams

# Set font to Arial
rcParams['font.family'] = 'Arial'

# Data
categories = ['WT PETase 30 °C', 'WT PETase 50 °C', 'FAST-PETase 30 °C', 'FAST-PETase 50 °C']
y = [-1092.4, -1048.9, -1064.1, -1109.3]
err = [22.97, 16.83, 27.22, 24.86]

# Define colors
colors = ['#87CEEB', '#0000FF', '#FA8072', '#FF0000']  # Blue and red tones for the bars

# Plot dimensions
fig_width_cm = 16
fig_height_cm = 9
fig, ax = plt.subplots(figsize=(fig_width_cm / 2.54, fig_height_cm / 2.54))


bar_width = 0.4
bar_positions = []

# Plot bars with colors
for i, category in enumerate(categories):
    bar = ax.bar(i, y[i], color=colors[i], width=bar_width, alpha=0.8, zorder=2)
    bar_positions.append(bar[0].get_height())  # Save bar height for annotation

# Add error bars
ax.errorbar(range(len(categories)), y, yerr=err, fmt='.k', capsize=5, linewidth=1)

# Set limits and labels
ax.set_ylim([-1140, -1000])
ax.set_ylabel('ΔG$_{Stability}$  / kcal · mol$^{-1}$', fontsize=10)
ax.set_xticks(range(len(categories)))
ax.set_xticklabels(categories, fontsize=10, rotation=45, ha='right')
ax.grid(axis='y', linestyle='--', zorder=1)  # Add dashed grid lines on y-axis

# First arrow (1st and 2nd bars)
x1, x2 = 0 + bar_width / 2, 1 - bar_width / 2  # Start and end points
y1, y2 = bar_positions[0], bar_positions[1]  # Heights
x_mid = (x1 + x2) / 2
ax.plot([x1, x_mid, x_mid, x2], [y1, y1, y2, y2], color='black', linestyle='-', linewidth=1)
ax.annotate('', xy=(x2, y2), xytext=(x_mid, y2), arrowprops=dict(arrowstyle='->', color='black'))
delta1 = abs(y1 - y2)
ax.text(x_mid+0.025, y1 + 5, f'{delta1:.2f} kcal · mol$^{{-1}}$', ha='left', va='top', fontsize=10)

# Second arrow (3rd and 4th bars)
x3, x4 = 2 + bar_width / 2, 3 - bar_width / 2
y3, y4 = bar_positions[2], bar_positions[3]
x_mid_2 = (x3 + x4) / 2
ax.plot([x3, x_mid_2, x_mid_2, x4], [y3, y3, y4, y4], color='black', linestyle='-', linewidth=1)
ax.annotate('', xy=(x4, y4), xytext=(x_mid_2+0.025, y4), arrowprops=dict(arrowstyle='->', color='black'))
delta2 = y3 - y4
ax.text(x_mid_2-0.025, y4 + 5, f'{-delta2:.2f} kcal · mol$^{{-1}}$', ha='right', va='top', fontsize=10)

# Layout adjustments
plt.tight_layout()
plt.savefig("WT_vs_FAST_Test.png", dpi=2500)

##% start: automatic generated code from pylustrator
#plt.figure(1).ax_dict = {ax.get_label(): ax for ax in plt.figure(1).axes}
#import matplotlib as mpl
#getattr(plt.figure(1), '_pylustrator_init', lambda: ...)()
#plt.figure(1).set_size_inches(16.000000/2.54, 9.000000/2.54, forward=True)
#plt.figure(1).axes[0].set(position=[0.1465, 0.3151, 0.8297, 0.6415])
#plt.figure(1).axes[0].texts[1].set(position=(0.5304, -1088.))
#plt.figure(1).axes[0].texts[3].set(position=(2.475, -1105.))
##% end: automatic generated code from pylustrator
plt.show()




