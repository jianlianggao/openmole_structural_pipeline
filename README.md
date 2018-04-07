# dHCP OpenMOLE workflow for structural pipeline 
Version: 1.05

## Short Description
OpenMOLE workflows for running dHCP structural pipeline.
## Description


## Key features
- CSV sampling
- Tasks
- Docker Container
## Functionality
- 
## Approaches
- 
## Instrument Data Types
- fMRI imaging (compressed NifTI format;that is  .ni.gz)

## Contributors
- [Jianliang Gao](https://github.com/jianlianggao) (Imperial College London)

## Container Contributor
- [John Cupitt] (Imperial College London)

## Website
- https://github.com/BioMedIA/dhcp-structural-pipeline

## Installation
- Please visit next.openmole.org (https://next.openmole.org/openmole.tar.gz) to download the latest OpenMOLE and run `tar xvzf openmole.tar.gz` to
extract OpenMOLE files into `openmole` directory. Then enter the `openmole` folder and run `./openmole` (on Linux system) to start OpenMOLE webUI.

- You may need OpenJDK to support OpenMOLE in your Ubuntu OS. If that is the case, you can run `sudo apt-get install openjdk-8-jre` to install OpenJDK.
## Usage Instructions
- Step 1: run `structure_pipeline_v5_pre.oms` to collect Subject IDs, session IDs and age of scans. A .csv file will be generated and stored in the input imaging data
directory.
- Step 2: run `structure_pipeline_v5_proc.oms` to execute dHCP structural pipeline to process all found imaging data.
## Help and Documentation
