# Analysis

What you need to start here:

- A copy or symlink of the GASPAR executable (named `gaspar`) in the source code of this directory;
- The `uv` tool for installing Python dependencies needed. Alternatively, installing `matplotlib` with `pip` should be enough.

Then run:

```bash
uv venv
source .venv/bin/activate
uv sync --locked
```

For this conference, three sets of analyses were conducted:

## Simulated Datasets (`simulated`)

Generated with TREvoSim externally (the same ones currently present at the [GASPAR source code repository](https://github.com/henrieger/gaspar/tree/main/data/)). This work used only the 32 and 64 taxa varieties. These simulations do NOT generate most parsimonious trees, but attempt to create realistic morphological matrices from statistic models. The "correct" MPTs were calculated using TNT.

The process of execution of this simulation involves running first
`./generate_tnt_files` to convert the original GASPAR files to ones compatible with TNT, then
`./run` to execute both the TNT and GASPAR analyses, compare the results of both and output a table to `result.csv

## Hexapoda empirical dataset (`hexapoda`)

Originally present in the work by Barbosa *et al.* (2024), this is a dataset of general morphological characters for every order of the Hexapoda clade. This was used as a benchmark dataset to assess correctness of parsimony, likelihood and Bayesian inference of phylogenies, as the correct tree is a well established relationship corroborated by multiple sources of data and methodologies.

To run the analyses here, first execute `./generate_config_files` to expand the `hexapoda_base.gas` configuration file to the 1000 independent replicates. Then use `./run <THREAD_AMOUNT>` to execute all analysis using the GNU Parallel utility. At last, `python histogram.py` outputs a file called `histogram.pdf` containing all charts for the distributions of of lengths, rearrangements and generations for all GASPAR executions. The TNT execution was done manually with the file `hexapoda_base.tnt`.

## Ornithischia empirical dataset (`ornithischia`)

> [!WARNING]
> Do **NOT** execute this pipeline in a regular home computer. Use a server (or regular computer) with at least 256GB of RAM. Failure will lead to OOM interruptions.

This is a modified version of the comprehensive morphological matrix published by Fonseca *et al.* (2024) on ornithischian dinosaur evolution. Different from the original, this one considers all characters as unordered, since GASPAR is not yet capable of ordered parsimony calculation. Also, some characters and taxa were pruned, as this version was focused solely in resolving the position of "silesaurids", animals which are usually clumped together outside of Dinosauria, a vision these data suggest shoud actually be reviewed; parsimony inference places them as a series of basal ornithischians.

The pipeline for execution is exactly the same as for the [hexapoda](#hexapoda-empirical-dataset-hexapoda) dataset. **Bear in mind**, though, that since this pipeline generates A LOT MORE DATA, it should **NOT** be executed in a home (desktop/laptop) computer. The complete pipeline was done in a remote server from the Laboratório de Biologia e Genética de Peixes from IBB-UNESP. Yes, even the generation of the charts. These analyses require a lot of RAM (at least 250GB), as all the replicates genrate heaps of data.
