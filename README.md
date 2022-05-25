## Qiime Kernel

This repository contains the making for adding a Qiime focused kernel to a Jupyter Notebook

This kernel is meant to be used by anyone who is using the CIRC JupyterHub interface. 

**This repository only needs to be cloned once per Qiime2 conda versions**.  

To use:

1. Clone this repository into the `share/jupyter/kernels/` directory under the Qiime2 conda environment.
2. Update the paths in the *kernel.json* and *python-wrapper* files.


### Optional, but highly recommended

#### Change Jupter settings so the editor takes up the full browser
1. Under your home directory, make the directory, `.jupyter/custom` if it does not exist
2. Create the file **custom.css** and add the line `.container { width:99% !important; }` to it.
