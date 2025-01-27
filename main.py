from antlr4 import *
import argparse
from CustomCodes.StoreDSLCustomListener import StoreDSLCustomListener
from Visualization.ASTToNetworkxGraph import show_ast
from GeneratedCodes.StoreDSLLexer import StoreDSLLexer
from GeneratedCodes.StoreDSLParser import StoreDSLParser
from Visualization.PostOrderASTTraverser import PostOrderASTTraverser
from CustomCodes.StoreDSLCodeGenerator import StoreDSLCodeGenerator


def main(arguments):
    stream = FileStream(arguments.input, encoding='utf8')
    lexer = StoreDSLLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = StoreDSLParser(token_stream)
    parse_tree = parser.program()
    ast_builder_listener = StoreDSLCustomListener(parser.ruleNames)
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=ast_builder_listener)
    ast = ast_builder_listener.ast
    show_ast(ast.root)
    post_order_ast_traverser = PostOrderASTTraverser()
    post_order_ast_traverser.node_attributes = ['label']
    traversal = post_order_ast_traverser.traverse_ast(ast.root)
    code_generator = StoreDSLCodeGenerator()
    generated_code = code_generator.generate_code(traversal)
    with open(arguments.output, 'w') as output_file:
        output_file.write(generated_code)


if __name__ == '__main__':
    input_index = 2
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-i', '--input', help='Input source', default=rf'./TestInputs/input_{input_index}.txt')
    argparser.add_argument('-o', '--output', help='Output path', default=rf'./TestOutputs/output_{input_index}.py')
    args = argparser.parse_args()
    main(args)