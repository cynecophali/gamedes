.PHONY: all

all: mda_summary.pdf mda_themehospital_dungeon-keeper-2.pdf

mda_summary.pdf: mda_summary.md
	pandoc -N -t ms $^ -o $@

mda_themehospital_dungeon-keeper-2.pdf: mda_themehospital_dungeon-keeper-2.md
	pandoc -N -t ms $^ -o $@
