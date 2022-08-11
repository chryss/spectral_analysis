# spectral_analysis guide installation

## Prerequisites

- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)
- Optional [Mamba](https://mamba.readthedocs.io/en/latest/)

## Create environment

```bash
conda env create -f environment.yml
activate spectral_analysis
```

or 

```bash
mamba env create -f environment.yml
activate spectral_analysis
```

The packages necessary to run the project are now installed inside the conda environment.

**Note: The following sections assume you are located in your conda environment.**

## Set up project's module

To move beyond notebook prototyping, all reusable code should go into the `spectral_analysis/` folder package. To use that package inside your project, install the project's module in editable mode, so you can edit files in the `spectral_analysis` folder and use the modules inside your notebooks :

```bash
pip install --editable .
```

To use the module inside your notebooks, add `%autoreload` at the top of your notebook :

```python
%load_ext autoreload
%autoreload 2
```

Example of module usage :

```python
from spectral_analysis.utils.paths import data_dir
data_dir()
```


