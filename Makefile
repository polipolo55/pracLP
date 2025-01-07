# Opcions del compilador
ANTLR = antlr4
ANTLR_FLAGS = -Dlanguage=Python3 -no-listener -visitor
GRAMMAR_FILE = Scheme.g4

# Fitxers de sortida
LEXER = SchemeLexer.py
PARSER = SchemeParser.py
VISITOR = SchemeVisitor.py

# Fitxer Scheme per defecte a executar
DEFAULT_SCHEME_FILE = test_principal.scm

all: 
	$(ANTLR) $(ANTLR_FLAGS) $(GRAMMAR_FILE)

# Netejar fitxers generats
clean:
	rm -f $(LEXER) $(PARSER) $(VISITOR)
	rm -f *.tokens *.interp

# Ús: make run SCHEME_FILE=el_teu_fitxer.scm
run: all
ifndef SCHEME_FILE
	$(MAKE) run SCHEME_FILE=$(DEFAULT_SCHEME_FILE)
else
	python3 Scheme.py $(SCHEME_FILE)
endif

test: all
	for file in test_*.scm; do \
		echo "Executant $$file..."; \
		python3 Scheme.py $$file; \
	done

help:
	@echo "Ús del Makefile:"
	@echo "  make all                 - Genera les classes del lexer, parser i visitor"
	@echo "  make clean               - Elimina els fitxers generats del lexer, parser i visitor"
	@echo "  make run SCHEME_FILE=... - Executa Scheme.py amb el fitxer Scheme especificat"
	@echo "     Si SCHEME_FILE no està especificat, s'utilitza $(DEFAULT_SCHEME_FILE) per defecte."
	@echo "  make test                - Executa tots els fitxers de prova que comencen amb test_"