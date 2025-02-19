import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Schriftart auf Arial setzen
rcParams['font.family'] = 'Arial'

# Dateipfade
file_path_fast = './RoG_comparison_FAST.xlsx'
file_path_wt = './RoG_comparison_WT.xlsx'

# Sheet-Namen
sheet_fast = 'Sheet1'
sheet_wt = 'Sheet1'

# Daten laden
fast_data = pd.read_excel(file_path_fast, sheet_name=sheet_fast)
wt_data = pd.read_excel(file_path_wt, sheet_name=sheet_wt)

# Farben definieren
colors_blue = ['#0000FF', '#1E90FF', '#00BFFF', '#87CEEB', '#ADD8E6']  # Blautöne
colors_red = ['#FF0000', '#FF4500', '#FF6347', '#FA8072', '#FFA07A']    # Rottöne
colors = colors_blue + colors_red

# Plot-Dimensionen
fig_width_cm = 16
fig_height_cm = 9
fig, axes = plt.subplots(1, 2, figsize=(fig_width_cm / 2.54, fig_height_cm / 2.54), sharex=True, sharey=True)

# X-Achsen-Beschränkung
x_limits = (0, 100)

# Transparenz-Wert
alpha_value = 0.7

# WT-Plot (links)
x_wt = wt_data.iloc[:, 10]  # Werte aus Spalte K
for i, column in enumerate(wt_data.columns[:10]):  # Spalten A bis J
    axes[0].plot(x_wt, wt_data[column], label=column, color=colors[i], alpha=alpha_value)
axes[0].set_xlabel("Simulation time (ns)", fontsize=10)
axes[0].set_ylabel("Radius of gyration (nm)", fontsize=10)
axes[0].grid(axis='y', linestyle='--')  # Nur waagrechte Gitterlinien
axes[0].set_xlim(x_limits)  # X-Achsen-Begrenzung setzen
axes[0].text(0.02, 0.95, 'a', transform=axes[0].transAxes, fontsize=12, fontweight='bold', va='top', ha='left')  # "a" hinzufügen
axes[0].set_title("WT-PETase", fontsize=12, fontweight='bold')

# FAST-Plot (rechts)
x_fast = fast_data.iloc[:, 10]  # Werte aus Spalte K
for i, column in enumerate(fast_data.columns[:10]):  # Spalten A bis J
    axes[1].plot(x_fast, fast_data[column], label=column, color=colors[i], alpha=alpha_value)
axes[1].set_xlabel("Simulation time (ns)", fontsize=10)
axes[1].grid(axis='y', linestyle='--')  # Nur waagrechte Gitterlinien
axes[1].set_xlim(x_limits)  # X-Achsen-Begrenzung setzen
axes[1].text(0.02, 0.95, 'b', transform=axes[1].transAxes, fontsize=12, fontweight='bold', va='top', ha='left')  # "b" hinzufügen
axes[1].set_title("FAST-PETase", fontsize=12, fontweight='bold')


handles, labels = axes[0].get_legend_handles_labels()
blue_handles = handles[:5]  # Erste fünf Linien (blaue Farben)
blue_labels = labels[:5]
red_handles = handles[5:]  # Zweite fünf Linien (rote Farben)
red_labels = labels[5:]

# Abwechselnde Reihenfolge erstellen
legend_handles = [handle for pair in zip(blue_handles, red_handles) for handle in pair]
legend_labels = [label for pair in zip(blue_labels, red_labels) for label in pair]

fig.legend(
    legend_handles,
    legend_labels,
    loc='lower center',
    frameon=False,
    ncol=5,
    fontsize=8,
)

# Layout-Anpassungen
plt.subplots_adjust(
    top=0.903,
    bottom=0.245,
    left=0.098,
    right=0.978,
    hspace=0.195,
    wspace=0.126
)
plt.savefig("RoG_Comparison_Combined.png", dpi=1000, bbox_inches='tight')
plt.show()

print("Abbildung gespeichert als 'RMSD_Comparison_Combined.png'")


