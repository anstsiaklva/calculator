from dataclasses import dataclass

@dataclass
class NumberNode:
    value: any

    def __repr__(self):
        return f"{self.value}"

@dataclass
class AddNode:
    left: any
    right: any

    def __repr__(self):
        return f"({self.left}+{self.right})"

@dataclass
class SubtractNode:
    left: any
    right: any

    def __repr__(self):
        return f"({self.left}-{self.right})"

@dataclass
class MultiplyNode:
    left: any
    right: any

    def __repr__(self):
        return f"({self.left}*{self.right})"

@dataclass
class DivisionNode:
    left: any
    right: any

    def __repr__(self):
        return f"({self.left}/{self.right})"

@dataclass
class PowerNode:
    left: any
    right: any

    def __repr__(self):
        return f"({self.left}^{self.right})"

@dataclass
class UnarPlusNode:
    node: any

    def __repr__(self):
        return f"(+{self.node})"

@dataclass
class UnarMinusNode:
    node: any

    def __repr__(self):
        return f"(-{self.node})"
