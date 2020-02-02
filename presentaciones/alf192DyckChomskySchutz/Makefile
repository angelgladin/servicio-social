SHELL := /bin/zsh

TEX := pdflatex
TEXFLAGS := -interaction=nonstopmode

BUILDDIR := build
PDFDIR := pdf

all: compile_all clean

compile_all:
	mkdir -p $(BUILDDIR)
	mkdir -p $(PDFDIR)
	for file in alf192*.tex ; do \
		$(TEX) $(TEXFLAGS) -output-directory=$(BUILDDIR) $$file ; \
	done
	mv $(BUILDDIR)/*.pdf ../$(pdf)

clean:
	-rm -rf $(BUILDDIR)

cleanall:
	-rm -rf $(BUILDDIR)
	-rm -rf $(PDFDIR)

compile_one:
	mkdir -p $(BUILDDIR)
	mkdir -p $(PDFDIR)
	$(TEX) -output-directory=$(BUILDDIR) $(file)
	mv $(BUILDDIR)/*.pdf ../$(pdf)

