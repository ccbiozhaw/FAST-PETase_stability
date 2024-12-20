import os
import subprocess
import csv

def repair_pdb(input_pdb, output_folder):
    repair_command = f"/home/cornel/Documents/FoldX/foldx_20241231 --command=RepairPDB --pdb={input_pdb}"
    subprocess.run(repair_command, shell=True)

    # Extract filename without extension
    file_name = os.path.splitext(os.path.basename(input_pdb))[0]
    repair_file = f"{file_name}_Repair.pdb"

    # Use absolute path of input PDB for temporary file
    repair_file_path = os.path.join(os.path.dirname(input_pdb), repair_file)  # Get directory from input_pdb
    output_path = os.path.join(output_folder, repair_file)
    os.rename(repair_file_path, output_path)
    return output_path

def compute_stability(input_pdb):
    stability_command = f"/home/cornel/Documents/FoldX/foldx_20241231 --command=Stability --pdb={input_pdb}"
    result = subprocess.check_output(stability_command, shell=True, text=True)
    
    # Extract stability value from output
    for line in result.split('\n'):
        if line.startswith("Total"):
            stability = line.split()[2]
            return stability

def process_pdb_files(input_folder, output_folder, output_csv):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each pdb file in input folder
    with open(output_csv, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Filename", "Stability"])

        for file in os.listdir(input_folder):
            if file.endswith(".pdb"):
                pdb_file = os.path.join(input_folder, file)
                repair_file = repair_pdb(pdb_file, output_folder)
                stability = compute_stability(repair_file)
                csv_writer.writerow([file, stability])

if __name__ == "__main__":
    input_folder = ""
    output_folder = ""
    output_csv = ""
    process_pdb_files(input_folder, output_folder, output_csv)