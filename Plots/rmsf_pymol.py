import re
import pandas as pd

# Pfade zu den Dateien
pdb_file_path = r'C:/Users/nieu/OneDrive - ZHAW/PETase/Paper/7sh6.pdb'
rmsf_file_path = r'C:/Users/nieu/OneDrive - ZHAW/PETase/Paper/delta_rmsf.xlsx'

# RMSF-Daten aus Excel-Datei laden
rmsf_data = pd.read_excel(rmsf_file_path, header=None)
amino_acid_positions = rmsf_data.iloc[1:, 8]  # Annahme: Spalte C ist die 3. Spalte (index 2)
rmsf_values = rmsf_data.iloc[1:, 9]  # Annahme: Spalte D ist die 4. Spalte (index 3)

# Nur Werte für den Bereich 50-290 filtern
filtered_rmsf_data = {int(amino_acid_positions.iloc[i]): rmsf_values.iloc[i] for i in range(len(amino_acid_positions)) if 50 <= int(amino_acid_positions.iloc[i]) <= 290}

# Minimum und Maximum der gefilterten Werte bestimmen
min_rmsf = min(filtered_rmsf_data.values())
max_rmsf = max(filtered_rmsf_data.values())

# PDB-Datei einlesen und B-Faktoren ersetzen
updated_lines = []
with open(pdb_file_path, 'r') as pdb_file:
    for line in pdb_file:
        if line.startswith('ATOM') or line.startswith('HETATM'):
            res_id = int(line[22:26].strip())
            if 50 <= res_id <= 290:
                if res_id in filtered_rmsf_data:
                    b_factor = f"{filtered_rmsf_data[res_id]:6.2f}"
                    line = line[:60] + b_factor.rjust(6) + line[66:]
                updated_lines.append(line)
        elif line.startswith('TER'):
            updated_lines.append(line)

# Aktualisierte PDB-Datei speichern
output_file_path = pdb_file_path.replace('.pdb', '_updated.pdb')
with open(output_file_path, 'w') as output_file:
    output_file.writelines(updated_lines)

print(f"Die aktualisierte PDB-Datei wurde gespeichert unter: {output_file_path}")
print(f"Das Minimum des RMSF-Wertes im Bereich 50-290 ist: {min_rmsf:.2f}")
print(f"Das Maximum des RMSF-Wertes im Bereich 50-290 ist: {max_rmsf:.2f}")

# Pymol-Funktion zur Einfärbung mit benutzerdefinierten Farben
try:
    import pymol
    from pymol import cmd

    colors_blue = ['#0000FF', '#1E90FF', '#00BFFF', '#87CEEB', '#ADD8E6']  # Blautöne
    colors_red = ['#FF0000', '#FF4500', '#FF6347', '#FA8072', '#FFA07A']    # Rottöne
    gradient_colors = colors_blue + colors_red  # Farbverlauf von Blau nach Rot

    def color_by_rmsf(selection="all"):
        step = (max_rmsf - min_rmsf) / (len(gradient_colors) - 1)
        for i, color in enumerate(gradient_colors):
            cmd.set_color(f"custom_color_{i}", [int(color[1:3], 16) / 255.0, int(color[3:5], 16) / 255.0, int(color[5:7], 16) / 255.0])
            min_value = min_rmsf + i * step
            max_value = min_rmsf + (i + 1) * step if i < len(gradient_colors) - 1 else max_rmsf
            cmd.spectrum("b", f"custom_color_{i}", selection, minimum=min_value, maximum=max_value)

    print("PyMOL-Einfärbung basierend auf benutzerdefinierten Farben ist bereit zur Verwendung.")
except ImportError:
    print("PyMOL ist nicht installiert. Bitte installieren Sie PyMOL, um die Einfärbung zu verwenden.")

