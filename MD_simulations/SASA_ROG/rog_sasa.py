import mdtraj as md
import pandas as pd
import numpy as np
import glob
import os

# Define the folder containing trajectories
trajectory_folder = "/home/peter/Documents/dataheart/PETase/FAST_30"  # Change this to your folder
topology_file = "reference_fast.pdb"  # Change this if needed

# Find all production trajectory files
trajectory_files = sorted(glob.glob(os.path.join(trajectory_folder, "production_*.h5")))

# Initialize dictionaries to store results
rg_data = {}
sasa_data = {}

# Process each trajectory file
for traj_file in trajectory_files:
    print(f"Processing {traj_file}...")

    # Load trajectory, selecting every 1000th frame
    traj = md.load(traj_file, top=topology_file, stride=100)

    # Superpose only the selected frames
    traj.superpose(traj, frame=0)

    # Compute radius of gyration
    rg = md.compute_rg(traj)

    # Compute SASA
    sasa = md.shrake_rupley(traj, mode='residue')
    sasa_total = np.sum(sasa, axis=1)  # Sum over all residues

    # Store results
    replicate_name = os.path.basename(traj_file).replace(".h5", "")
    rg_data[replicate_name] = rg
    sasa_data[replicate_name] = sasa_total

# Convert to DataFrame
rg_df = pd.DataFrame(rg_data)
sasa_df = pd.DataFrame(sasa_data)

# Save to Excel files
rg_df.to_excel(os.path.join(trajectory_folder, "radius_of_gyration.xlsx"), index=False)
sasa_df.to_excel(os.path.join(trajectory_folder, "sasa.xlsx"), index=False)

print("Analysis complete. Results saved to Excel files.")
