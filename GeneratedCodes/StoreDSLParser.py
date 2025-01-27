# Generated from D:/semester-7/Compiler/FinalProject/Grammar/StoreDSL.g4 by ANTLR 4.13.2
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
        4,1,23,169,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,0,1,1,5,1,37,8,1,10,1,12,1,40,9,1,
        1,2,1,2,1,2,1,2,1,2,1,2,3,2,48,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,5,3,61,8,3,10,3,12,3,64,9,3,1,3,1,3,1,3,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,80,8,4,10,4,12,4,83,9,4,1,
        4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,111,8,6,10,6,12,6,114,
        9,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,
        1,10,1,10,1,10,5,10,150,8,10,10,10,12,10,153,9,10,1,10,1,10,1,11,
        1,11,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,15,0,0,
        16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,2,1,0,14,16,1,0,
        17,19,162,0,32,1,0,0,0,2,38,1,0,0,0,4,47,1,0,0,0,6,49,1,0,0,0,8,
        68,1,0,0,0,10,87,1,0,0,0,12,99,1,0,0,0,14,118,1,0,0,0,16,125,1,0,
        0,0,18,141,1,0,0,0,20,145,1,0,0,0,22,156,1,0,0,0,24,160,1,0,0,0,
        26,162,1,0,0,0,28,164,1,0,0,0,30,166,1,0,0,0,32,33,3,2,1,0,33,34,
        5,0,0,1,34,1,1,0,0,0,35,37,3,4,2,0,36,35,1,0,0,0,37,40,1,0,0,0,38,
        36,1,0,0,0,38,39,1,0,0,0,39,3,1,0,0,0,40,38,1,0,0,0,41,48,3,6,3,
        0,42,48,3,8,4,0,43,48,3,10,5,0,44,48,3,12,6,0,45,48,3,14,7,0,46,
        48,3,16,8,0,47,41,1,0,0,0,47,42,1,0,0,0,47,43,1,0,0,0,47,44,1,0,
        0,0,47,45,1,0,0,0,47,46,1,0,0,0,48,5,1,0,0,0,49,50,5,1,0,0,50,51,
        5,2,0,0,51,52,5,3,0,0,52,53,5,4,0,0,53,54,3,30,15,0,54,55,5,5,0,
        0,55,56,5,6,0,0,56,57,5,2,0,0,57,62,3,18,9,0,58,59,5,5,0,0,59,61,
        3,18,9,0,60,58,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,
        63,65,1,0,0,0,64,62,1,0,0,0,65,66,5,7,0,0,66,67,5,7,0,0,67,7,1,0,
        0,0,68,69,5,8,0,0,69,70,5,2,0,0,70,71,5,3,0,0,71,72,5,4,0,0,72,73,
        3,30,15,0,73,74,5,5,0,0,74,75,5,6,0,0,75,76,5,2,0,0,76,81,3,22,11,
        0,77,78,5,5,0,0,78,80,3,22,11,0,79,77,1,0,0,0,80,83,1,0,0,0,81,79,
        1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,5,7,0,0,
        85,86,5,7,0,0,86,9,1,0,0,0,87,88,5,9,0,0,88,89,5,2,0,0,89,90,5,3,
        0,0,90,91,5,4,0,0,91,92,3,30,15,0,92,93,5,5,0,0,93,94,5,6,0,0,94,
        95,5,2,0,0,95,96,3,22,11,0,96,97,5,7,0,0,97,98,5,7,0,0,98,11,1,0,
        0,0,99,100,5,10,0,0,100,101,5,2,0,0,101,102,5,3,0,0,102,103,5,4,
        0,0,103,104,3,30,15,0,104,105,5,5,0,0,105,106,5,6,0,0,106,107,5,
        2,0,0,107,112,3,22,11,0,108,109,5,5,0,0,109,111,3,22,11,0,110,108,
        1,0,0,0,111,114,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,115,
        1,0,0,0,114,112,1,0,0,0,115,116,5,7,0,0,116,117,5,7,0,0,117,13,1,
        0,0,0,118,119,5,11,0,0,119,120,5,2,0,0,120,121,5,3,0,0,121,122,5,
        4,0,0,122,123,3,30,15,0,123,124,5,7,0,0,124,15,1,0,0,0,125,126,5,
        12,0,0,126,127,5,2,0,0,127,128,5,3,0,0,128,129,5,4,0,0,129,130,3,
        30,15,0,130,131,5,5,0,0,131,132,5,6,0,0,132,133,5,2,0,0,133,134,
        3,22,11,0,134,135,5,5,0,0,135,136,5,13,0,0,136,137,5,4,0,0,137,138,
        3,28,14,0,138,139,5,7,0,0,139,140,5,7,0,0,140,17,1,0,0,0,141,142,
        3,24,12,0,142,143,5,4,0,0,143,144,3,26,13,0,144,19,1,0,0,0,145,146,
        5,2,0,0,146,151,3,22,11,0,147,148,5,5,0,0,148,150,3,22,11,0,149,
        147,1,0,0,0,150,153,1,0,0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,
        154,1,0,0,0,153,151,1,0,0,0,154,155,5,7,0,0,155,21,1,0,0,0,156,157,
        3,24,12,0,157,158,5,4,0,0,158,159,3,28,14,0,159,23,1,0,0,0,160,161,
        5,20,0,0,161,25,1,0,0,0,162,163,7,0,0,0,163,27,1,0,0,0,164,165,7,
        1,0,0,165,29,1,0,0,0,166,167,5,20,0,0,167,31,1,0,0,0,6,38,47,62,
        81,112,151
    ]

