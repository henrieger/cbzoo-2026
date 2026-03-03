# Poster

This is the directory that contains all LaTeX code for the poster presented at the conference. The file `main.tex` has all the main content and `beamerthemestyle.sty` defines the custom beamer theme.

To generate the final PDF, simply run:

```bash
make

```

Or, if you want the complete command:

```bash
pdflatex main.tex
pdflatex main.tex

```

Yes, the same command twice. Some of the decorations made with the `tikz` package require double compilation to render correctly.
