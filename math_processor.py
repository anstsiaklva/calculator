from token_generator import TokenGenerator
from expression_parser import ExpressionParser
from interpreter import Interpreter

class Processor:
    def process(self, expression):
        self.token_generator = TokenGenerator(expression)
        self.tokens = self.token_generator.generate_tokens()

        self.tokens = iter(self.tokens)

        self.expression_parser = ExpressionParser(self.tokens)
        self.tree = self.expression_parser.parse()

        self.interpreter = Interpreter()
        self.result = self.interpreter.visit_node(self.tree)

        return self.result