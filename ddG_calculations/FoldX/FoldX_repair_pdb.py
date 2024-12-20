import os
import subprocess
import shutil

def repair_pdb_with_FoldX(input_folder, output_folder, FoldX_path):
    # Erstelle den Ausgabeordner, falls er nicht existiert
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Navigiere zum Ordner mit den PDB-Dateien
    os.chdir(input_folder)
    
    # Durchlaufe alle PDB-Dateien im Eingabeordner
    for pdb_file in os.listdir():
        if pdb_file.endswith(".pdb"):
            input_path = os.path.join(pdb_file)
            
            # Befehl für FoldX erstellen
            command = [FoldX_path, "--command=RepairPDB", "--pdb=" + input_path]
            
            # FoldX ausführen
            try:
                subprocess.run(command, check=True)
            except subprocess.CalledProcessError as e:
                print("Fehler beim Reparieren der Datei", pdb_file)
                print(e)
                continue
            
            # Überprüfe, ob die reparierte Datei erstellt wurde
            repaired_pdb_path = input_path.replace(".pdb", "_Repair.pdb")
            if not os.path.exists(repaired_pdb_path):
                print("Fehler: Reparierte Datei wurde nicht gefunden für", pdb_file)
                continue
            
            # Verschiebe die reparierte PDB-Datei in den Ausgabeordner
            output_path = os.path.join(output_folder, os.path.basename(repaired_pdb_path))
            shutil.move(repaired_pdb_path, output_path)
            print("Reparierte Datei gespeichert unter", output_path)


# Aufruf des Skripts
if __name__ == "__main__":
    input_folder = "/home/cornel/Documents/FoldX"
    output_folder = "/home/cornel/Documents/FoldX/Repaired_pdb_files"
    FoldX_path = "./foldx_20241231"
    
    repair_pdb_with_FoldX(input_folder, output_folder, FoldX_path)
