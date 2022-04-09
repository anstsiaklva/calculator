from enum import Enum
from dataclasses import dataclass
class TokenList(Enum):
    NUM   = 0
    PLUS  = 1
    MIN   = 2
    MUL   = 3
    DIV   = 4
    LP    = 5
    RP    = 7
    POW   = 8

#only float numbers should have value
@dataclass
class Token:
    type: TokenList
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}")