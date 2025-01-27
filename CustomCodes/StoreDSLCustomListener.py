from Visualization.AST import AST
from Visualization.make_ast_subtree import make_ast_subtree
from GeneratedCodes.StoreDSLListener import StoreDSLListener


class StoreDSLCustomListener(StoreDSLListener):
    def __init__(self, rule_names):
        self.rule_names = rule_names
        self.ast = AST()

    def exitEveryRule(self, ctx):
        rule_name = self.rule_names[ctx.getRuleIndex()]
        make_ast_subtree(self.ast, ctx, rule_name)