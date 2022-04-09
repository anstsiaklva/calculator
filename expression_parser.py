from token_types import TokenList
from operation_nodes import *

class ExpressionParser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.move()


    def invalid_syntax_error(self):
        raise Exception("Invalid Syntax")

    def move(self):
        try:
            self.current_position = next(self.tokens)
        except StopIteration:
            self.current_position = None
    
    def parse(self):
        if self.current_position == None:
            return None

        #scanning
        result = self.fullexp()

        #if something remains
        if self.current_position != None:
            self.invalid_syntax_error()
        
        return result

    def fullexp(self):
        result = self.term()

        while (self.current_position != None) and (self.current_position.type in (TokenList.PLUS, TokenList.MIN) ):
            if (self.current_position.type == TokenList.PLUS):
                self.move()
                result = AddNode(result, self.term())
            elif (self.current_position.type == TokenList.MIN):
                self.move()
                result = SubtractNode(result, self.term())

        return result

    def term(self):
        result = self.factor()

        while (self.current_position != None) and (self.current_position.type in (TokenList.MUL, TokenList.DIV, TokenList.POW) ):
            if (self.current_position.type == TokenList.MUL):
                self.move()
                result = MultiplyNode(result, self.factor())
            elif (self.current_position.type == TokenList.DIV):
                self.move()
                result = DivisionNode(result, self.factor())
            elif (self.current_position.type == TokenList.POW):
                self.move()
                result = PowerNode(result, self.factor())

        return result

    def factor(self):
        token = self.current_position

        if (token.type == TokenList.LP):
            self.move()
            result = self.fullexp()

            if (self.current_position.type != TokenList.RP):
                self.invalid_syntax_error()
            
            self.move()
            return result
        
        elif (token.type == TokenList.NUM):
            self.move()
            return NumberNode(token.value)
        
        elif (token.type == TokenList.PLUS):
            self.move()
            return UnarPlusNode(self.factor())

        elif (token.type == TokenList.MIN):
            self.move()
            return UnarMinusNode(self.factor())

        self.invalid_syntax_error()