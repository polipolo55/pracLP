# Generated from Scheme.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SchemeParser import SchemeParser
else:
    from SchemeParser import SchemeParser

# This class defines a complete generic visitor for a parse tree produced by SchemeParser.

class SchemeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SchemeParser#program.
    def visitProgram(self, ctx:SchemeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#ArOperation.
    def visitArOperation(self, ctx:SchemeParser.ArOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#BoOperatio.
    def visitBoOperatio(self, ctx:SchemeParser.BoOperatioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#Num.
    def visitNum(self, ctx:SchemeParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#Str.
    def visitStr(self, ctx:SchemeParser.StrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#True.
    def visitTrue(self, ctx:SchemeParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#False.
    def visitFalse(self, ctx:SchemeParser.FalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#Id.
    def visitId(self, ctx:SchemeParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#calls.
    def visitCalls(self, ctx:SchemeParser.CallsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#arithmeticOperation.
    def visitArithmeticOperation(self, ctx:SchemeParser.ArithmeticOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemeParser#booleanOperation.
    def visitBooleanOperation(self, ctx:SchemeParser.BooleanOperationContext):
        return self.visitChildren(ctx)



del SchemeParser