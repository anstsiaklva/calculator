from token_types import TokenList, Token

skipable = ' \n\t'
numbers = '0123456789'

class TokenGenerator:
    def __init__(self, expression):
        self.expression = iter(expression)
        self.move()

    def move(self):
        try:
            self.current_position = next(self.expression)
        except StopIteration:
            self.current_position = None

    def generate_float_number(self):
        #decimal_point_count = int(self.current_position == '.')
        decimal_point_count = 0
        number = self.current_position
        self.move()

        while (self.current_position != None) and (self.current_position == '.' or self.current_position in numbers):
            if self.current_position == '.':
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break

            number += self.current_position
            self.move()

        if number.startswith('.'):
            number = '0' + number
        elif number.endswith('.'):
            number = number + '0'

        return Token(TokenList.NUM, value=float(number))
        

    def generate_tokens(self):
        while self.current_position != None:

            if (self.current_position in skipable):
                self.move()

            elif (self.current_position in numbers) or (self.current_position == '.'):
                yield self.generate_float_number()

            elif (self.current_position == '+'):
                self.move()
                yield Token(TokenList.PLUS)
            elif (self.current_position == '-'):
                self.move()
                yield Token(TokenList.MIN)

            elif (self.current_position == '/'):
                self.move()
                yield Token(TokenList.DIV)
            elif (self.current_position == '*'):
                self.move()
                yield Token(TokenList.MUL)

            elif (self.current_position == '('):
                self.move()
                yield Token(TokenList.LP)
            elif (self.current_position == ')'):
                self.move()
                yield Token(TokenList.RP)
            elif (self.current_position == '^'):
                self.move()
                yield Token(TokenList.POW)
            else:
                raise Exception('Illegal syntax')