import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
import matplotlib.patches as mpatches
from scipy import stats

# Set font to Arial
rcParams['font.family'] = 'Arial'

# Previous data loading code remains the same
file_path_fast = './FAST_hydrogen_bonding_analysis_full.xlsx'
file_path_wt = './WT_hydrogen_bonding_analysis_full.xlsx'
sheet_fast = 'Tabelle1'
sheet_wt = 'Tabelle1'
fast_data = pd.read_excel(file_path_fast, sheet_name=sheet_fast)
wt_data = pd.read_excel(file_path_wt, sheet_name=sheet_wt)
fast_data['Group'] = 'FAST-PETase'
wt_data['Group'] = 'WT-PETase'
combined_data = pd.concat([wt_data[['Delta', 'Group']], fast_data[['Delta', 'Group']]])

# Define colors
color_blue = '#1E90FF'  # Blue for WT-PETase
color_red = '#FF4500'   # Red for FAST-PETase

# Plot dimensions
fig_width_cm = 8
fig_height_cm = 12
fig, ax = plt.subplots(figsize=(fig_width_cm / 2.54, fig_height_cm / 2.54))

# Add horizontal grid lines (ensure they are in the background)
ax.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)  # Set zorder to 0 for grid lines

def overlay_histogram(data, x_pos, color, orientation='left'):
    bins = np.arange(-1.1, 0.8 + 0.05, 0.05)  # Fixed bins to align both histograms with bar width of 0.05
    counts, bin_edges = np.histogram(data, bins=bins)  # Raw counts, no density normalization
    bin_width = 0.05
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

    # Plot the raw counts (not density)
    for i in range(len(counts)):
        if orientation == 'left':
            rect = plt.Rectangle((x_pos - counts[i], bin_centers[i] - bin_width / 2),
                                  counts[i], bin_width,
                                  facecolor=color, alpha=0.8, edgecolor='black', linewidth=0.5, zorder=3)  # Set zorder to 3 for bars
        else:
            rect = plt.Rectangle((x_pos, bin_centers[i] - bin_width / 2),
                                  counts[i], bin_width,
                                  facecolor=color, alpha=0.8, edgecolor='black', linewidth=0.5, zorder=3)  # Set zorder to 3 for bars
        ax.add_patch(rect)

    return np.max(counts)

# Get data and plot
wt_data_delta = combined_data[combined_data['Group'] == 'WT-PETase']['Delta']
fast_data_delta = combined_data[combined_data['Group'] == 'FAST-PETase']['Delta']

overlay_histogram(wt_data_delta, 0, color_blue, 'left')
overlay_histogram(fast_data_delta, 0, color_red, 'right')

# Create legend - smaller and without box
blue_patch = mpatches.Patch(color=color_blue, label='WT-PETase')
red_patch = mpatches.Patch(color=color_red, label='FAST-PETase')
plt.legend(handles=[blue_patch, red_patch], loc='upper left', frameon=False, prop={'size': 8})

# Plot settings
ax.set_ylabel("Δ bonding distance (50 - 30 °C)", fontsize=10)
ax.set_xlabel("Number of Entries", fontsize=10)  # Label changed to reflect number of entries
ax.set_title("Hydrogen Bonding Comparison", fontsize=12, fontweight='bold')

# Adjust y-axis
ax.set_ylim(-1.1, 0.8)  # Fixed y-axis range from -1.1 to 0.8
ax.set_yticks(np.arange(-1.1, 0.9, 0.2))

# Adjust x-axis
ax.set_xlim(-30, 30)  # Adjust x-axis range to reflect -30 to 0 on the left and 0 to 30 on the right
ax.set_xticks([-30, -20, -10, 0, 10, 20, 30])

# Vertical line at x=0
ax.axvline(x=0, color='black', linestyle='-', linewidth=0.5, zorder=3)

# Layout adjustments
plt.subplots_adjust(
    top=0.9,
    bottom=0.1,
    left=0.1,
    right=0.95
)

plt.savefig("Hydrogen_Bonding_Comparison.svg", bbox_inches='tight')
plt.show()
