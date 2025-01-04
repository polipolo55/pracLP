# Compiler options
ANTLR = antlr4
ANTLR_FLAGS = -Dlanguage=Python3 -no-listener -visitor
GRAMMAR_FILE = Scheme.g4

# Output files
LEXER = SchemeLexer.py
PARSER = SchemeParser.py
VISITOR = SchemeVisitor.py

# Target to generate the parser, lexer, and visitor classes
all: 
	$(ANTLR) $(ANTLR_FLAGS) $(GRAMMAR_FILE)

# Clean generated files
clean:

# Target to run your Python script (e.g., your evaluation logic)
run: all
	python3 Scheme.py

# antlr4 -visitor -no-visitor -Dlanguage=Python3 Scheme.g4