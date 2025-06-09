import ast
import operator

class Calculator:
    """Simple calculator that safely evaluates arithmetic expressions."""

    ALLOWED_OPERATORS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.USub: operator.neg
    }

    def evaluate(self, expression: str):
        """Evaluate a basic arithmetic expression."""
        try:
            node = ast.parse(expression, mode='eval').body
            return self._eval(node)
        except Exception as e:
            raise ValueError(f"Invalid expression: {e}")

    def _eval(self, node):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        elif isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type in self.ALLOWED_OPERATORS:
                left = self._eval(node.left)
                right = self._eval(node.right)
                return self.ALLOWED_OPERATORS[op_type](left, right)
        elif isinstance(node, ast.UnaryOp) and type(node.op) in self.ALLOWED_OPERATORS:
            operand = self._eval(node.operand)
            return self.ALLOWED_OPERATORS[type(node.op)](operand)
        raise ValueError('Unsupported expression')


def main():
    calc = Calculator()
    print("Simple Calculator. Enter 'q' to quit.")
    while True:
        expr = input('Expression: ')
        if expr.lower() == 'q':
            break
        try:
            result = calc.evaluate(expr)
            print('Result:', result)
        except Exception as e:
            print('Error:', e)


if __name__ == '__main__':
    main()
