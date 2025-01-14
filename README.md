## This is the GitHub repository for the publication: 

#  Computational Analysis Reveals Temperature-Induced Stabilization of FAST-PETase

Peter Stockinger[1,2], Cornel Niederhauser [2], Sebastien Farnaud [1]§, and Rebecca Buller [2]§

<sub>1 Research Centre for Health & Life Sciences, Coventry University, CV1 5FB, Coventry, United Kingdom</sub><br />
<sub>2 Competence Center for Biocatalysis, Zurich University of Applied Sciences, Einsiedlerstrasse 31, 8820 Wädenswil, Switzerland</sub><br />
<sub>§ corresponding authors

## Overview 
This repository contains code and supplementary data for the publication "Computational Analysis Reveals Temperature-Induced Stabilization of FAST-PETase".

## Software Requirements
The code has been tested on the following systems:
- Ubuntu 22.04 LTS
- Ubuntu 24.04 LTS

**Python Dependencies** <br />
We recommend to replicate out utilized conda environments to ensure compatibility of Python dependencies. 
For this purpose, we provide separate YAML files for both:
- calculations (sim.yml)
- plots (plots.yml)
  
You can create the Conda environments from YAML file with the following commands:

For calculations:

```
conda env create -f sim.yml
conda activate sim
```
For plots:

```
conda env create -f plots.yml
conda activate plots
```
Please note, that the energy calculations rely on external standalone software of EvoEF1, EvoEF2 and FoldX.

## Methods and Code Availability
We provide relevant data and code snippets utilized for:

a) CNAnalysis 
https://cpclab.uni-duesseldorf.de/cna/

b) Analysis of MD Trajectories
- Secondary structure analysis
- Hydrogen bonding analysis
- 
https://openmm.org/documentation
https://mdtraj.org/1.9.4/analysis.html


c) Energy of unfolding calculation 
Please note, that the energy calculations rely on external standalone software of EvoEF1, EvoEF2 and FoldX:
https://zhanggroup.org/EvoEF/
https://github.com/tommyhuangthu/EvoEF
https://github.com/tommyhuangthu/EvoEF2
https://foldxsuite.crg.eu/

## Citation
Please cite the following publication if you found this ressource helpful:
t.b.d.
