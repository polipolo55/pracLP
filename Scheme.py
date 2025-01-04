from antlr4 import *

from SchemeLexer import SchemeLexer
from SchemeParser import SchemeParser
from SchemeVisitor import   SchemeVisitor
from EvalVisitor import     EvalVisitor


input_stream = FileStream('test.scm')
lexer = SchemeLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = SchemeParser(token_stream)
tree = parser.program()


evaluator = EvalVisitor()
results = evaluator.visitProgram(tree)
for result in results:
    print(result)