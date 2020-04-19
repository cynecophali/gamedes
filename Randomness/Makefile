PDF_PARAMS=-s --pdf-engine=xelatex -V documentclass=scrartcl -V papersize=a4 -V lang=de -V fontsize=11pt
FONT_PARAMS=-V mainfont="Symbola" -V sansfont="DejaVu Sans" -V monofont="DejaVu Sans Mono"
DATE=-V date="`date +'%d.%m.%Y'`"

.PHONY: all clean

all: loesungen-1.pdf loesungen-2.pdf

loesungen-1.pdf: loesungen-1.md
	pandoc $(PDF_PARAMS) $(FONT_PARAMS) $(DATE) $^ -o $@

loesungen-2.pdf: loesungen-2.md
	pandoc -t ms $^ -o $@

clean:
	rm -rf loesungen-1.pdf loesungen-2.pdf
