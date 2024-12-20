import matplotlib.pyplot as plt
from matplotlib import rcParams

# Set font to Arial
rcParams['font.family'] = 'Arial'

# Data for first plot (WT_vs_FAST_EvoEF)
categories_1 = ['WT PETase 30 °C', 'WT PETase 50 °C', 'FAST-PETase 30 °C', 'FAST-PETase 50 °C']
y_1 = [201.794, 202.99, 205.562, 199.796]
err_1 = [4.866158238, 3.354302312, 4.375831807, 4.091390962]
colors_1 = ['#87CEEB', '#0000FF', '#FA8072', '#FF0000']

# Data for second plot (WT_vs_FAST_FoldX)
categories_2 = ['WT PETase 30 °C', 'WT PETase 50 °C', 'FAST-PETase 30 °C', 'FAST-PETase 50 °C']
y_2 = [57.142, 71.24, 72.894, 68.694]
err_2 = [6.165978917, 9.321242406, 4.358791576, 5.844821982]
colors_2 = ['#87CEEB', '#0000FF', '#FA8072', '#FF0000']

# Plot dimensions
fig, axes = plt.subplots(2, 1, figsize=(16 / 2.54, 18 / 2.54))

# First subplot (top)
ax1 = axes[0]
bar_width = 0.4
bar_positions_1 = []

for i, category in enumerate(categories_1):
    bar = ax1.bar(i, y_1[i], color=colors_1[i], width=bar_width, alpha=0.8, zorder=2)
    bar_positions_1.append(bar[0].get_height())
ax1.errorbar(range(len(categories_1)), y_1, yerr=err_1, fmt='.k', capsize=5, linewidth=1)
ax1.set_ylim([190, 215])
ax1.set_ylabel('ΔG$_{Stability}$  / kcal · mol$^{-1}$', fontsize=10)
ax1.set_xticks(range(len(categories_1)))
ax1.set_xticklabels(categories_1, fontsize=10, rotation=45, ha='right')
ax1.grid(axis='y', linestyle='--', zorder=1)
ax1.text(-0.35, ax1.get_ylim()[1] - 0.75, "a", fontsize=12, fontweight='bold', va='top', ha='left')

# Arrows and annotations for the first plot
x1, x2 = 0 + bar_width / 2, 1 - bar_width / 2
y1, y2 = bar_positions_1[0], bar_positions_1[1]
x_mid = (x1 + x2) / 2
ax1.plot([x1, x_mid, x_mid, x2], [y1, y1, y2, y2], color='black', linestyle='-', linewidth=1)
ax1.annotate('', xy=(x2, y2), xytext=(x_mid, y2), arrowprops=dict(arrowstyle='->', color='black'))
delta1 = abs(y1 - y2)
ax1.text(x_mid, y2+2, f'{delta1:.2f} kcal · mol$^{{-1}}$', ha='center', va='top', fontsize=10)

x3, x4 = 2 + bar_width / 2, 3 - bar_width / 2
y3, y4 = bar_positions_1[2], bar_positions_1[3]
x_mid_2 = (x3 + x4) / 2
ax1.plot([x3, x_mid_2, x_mid_2, x4], [y3, y3, y4, y4], color='black', linestyle='-', linewidth=1)
ax1.annotate('', xy=(x4, y4), xytext=(x_mid_2, y4), arrowprops=dict(arrowstyle='->', color='black'))
delta2 = abs(y3 - y4)
ax1.text(x_mid_2, y3+2, f'{-delta2:.2f} kcal · mol$^{{-1}}$', ha='center', va='top', fontsize=10)

# Second subplot (bottom)
ax2 = axes[1]
bar_positions_2 = []
for i, category in enumerate(categories_2):
    bar = ax2.bar(i, y_2[i], color=colors_2[i], width=bar_width, alpha=0.8, zorder=2)
    bar_positions_2.append(bar[0].get_height())
ax2.errorbar(range(len(categories_2)), y_2, yerr=err_2, fmt='.k', capsize=5, linewidth=1)
ax2.set_ylim([50, 85])
ax2.set_ylabel('ΔG$_{Stability}$  / kcal · mol$^{-1}$', fontsize=10)
ax2.set_xticks(range(len(categories_2)))
ax2.set_xticklabels(categories_2, fontsize=10, rotation=45, ha='right')
ax2.grid(axis='y', linestyle='--', zorder=1)
ax2.text(-0.35, ax2.get_ylim()[1] - 0.75, "b", fontsize=12, fontweight='bold', va='top', ha='left')

# Arrows and annotations for the second plot
x1, x2 = 0 + bar_width / 2, 1 - bar_width / 2
y1, y2 = bar_positions_2[0], bar_positions_2[1]
x_mid = (x1 + x2) / 2
ax2.plot([x1, x_mid, x_mid, x2], [y1, y1, y2, y2], color='black', linestyle='-', linewidth=1)
ax2.annotate('', xy=(x2, y2), xytext=(x_mid, y2), arrowprops=dict(arrowstyle='->', color='black'))
delta1 = abs(y1 - y2)
ax2.text(x_mid, y2+3, f'{delta1:.2f} kcal · mol$^{{-1}}$', ha='center', va='top', fontsize=10)

x3, x4 = 2 + bar_width / 2, 3 - bar_width / 2
y3, y4 = bar_positions_2[2], bar_positions_2[3]
x_mid_2 = (x3 + x4) / 2
ax2.plot([x3, x_mid_2, x_mid_2, x4], [y3, y3, y4, y4], color='black', linestyle='-', linewidth=1)
ax2.annotate('', xy=(x4, y4), xytext=(x_mid_2, y4), arrowprops=dict(arrowstyle='->', color='black'))
delta2 = abs(y3 - y4)
ax2.text(x_mid_2, y3+3, f'{-delta2:.2f} kcal · mol$^{{-1}}$', ha='center', va='top', fontsize=10)

# Layout adjustments
plt.tight_layout()
plt.savefig("Combined_WT_vs_FAST_Stacked.png", dpi=1000)
plt.show()
