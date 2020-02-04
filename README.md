# Servicio Social

<img src="/assets/lambda.png" width="100">

## Documentos

* [Plan de trabajo](/documentos/plan-de-trabajo.pdf).
* [Formato](/documentos/formato.pdf)
* [Calendario 2020](documentos/calendario-anual-2020.pdf)

## Entorno

* `pdflatex`: pdfTeX 3.14159265-2.6-1.40.19 (TeX Live 2018)
* `make`: GNU Make 3.81
* `zsh`: zsh 5.7.1
* `iconv`: conv (GNU libiconv 1.11) *(Es usado para cuando se requiera cambiar la codificación 
de los `.tex` de `ISO-8859-1` a `UTF-8`, es opcional su instalación si no se va a usar)*


## Compilación

Para la automatización de las tareas de compilación y limpieza del proyecto, se hizo uso 
de la herramienta `make`. **Es importante que tener los binarios especificados en 
la sección de Entorno**.

Los directorios que contengan un `Makefile` podrán realizar las tareas descritas anteriormente.

#### Compilación de todos los `.tex`

En el directorio, teclear el siguiente comando:

```bash
$ make
```

Compilará todos los `.tex` que coincidan con la expresión regular descrita en el `Makefile` 
en la variable `TEXFILESWILDCARD := regex` donde `regex` es la expresión regular. Seguido de 
compilar los `.tex`, moverá los `.pdf` generados a una carpeta llamada `pdf`.

#### Limpieza del proyecto

Si se requiere eliminar los archivos generados y los `.pdf`, se puede hacer con:

```bash
$ make clean_all
```

#### Compilar solo un archivo `.tex`

Hay casos donde solo se quiere compilar un solo archivo, para eso hay una tarea en el 
`Makefile` que lo hace. Para ello se deberá teclear lo siguiente:

```bash
$ make compile_one file=FILE_NAME.tex
```

Donde `FILE_NAME` es el archivo `.tex` que se quiere compilar.


## Scripts útiles

Si hay archivos con codificación que no sea `UTF-8` se puede cambiar con la ayuda del binario 
`iconv`. Un ejemplo de ello es que si en un directorio tenemos varios `.tex` con diferente 
codificación, se las podemos cambiar con el siguiente comando:

```bash
$ for file in *.tex ; do iconv --from-code=ISO-8859-1 --to-code=UTF-8 "$file" > "$file.aux" && mv -f "$file.aux" "$file" ; done
```

En caso de que no sepamos de antemano la codificación, podemos iterar sobre los archivos 
en el directorio donde estemos situados, y para cada uno de ellos imprimirá detalles del
archivo y si es texto, indicará su codificación.

```bash
$ for x in *.* ; do file $x ; done
```

### TODO's

- [x] Reunirme la última semana con Favio para acordadar que se debe hacer.
(25 al 29 de noviembre).
- [ ] Preguntar acerca de las notas `n09alf192.tex`, `n10alf192.tex` y `n11alf192.tex` con 
  con el archivo `.diff` que cambias se deben tener.
- [x] Presentaciones compilen.
    - [x] `alf192DyckChomskySchutz`
    - [x] `aylfm161`
    - [x] `alfp`
- [ ] Agregar el `Makefile` a `aylfm161` y `alf192DyckChomskySchutz`.
- [ ] Quitar los archivos de `diff` en `alfp`.
- [x] Notas `alf192` compilen.
- [ ] Hacer resumen del contenido de cada nota y presentación y ponerlo en un `.txt`.
- [x] Hacer lo del `.gitignore`.
- [ ] Ir con Favio el 4 de febrero.
- [x] Hacer un `Makefile` genérico y con base a ése, usarlo para cada diferente proyecto.
- [ ] Agregar al `.gitignore` los archivos temporales de emacs.