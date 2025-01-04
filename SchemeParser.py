# Generated from Scheme.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,20,40,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,24,8,1,1,1,1,1,
        5,1,28,8,1,10,1,12,1,31,9,1,1,1,3,1,34,8,1,1,2,1,2,1,3,1,3,1,3,0,
        0,4,0,2,4,6,0,2,1,0,4,7,1,0,8,13,45,0,9,1,0,0,0,2,33,1,0,0,0,4,35,
        1,0,0,0,6,37,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,11,1,0,0,0,11,9,
        1,0,0,0,11,12,1,0,0,0,12,13,1,0,0,0,13,14,5,0,0,1,14,1,1,0,0,0,15,
        34,3,4,2,0,16,34,3,6,3,0,17,34,5,18,0,0,18,34,5,16,0,0,19,34,5,14,
        0,0,20,34,5,15,0,0,21,34,5,17,0,0,22,24,5,1,0,0,23,22,1,0,0,0,23,
        24,1,0,0,0,24,25,1,0,0,0,25,29,5,2,0,0,26,28,3,2,1,0,27,26,1,0,0,
        0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,32,1,0,0,0,31,29,
        1,0,0,0,32,34,5,3,0,0,33,15,1,0,0,0,33,16,1,0,0,0,33,17,1,0,0,0,
        33,18,1,0,0,0,33,19,1,0,0,0,33,20,1,0,0,0,33,21,1,0,0,0,33,23,1,
        0,0,0,34,3,1,0,0,0,35,36,7,0,0,0,36,5,1,0,0,0,37,38,7,1,0,0,38,7,
        1,0,0,0,4,11,23,29,33
    ]

class SchemeParser ( Parser ):

    grammarFileName = "Scheme.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'''", "'('", "')'", "'*'", "'/'", "'+'", 
                     "'-'", "'>='", "'<='", "'='", "'<>'", "'>'", "'<'", 
                     "'#t'", "'#f'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "TRUE", "FALSE", "STRING", 
                      "IDENTIFIER", "NUMBER", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_arithmeticOperation = 2
    RULE_booleanOperation = 3

    ruleNames =  [ "program", "expression", "arithmeticOperation", "booleanOperation" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    TRUE=14
    FALSE=15
    STRING=16
    IDENTIFIER=17
    NUMBER=18
    WS=19
    COMMENT=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SchemeParser.EOF, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SchemeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SchemeParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SchemeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SchemeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.expression()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 524278) != 0)):
                    break

            self.state = 13
            self.match(SchemeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SchemeParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StrContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SchemeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(SchemeParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStr" ):
                return visitor.visitStr(self)
            else:
                return visitor.visitChildren(self)


    class ArOperationContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SchemeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arithmeticOperation(self):
            return self.getTypedRuleContext(SchemeParser.ArithmeticOperationContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArOperation" ):
                return visitor.visitArOperation(self)
            else:
                return visitor.visitChildren(self)


    class CallsContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SchemeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SchemeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SchemeParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalls" ):
                return visitor.visitCalls(self)
            else:
                return visitor.visitChildren(self)


    class NumContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SchemeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(SchemeParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)


    class TrueContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SchemeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(SchemeParser.TRUE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrue" ):
                return visitor.visitTrue(self)
            else:
                return visitor.visitChildren(self)


    class BoOperatioContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SchemeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def booleanOperation(self):
            return self.getTypedRuleContext(SchemeParser.BooleanOperationContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoOperatio" ):
                return visitor.visitBoOperatio(self)
            else:
                return visitor.visitChildren(self)


    class FalseContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SchemeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(SchemeParser.FALSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalse" ):
                return visitor.visitFalse(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SchemeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(SchemeParser.IDENTIFIER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)



    def expression(self):

        localctx = SchemeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 7]:
                localctx = SchemeParser.ArOperationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.arithmeticOperation()
                pass
            elif token in [8, 9, 10, 11, 12, 13]:
                localctx = SchemeParser.BoOperatioContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.booleanOperation()
                pass
            elif token in [18]:
                localctx = SchemeParser.NumContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 17
                self.match(SchemeParser.NUMBER)
                pass
            elif token in [16]:
                localctx = SchemeParser.StrContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 18
                self.match(SchemeParser.STRING)
                pass
            elif token in [14]:
                localctx = SchemeParser.TrueContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 19
                self.match(SchemeParser.TRUE)
                pass
            elif token in [15]:
                localctx = SchemeParser.FalseContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 20
                self.match(SchemeParser.FALSE)
                pass
            elif token in [17]:
                localctx = SchemeParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 21
                self.match(SchemeParser.IDENTIFIER)
                pass
            elif token in [1, 2]:
                localctx = SchemeParser.CallsContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 22
                    self.match(SchemeParser.T__0)


                self.state = 25
                self.match(SchemeParser.T__1)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 524278) != 0):
                    self.state = 26
                    self.expression()
                    self.state = 31
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 32
                self.match(SchemeParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SchemeParser.RULE_arithmeticOperation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticOperation" ):
                return visitor.visitArithmeticOperation(self)
            else:
                return visitor.visitChildren(self)




    def arithmeticOperation(self):

        localctx = SchemeParser.ArithmeticOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_arithmeticOperation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 240) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SchemeParser.RULE_booleanOperation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanOperation" ):
                return visitor.visitBooleanOperation(self)
            else:
                return visitor.visitChildren(self)




    def booleanOperation(self):

        localctx = SchemeParser.BooleanOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_booleanOperation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





