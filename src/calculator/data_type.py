"""The data types for the calculator."""

# Standard library

# 3rd Party library

# Project library
from calculator.factorial import factorial


# -----------------------------------------------------------------------------
class Number:
    """The number representation."""

    def __init__(self, value):
        """Construct a Number expression."""
        self.value = value

    def eval(self):
        """Calculate the value of the number expression."""
        return self.value


# -----------------------------------------------------------------------------
class FactExpr:
    """The representation of Factorial expression"""

    def __init__(self, operand):
        """Construct a Factorial expression."""
        self.operand = operand

    def eval(self):
        """Calculate the value of the Factorial expression."""
        return factorial(self.operand.eval())


# -----------------------------------------------------------------------------
class PowerExpr:
    """The representation of Power expression"""

    def __init__(self, left, right):
        """Construct a Power expression."""
        self.left = left
        self.right = right

    def eval(self):
        """Calculate the value of the Factorial expression."""
        return self.left.eval() ** self.right.eval()


# -----------------------------------------------------------------------------
class UnaryExpr:
    """The representation of Unary expression"""

    def __init__(self, operator, operand):
        """Construct a Unary expression."""
        self.operator = operator
        self.operand = operand

    def eval(self):
        """Calculate the value of the Unary expression."""
        if self.operator == "-":
            return - self.operand.eval()
        else:
            return self.operand.eval()

# -----------------------------------------------------------------------------
class MulExpr:
    """The representation of Multiplication expression"""

    def __init__(self, operator,left, right):
        """Construct a Unary expression."""
        self.operator = operator
        self.left = left
        self.right = right

    def eval(self):
        """Calculate the value of the Multiplication expression."""
        if self.operator == "*":
            return self.left.eval() * self.right.eval()
        elif self.operator == "/":
            return self.left.eval() / self.right.eval()
        elif self.operator == "%":
            return self.left.eval() % self.right.eval()
        else:
            raise ValueError("Unrecognized operator")
        
        
# -----------------------------------------------------------------------------
class AddExpr:
    """The representation of Addition expression"""

    def __init__(self, operator,left, right):
        """Construct a Addition expression."""
        self.operator = operator
        self.left = left
        self.right = right

    def eval(self):
        """Calculate the value of the Addition expression."""
        if self.operator == "+":
            return self.left.eval() + self.right.eval()
        elif self.operator == "-":
            return self.left.eval() - self.right.eval()
        else:
            raise ValueError("Unrecognized operator")
        
