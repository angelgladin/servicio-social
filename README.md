# Servicio Social

<img src="/assets/lambda.png" width="100">

## Documentos

* [Plan de trabajo](/documentos/plan-de-trabajo.pdf).
* [Formato](/documentos/formato.pdf)
* [Calendario 2020](documentos/calendario-anual-2020.pdf)

## TODO's

- [x] Reunirme la última semana con Favio para acordadar que se debe hacer.
(25 al 29 de noviembre).
- [x] Checar que las notas (nota 192) compilen.
- [ ] Preguntar acerca de las notas `n09alf192.tex`, `n10alf192.tex` y `n10alf192.tex` con 
  con el archivo `.diff` que cambias se deben tener.
- [ ] Presentaciones compilen.
- [ ] Hacer resumen del contenido de cada nota y presentación y ponerlo en un `.txt`.
- [x] Hacer lo del `.gitignore`.
- [ ] Ir con Favio la semana del 6 de enero (6 a 10 de enero).
- [ ] En las presentaciones `aylfm161`, checar los diff: `aylfm161p01.tex~`, `aylfm161p06.tex\~`, 
`aylfm161p07.tex\~`, `aylfm161p11.tex\~` y `aylfm161p12.tex\~`
- [ ] Checar error en el `.tex` de `/presentaciones/aylfm161/aylfm161p12.tex`.
- [ ] Hacer un `Makefile` genérico y con base a ése, usarlo para cada diferente proyecto.

## Entorno

* `pdflatex`: pdfTeX 3.14159265-2.6-1.40.19 (TeX Live 2018)
* `zsh`: zsh 5.7.1

## Scripts

Para cambiar la codificación de los archivos `.tex` de _ISO-8859-1_ a _UTF-8_ en un directorio 
se puede hacer con el siguiente comando:

```bash
$ for file in *.tex; do iconv --from-code=ISO-8859-1 --to-code=UTF-8 "$file" > "$file.aux" && mv -f "$file.aux" "$file"; done
```

#### TODO

```bash
$ pdflatex -output-directory=build aylfm161p12.tex
$ mkdir -p build
```

https://tex.stackexchange.com/questions/369771/how-to-delete-files-generated-by-latex

### Compilación

Para compilar un solo archivo:

```bash
$ pdflatex [filename].tex
```

Compilación de varios `.tex` estando en un directorio:

```bash
$ for x in *.tex; do pdflatex "$x"; done
```

### Remover archivos generados

Remover los `.aux`, `.log`, `.out`, `.nav`, `.smn` y `.toc`:

```bash
$ rm -f *.{aux,log,out,nav,smn,toc}
```

Remover los `.pdf`:

```bash
$ rm -f *.pdf
```

## Referencias
Obtener versión de `pdflatex` [aquí](https://tex.stackexchange.com/questions/366586/how-to-find-out-and-interpret-the-latex-version-number).

[Compilación](https://guides.lib.wayne.edu/latex/compiling)