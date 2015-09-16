#!/usr/bin/make

# Makefile to build the ibus-table database for Cherokee input, by
# Thomas Klute <thomas2.klute@uni-dortmund.de>.
#
# Licensed as CC0 (see
# https://creativecommons.org/publicdomain/zero/1.0/), use as you
# wish!
#
# Please see "help" target for usage.

# Installation prefix (commonly "/usr" or "/usr/local")
PREFIX ?= /usr/local
# Installation directory for ibus-table databases relative to PREFIX
TABLES_DIR ?= $(PREFIX)/share/ibus-table/tables

CSV = ../../data/full.csv
DB = chr.db
CLEANFILES = chr.txt $(DB)

all: $(DB)

chr.txt: $(CSV)
	./csv-to-ibus.py < $< > $@

%.db: %.txt
	ibus-table-createdb -s $< -n $@

clean:
	rm $(CLEANFILES) || true

install: all
	if ! [ -d $(TABLES_DIR) ]; then \
		mkdir -p $(TABLES_DIR); \
	fi
	install --mode=0644 $(DB) $(TABLES_DIR)/

uninstall:
	if [ -e $(TABLES_DIR)/$(DB) ]; then \
		rm $(TABLES_DIR)/$(DB); \
	fi

help:
	@echo "Makefile to build the ibus-table database for Cherokee syllabary"
	@echo ""
	@echo "Environment variables:"
	@echo "  PREFIX\tInstallation prefix, default: $(PREFIX)"
	@echo "  TABLES_DIR\tInstallation directory for tables, default: \$${PREFIX}/share/ibus-table/tables/"

.PHONY: all clean install uninstall help
