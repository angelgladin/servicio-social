# Ambiente
* `pdflatex`: pdfTeX 3.14159265-2.6-1.40.19 (TeX Live 2018)

# Compilación

Para compilar un solo archivo:

```bash
$ pdflatex [filename].tex
```

Compilación todas las notas `n**alf192.tex` (`**` significa cualquier cosa, e.g., `n01alf192.tex`):

```bash
$ for x in n**alf192.tex; do pdflatex $x;done
```

# Remover archivos generados

Remover los `.aux`, `.log` y `.out`:

```bash
$ rm -f *.{aux,log,out}
```

Remover los `.pdf`:

```bash
$ rm -f *.pdf
```



# Referencias
Obtener versión de `pdflatex` [aquí](https://tex.stackexchange.com/questions/366586/how-to-find-out-and-interpret-the-latex-version-number).

[Compilación](https://guides.lib.wayne.edu/latex/compiling)
