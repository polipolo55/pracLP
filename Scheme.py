import os
from antlr4 import *
import sys

from SchemeLexer import SchemeLexer
from SchemeParser import SchemeParser
from SchemeVisitor import SchemeVisitor
from EvalVisitor import EvalVisitor


def main():

    if len(sys.argv) != 2:
        print("Ús: python3 Scheme.py fitxer")
        sys.exit(1)
    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print(f"el fitxer {input_file} no existeix")
        sys.exit(1)
    if not os.path.isfile(input_file):
        print(f"{input_file} no és un fitxer")
        sys.exit(1)
    if not input_file.endswith('.scm'):
        print(f"{input_file} no és un fitxer Scheme")
        sys.exit(1)

    try:
        input_stream = FileStream(input_file, encoding='utf-8')
        lexer = SchemeLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = SchemeParser(token_stream)
        tree = parser.program()
        evaluator = EvalVisitor()
        evaluator.visitProgram(tree)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
