.DEFAULT_GOAL := all

replace = echo $(1) | sed 's/?/ /g'

all: $(subst tex,pdf,$(shell ls *.tex | sed 's/ /?/g'))

%.pdf: %.tex
	xelatex -output-directory=pdf -halt-on-error -interaction=nonstopmode "`$(call replace,$<)`"
	rm pdf/*.log pdf/*.aux

clean:
	rm -f pdf/*

.PHONY : clean all
