# Convergence Studies for WindSE
**Jordan Perr-Sauer, CSCI 5636, Fall 2021**

This repository contains examples of mesh refinement for selected examples from the [NREL WindSE project](https://github.com/NREL/WindSE). The purpose of these examples is to provide evidence towards a validation study of WindSE.

## Quickstart

1. Download WindSE and place it in the root of this repository. `./WindSE`

2. Follow the installation instructions of WindSE to install a conda environment and install WindSE. We will refer to this environment as `windse_env` in this guide. Activate this environment and ensure you can run an example in the WindSE examples folder.

3. Use the windse_env to run the examples in this repo.

## Goal

This demo extends the built-in 3 turbine demo to test convergence with respect to model parameters (such as mesh resolution, thickness of disks, number of ALM nodes,radius of ALM gaussians) for objectives and derivatives. Plots:

- power (for each turbine) vs DOFS
- ∂power / ∂mivs DOFS
- repeat the previous two plots for other model parameters