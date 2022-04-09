from operation_nodes import *
from values import Number

class Interpreter:
    def __init__(self):
        pass

    def visit_node(self, node):
        method_name = f"visit_{type(node).__name__}"
        method = getattr(self, method_name)
        return method(node)

    def visit_NumberNode(self, node):
        return Number(node.value)

    def visit_AddNode(self, node):
        return Number(self.visit_node(node.left).value + self.visit_node(node.right).value)

    def visit_SubtractNode(self, node):
        return Number(self.visit_node(node.left).value - self.visit_node(node.right).value)

    def visit_MultiplyNode(self, node):
        return Number(self.visit_node(node.left).value * self.visit_node(node.right).value)
            
    def visit_DivisionNode(self, node):
        try:
            return Number(self.visit_node(node.left).value / self.visit_node(node.right).value)
        except:
            raise Exception("Runtime math error")

    def visit_PowerNode(self, node):
        return Number(self.visit_node(node.left).value ** self.visit_node(node.right).value)
        
    def visit_UnarMinusNode(self, node):
        return Number(-self.visit_node(node.node).value)

    def visit_UnarPlusNode(self, node):
        return Number(self.visit_node(node.node).value)