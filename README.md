![Logo](dHCP_openmole.gif)
# dHCP OpenMOLE workflow for structural pipeline 
Version: 1.05

## Short Description
OpenMOLE workflows for running dHCP structural pipeline.
## Description
Funded by ERC, [dHCP](http://www.developingconnectome.org/) project is led by King’s College London, Imperial College London and Oxford University
and aims to make major scientific progress by creating the first 4-dimensional connectome of early life. The containerized dHCP structural pipeline
is scheduled by OpenMOLE to utilize any scale of cluster or cloud platform to performs structural analysis of neonatal brain MRI images (including T1 and T2).

## Key features
- CSV sampling
- Tasks
- Docker Container
- Structural analysis of brain MRI images

## Instrument Data Types
- fMRI imaging (compressed NifTI format;that is  .ni.gz)

## Contributors
- [Jonathan](https://github.com/jopasserat) and [Jianliang Gao](https://github.com/jianlianggao) (Imperial College London)

## Container Contributor
- [John Cupitt](https://github.com/jcupitt) (Imperial College London)

## Website
- https://github.com/BioMedIA/dhcp-structural-pipeline

## Installation
- Please visit next.openmole.org (https://next.openmole.org/openmole.tar.gz) to download the latest OpenMOLE and run `tar xvzf openmole.tar.gz` to
extract OpenMOLE files into `openmole` directory. Then enter the `openmole` folder and run `./openmole` (on Linux system) to start OpenMOLE webUI.

- You may need OpenJDK to support OpenMOLE in your Ubuntu OS. If that is the case, you can run `sudo apt-get install openjdk-8-jre` to install OpenJDK.
## Usage Instructions
- Step 1: Upload the .oms and .py files into OpenMOLE.
- Step 2: run `structure_pipeline_v5_pre.oms` to collect Subject IDs, session IDs and age of scans. A .csv file will be generated and stored in the input imaging data
directory.
- Step 3: run `structure_pipeline_v5_proc.oms` to execute dHCP structural pipeline to process all found imaging data.
## Help and Documentation
- Please take your time to follow the tutorial if you are new to OpenMOLE:
- https://next.openmole.org/GUI+guide.html
- https://next.openmole.org/Getting+started.html
- https://next.openmole.org/Models.html
- http://demo.openmole.org/app
