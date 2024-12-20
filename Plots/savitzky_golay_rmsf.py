import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from matplotlib import rcParams

# Set font to Arial
rcParams['font.family'] = 'Arial'

# File paths
file_path_fast = './RMSD_comparison_FAST.xlsx'
file_path_wt = './RMSD_comparison_WT.xlsx'

# Sheet names
sheet_fast = 'RMSD_production'
sheet_wt = 'RMSD_production'

# Load data
fast_data = pd.read_excel(file_path_fast, sheet_name=sheet_fast)
wt_data = pd.read_excel(file_path_wt, sheet_name=sheet_wt)

# Define colors
colors_blue = ['#0000FF', '#1E90FF', '#00BFFF', '#87CEEB', '#ADD8E6']  # Blue shades
colors_red = ['#FF0000', '#FF4500', '#FF6347', '#FA8072', '#FFA07A']    # Red shades
colors = colors_blue + colors_red

# Savitzky-Golay Filter Function
def apply_savgol(data, window_size=11, poly_order=3):
    """Applies Savitzky-Golay filter to smooth data."""
    return savgol_filter(data, window_length=window_size, polyorder=poly_order, mode='nearest')

# Apply smoothing to data
fast_data_smoothed = fast_data.iloc[:, :10].apply(lambda col: apply_savgol(col, window_size=11, poly_order=3))
wt_data_smoothed = wt_data.iloc[:, :10].apply(lambda col: apply_savgol(col, window_size=11, poly_order=3))

# Plot dimensions
fig_width_cm = 16
fig_height_cm = 9
fig, axes = plt.subplots(1, 2, figsize=(fig_width_cm / 2.54, fig_height_cm / 2.54), sharex=True, sharey=True)

# X-axis limits
x_limits = (0, 100)

# Transparency for lines
alpha_value = 0.7

# WT Plot (left)
x_wt = wt_data.iloc[:, 10]  # Values from column K
for i, column in enumerate(wt_data_smoothed.columns):  # Columns A to J
    axes[0].plot(x_wt, wt_data_smoothed[column], label=column, color=colors[i], alpha=alpha_value)
axes[0].set_xlabel("Simulation time (ns)", fontsize=10)
axes[0].set_ylabel("RMSD (nm)", fontsize=10)
axes[0].grid(axis='y', linestyle='--')  # Horizontal grid lines only
axes[0].set_xlim(x_limits)  # Set x-axis limits
axes[0].text(0.02, 0.95, 'a', transform=axes[0].transAxes, fontsize=12, fontweight='bold', va='top', ha='left')  # Add "a"
axes[0].set_title("WT-PETase", fontsize=12, fontweight='bold')

# FAST Plot (right)
x_fast = fast_data.iloc[:, 10]  # Values from column K
for i, column in enumerate(fast_data_smoothed.columns):  # Columns A to J
    axes[1].plot(x_fast, fast_data_smoothed[column], label=column, color=colors[i], alpha=alpha_value)
axes[1].set_xlabel("Simulation time (ns)", fontsize=10)
axes[1].grid(axis='y', linestyle='--')  # Horizontal grid lines only
axes[1].set_xlim(x_limits)  # Set x-axis limits
axes[1].text(0.02, 0.95, 'b', transform=axes[1].transAxes, fontsize=12, fontweight='bold', va='top', ha='left')  # Add "b"
axes[1].set_title("FAST-PETase", fontsize=12, fontweight='bold')

# Legend
handles, labels = axes[0].get_legend_handles_labels()
blue_handles = handles[:5]  # First 5 lines (blue)
blue_labels = labels[:5]
red_handles = handles[5:]  # Next 5 lines (red)
red_labels = labels[5:]

# Create alternating legend
legend_handles = [handle for pair in zip(blue_handles, red_handles) for handle in pair]
legend_labels = [label for pair in zip(blue_labels, red_labels) for label in pair]

fig.legend(
    legend_handles,
    legend_labels,
    loc='lower center',
    frameon=False,  # No frame
    ncol=5,
    fontsize=8,
)

# Layout adjustments
plt.subplots_adjust(
    top=0.903,
    bottom=0.245,
    left=0.098,
    right=0.978,
    hspace=0.195,
    wspace=0.126
)
plt.savefig("RMSD_Comparison_Combined_Smoothed.png", dpi=5000, bbox_inches='tight')  # High resolution
plt.show()

print("Figure saved as 'RMSD_Comparison_Combined_Smoothed.png'")