class StoreDSLParser ( Parser ):

    grammarFileName = "StoreDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'define'", "'{'", "'entity'", "':'", 
                     "','", "'attributes'", "'}'", "'create'", "'delete'", 
                     "'update'", "'list'", "'discount'", "'discount_value'", 
                     "'String'", "'Integer'", "'Float'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "STRING", "FLOAT", "INT", "ID", "COMMENT", 
                      "WS", "NEWLINE" ]

    RULE_start = 0
    RULE_program = 1
    RULE_statement = 2
    RULE_define = 3
    RULE_create = 4
    RULE_delete = 5
    RULE_update = 6
    RULE_list = 7
    RULE_discount = 8
    RULE_attribute = 9
    RULE_keyValuePairs = 10
    RULE_keyValuePair = 11
    RULE_name = 12
    RULE_type = 13
    RULE_value = 14
    RULE_entityName = 15

    ruleNames =  [ "start", "program", "statement", "define", "create", 
                   "delete", "update", "list", "discount", "attribute", 
                   "keyValuePairs", "keyValuePair", "name", "type", "value", 
                   "entityName" ]

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
    T__13=14
    T__14=15
    T__15=16
    STRING=17
    FLOAT=18
    INT=19
    ID=20
    COMMENT=21
    WS=22
    NEWLINE=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def program(self):
            return self.getTypedRuleContext(StoreDSLParser.ProgramContext,0)


        def EOF(self):
            return self.getToken(StoreDSLParser.EOF, 0)

        def getRuleIndex(self):
            return StoreDSLParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = StoreDSLParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.program()
            self.state = 33
            self.match(StoreDSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StoreDSLParser.StatementContext)
            else:
                return self.getTypedRuleContext(StoreDSLParser.StatementContext,i)


        def getRuleIndex(self):
            return StoreDSLParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = StoreDSLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7938) != 0):
                self.state = 35
                self.statement()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def define(self):
            return self.getTypedRuleContext(StoreDSLParser.DefineContext,0)


        def create(self):
            return self.getTypedRuleContext(StoreDSLParser.CreateContext,0)


        def delete(self):
            return self.getTypedRuleContext(StoreDSLParser.DeleteContext,0)


        def update(self):
            return self.getTypedRuleContext(StoreDSLParser.UpdateContext,0)


        def list_(self):
            return self.getTypedRuleContext(StoreDSLParser.ListContext,0)


        def discount(self):
            return self.getTypedRuleContext(StoreDSLParser.DiscountContext,0)


        def getRuleIndex(self):
            return StoreDSLParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = StoreDSLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.define()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.create()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.delete()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 44
                self.update()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 45
                self.list_()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 6)
                self.state = 46
                self.discount()
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


    class DefineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entityName(self):
            return self.getTypedRuleContext(StoreDSLParser.EntityNameContext,0)


        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StoreDSLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(StoreDSLParser.AttributeContext,i)


        def getRuleIndex(self):
            return StoreDSLParser.RULE_define

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefine" ):
                listener.enterDefine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefine" ):
                listener.exitDefine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefine" ):
                return visitor.visitDefine(self)
            else:
                return visitor.visitChildren(self)




    def define(self):

        localctx = StoreDSLParser.DefineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_define)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(StoreDSLParser.T__0)
            self.state = 50
            self.match(StoreDSLParser.T__1)
            self.state = 51
            self.match(StoreDSLParser.T__2)
            self.state = 52
            self.match(StoreDSLParser.T__3)
            self.state = 53
            self.entityName()
            self.state = 54
            self.match(StoreDSLParser.T__4)
            self.state = 55
            self.match(StoreDSLParser.T__5)
            self.state = 56
            self.match(StoreDSLParser.T__1)
            self.state = 57
            self.attribute()
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 58
                self.match(StoreDSLParser.T__4)
                self.state = 59
                self.attribute()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
            self.match(StoreDSLParser.T__6)
            self.state = 66
            self.match(StoreDSLParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entityName(self):
            return self.getTypedRuleContext(StoreDSLParser.EntityNameContext,0)


        def keyValuePair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StoreDSLParser.KeyValuePairContext)
            else:
                return self.getTypedRuleContext(StoreDSLParser.KeyValuePairContext,i)


        def getRuleIndex(self):
            return StoreDSLParser.RULE_create

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreate" ):
                listener.enterCreate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreate" ):
                listener.exitCreate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreate" ):
                return visitor.visitCreate(self)
            else:
                return visitor.visitChildren(self)




    def create(self):

        localctx = StoreDSLParser.CreateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_create)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(StoreDSLParser.T__7)
            self.state = 69
            self.match(StoreDSLParser.T__1)
            self.state = 70
            self.match(StoreDSLParser.T__2)
            self.state = 71
            self.match(StoreDSLParser.T__3)
            self.state = 72
            self.entityName()
            self.state = 73
            self.match(StoreDSLParser.T__4)
            self.state = 74
            self.match(StoreDSLParser.T__5)
            self.state = 75
            self.match(StoreDSLParser.T__1)
            self.state = 76
            self.keyValuePair()
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 77
                self.match(StoreDSLParser.T__4)
                self.state = 78
                self.keyValuePair()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(StoreDSLParser.T__6)
            self.state = 85
            self.match(StoreDSLParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeleteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entityName(self):
            return self.getTypedRuleContext(StoreDSLParser.EntityNameContext,0)


        def keyValuePair(self):
            return self.getTypedRuleContext(StoreDSLParser.KeyValuePairContext,0)


        def getRuleIndex(self):
            return StoreDSLParser.RULE_delete

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelete" ):
                listener.enterDelete(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelete" ):
                listener.exitDelete(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelete" ):
                return visitor.visitDelete(self)
            else:
                return visitor.visitChildren(self)




    def delete(self):

        localctx = StoreDSLParser.DeleteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_delete)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(StoreDSLParser.T__8)
            self.state = 88
            self.match(StoreDSLParser.T__1)
            self.state = 89
            self.match(StoreDSLParser.T__2)
            self.state = 90
            self.match(StoreDSLParser.T__3)
            self.state = 91
            self.entityName()
            self.state = 92
            self.match(StoreDSLParser.T__4)
            self.state = 93
            self.match(StoreDSLParser.T__5)
            self.state = 94
            self.match(StoreDSLParser.T__1)
            self.state = 95
            self.keyValuePair()
            self.state = 96
            self.match(StoreDSLParser.T__6)
            self.state = 97
            self.match(StoreDSLParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entityName(self):
            return self.getTypedRuleContext(StoreDSLParser.EntityNameContext,0)


        def keyValuePair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StoreDSLParser.KeyValuePairContext)
            else:
                return self.getTypedRuleContext(StoreDSLParser.KeyValuePairContext,i)


        def getRuleIndex(self):
            return StoreDSLParser.RULE_update

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdate" ):
                listener.enterUpdate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdate" ):
                listener.exitUpdate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate" ):
                return visitor.visitUpdate(self)
            else:
                return visitor.visitChildren(self)




    def update(self):

        localctx = StoreDSLParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_update)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(StoreDSLParser.T__9)
            self.state = 100
            self.match(StoreDSLParser.T__1)
            self.state = 101
            self.match(StoreDSLParser.T__2)
            self.state = 102
            self.match(StoreDSLParser.T__3)
            self.state = 103
            self.entityName()
            self.state = 104
            self.match(StoreDSLParser.T__4)
            self.state = 105
            self.match(StoreDSLParser.T__5)
            self.state = 106
            self.match(StoreDSLParser.T__1)
            self.state = 107
            self.keyValuePair()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 108
                self.match(StoreDSLParser.T__4)
                self.state = 109
                self.keyValuePair()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 115
            self.match(StoreDSLParser.T__6)
            self.state = 116
            self.match(StoreDSLParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entityName(self):
            return self.getTypedRuleContext(StoreDSLParser.EntityNameContext,0)


        def getRuleIndex(self):
            return StoreDSLParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = StoreDSLParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(StoreDSLParser.T__10)
            self.state = 119
            self.match(StoreDSLParser.T__1)
            self.state = 120
            self.match(StoreDSLParser.T__2)
            self.state = 121
            self.match(StoreDSLParser.T__3)
            self.state = 122
            self.entityName()
            self.state = 123
            self.match(StoreDSLParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DiscountContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entityName(self):
            return self.getTypedRuleContext(StoreDSLParser.EntityNameContext,0)


        def keyValuePair(self):
            return self.getTypedRuleContext(StoreDSLParser.KeyValuePairContext,0)


        def value(self):
            return self.getTypedRuleContext(StoreDSLParser.ValueContext,0)


        def getRuleIndex(self):
            return StoreDSLParser.RULE_discount

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiscount" ):
                listener.enterDiscount(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiscount" ):
                listener.exitDiscount(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiscount" ):
                return visitor.visitDiscount(self)
            else:
                return visitor.visitChildren(self)




    def discount(self):

        localctx = StoreDSLParser.DiscountContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_discount)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(StoreDSLParser.T__11)
            self.state = 126
            self.match(StoreDSLParser.T__1)
            self.state = 127
            self.match(StoreDSLParser.T__2)
            self.state = 128
            self.match(StoreDSLParser.T__3)
            self.state = 129
            self.entityName()
            self.state = 130
            self.match(StoreDSLParser.T__4)
            self.state = 131
            self.match(StoreDSLParser.T__5)
            self.state = 132
            self.match(StoreDSLParser.T__1)
            self.state = 133
            self.keyValuePair()
            self.state = 134
            self.match(StoreDSLParser.T__4)
            self.state = 135
            self.match(StoreDSLParser.T__12)
            self.state = 136
            self.match(StoreDSLParser.T__3)
            self.state = 137
            self.value()
            self.state = 138
            self.match(StoreDSLParser.T__6)
            self.state = 139
            self.match(StoreDSLParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(StoreDSLParser.NameContext,0)


        def type_(self):
            return self.getTypedRuleContext(StoreDSLParser.TypeContext,0)


        def getRuleIndex(self):
            return StoreDSLParser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = StoreDSLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.name()
            self.state = 142
            self.match(StoreDSLParser.T__3)
            self.state = 143
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyValuePairsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyValuePair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StoreDSLParser.KeyValuePairContext)
            else:
                return self.getTypedRuleContext(StoreDSLParser.KeyValuePairContext,i)


        def getRuleIndex(self):
            return StoreDSLParser.RULE_keyValuePairs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyValuePairs" ):
                listener.enterKeyValuePairs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyValuePairs" ):
                listener.exitKeyValuePairs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyValuePairs" ):
                return visitor.visitKeyValuePairs(self)
            else:
                return visitor.visitChildren(self)




    def keyValuePairs(self):

        localctx = StoreDSLParser.KeyValuePairsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_keyValuePairs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(StoreDSLParser.T__1)
            self.state = 146
            self.keyValuePair()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 147
                self.match(StoreDSLParser.T__4)
                self.state = 148
                self.keyValuePair()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 154
            self.match(StoreDSLParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyValuePairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(StoreDSLParser.NameContext,0)


        def value(self):
            return self.getTypedRuleContext(StoreDSLParser.ValueContext,0)


        def getRuleIndex(self):
            return StoreDSLParser.RULE_keyValuePair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyValuePair" ):
                listener.enterKeyValuePair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyValuePair" ):
                listener.exitKeyValuePair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyValuePair" ):
                return visitor.visitKeyValuePair(self)
            else:
                return visitor.visitChildren(self)




    def keyValuePair(self):

        localctx = StoreDSLParser.KeyValuePairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_keyValuePair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.name()
            self.state = 157
            self.match(StoreDSLParser.T__3)
            self.state = 158
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(StoreDSLParser.ID, 0)

        def getRuleIndex(self):
            return StoreDSLParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = StoreDSLParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(StoreDSLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return StoreDSLParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = StoreDSLParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0)):
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


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(StoreDSLParser.STRING, 0)

        def INT(self):
            return self.getToken(StoreDSLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(StoreDSLParser.FLOAT, 0)

        def getRuleIndex(self):
            return StoreDSLParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = StoreDSLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 917504) != 0)):
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


    class EntityNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(StoreDSLParser.ID, 0)

        def getRuleIndex(self):
            return StoreDSLParser.RULE_entityName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntityName" ):
                listener.enterEntityName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntityName" ):
                listener.exitEntityName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntityName" ):
                return visitor.visitEntityName(self)
            else:
                return visitor.visitChildren(self)




    def entityName(self):

        localctx = StoreDSLParser.EntityNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_entityName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(StoreDSLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





