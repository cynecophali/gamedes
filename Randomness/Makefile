PDF_PARAMS=-s --pdf-engine=xelatex -V documentclass=scrartcl -V papersize=a4 -V lang=de -V fontsize=11pt
FONT_PARAMS=-V mainfont="Noto Serif" -V sansfont="Noto Sans" -V monofont="Noto Sans Mono"
DATE=-V date="`date +'%d.%m.%Y'`"

.PHONY: all clean

all: loesungen-1.pdf

loesungen-1.pdf: loesungen-1.md
	pandoc $(PDF_PARAMS) $(FONT_PARAMS) $(DATE) $^ -o $@

clean:
	rm -rf loesungen-1.pdf
