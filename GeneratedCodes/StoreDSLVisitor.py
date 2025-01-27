# Generated from D:/semester-7/Compiler/FinalProject/Grammar/StoreDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .StoreDSLParser import StoreDSLParser
else:
    from StoreDSLParser import StoreDSLParser

# This class defines a complete generic visitor for a parse tree produced by StoreDSLParser.

class StoreDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by StoreDSLParser#start.
    def visitStart(self, ctx:StoreDSLParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreDSLParser#program.
    def visitProgram(self, ctx:StoreDSLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreDSLParser#statement.
    def visitStatement(self, ctx:StoreDSLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreDSLParser#define.
    def visitDefine(self, ctx:StoreDSLParser.DefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreDSLParser#create.
    def visitCreate(self, ctx:StoreDSLParser.CreateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreDSLParser#delete.
    def visitDelete(self, ctx:StoreDSLParser.DeleteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreDSLParser#update.
    def visitUpdate(self, ctx:StoreDSLParser.UpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreDSLParser#list.
    def visitList(self, ctx:StoreDSLParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreDSLParser#discount.
    def visitDiscount(self, ctx:StoreDSLParser.DiscountContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreDSLParser#attribute.
    def visitAttribute(self, ctx:StoreDSLParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreDSLParser#keyValuePairs.
    def visitKeyValuePairs(self, ctx:StoreDSLParser.KeyValuePairsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreDSLParser#keyValuePair.
    def visitKeyValuePair(self, ctx:StoreDSLParser.KeyValuePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreDSLParser#name.
    def visitName(self, ctx:StoreDSLParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreDSLParser#type.
    def visitType(self, ctx:StoreDSLParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreDSLParser#value.
    def visitValue(self, ctx:StoreDSLParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoreDSLParser#entityName.
    def visitEntityName(self, ctx:StoreDSLParser.EntityNameContext):
        return self.visitChildren(ctx)



del StoreDSLParser