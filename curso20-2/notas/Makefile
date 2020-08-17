SHELL := /bin/zsh

TEX := pdflatex
TEXFLAGS := -interaction=nonstopmode

BUILDDIR := build
PDFDIR := pdf

TEXFILESWILDCARD := n**aylf202

all: compile_all clean

compile_all:
	mkdir -p $(BUILDDIR)
	mkdir -p $(PDFDIR)
	for file in $(TEXFILESWILDCARD).tex ; do \
		$(TEX) $(TEXFLAGS) -output-directory=$(BUILDDIR) $$file ; \
	done
	mv $(BUILDDIR)/*.pdf ./$(PDFDIR)

clean:
	-rm -rf $(BUILDDIR)

clean_all:
	-rm -rf $(BUILDDIR)
	-rm -rf $(PDFDIR)

compile_one:
	mkdir -p $(BUILDDIR)
	mkdir -p $(PDFDIR)
	$(TEX) -output-directory=$(BUILDDIR) $(file)
	@$(eval PDFFILE := $(shell basename $(file) .tex))
	mv $(BUILDDIR)/$(PDFFILE).pdf ./$(PDFDIR)