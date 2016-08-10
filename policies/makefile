.DEFAULT_GOAL := all

replace = echo $(1) | sed 's/?/ /g'

all: $(subst tex,pdf,$(shell ls *.tex | sed 's/ /?/g' | sed 's/.*/pdf\/&/g'))

pdf/%.pdf: %.tex
	mkdir -p pdf
	xelatex -output-directory=pdf -halt-on-error -interaction=nonstopmode "`$(call replace,$<)`"
	xelatex -output-directory=pdf -halt-on-error -interaction=nonstopmode "`$(call replace,$<)`"
	rm pdf/*.log pdf/*.aux

clean:
	rm -f pdf/*

.PHONY : clean all
