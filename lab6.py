import ast


def cyclomatic_complexity(code: str) -> int:
    tree = ast.parse(code)
    complexity = 1  # Start with 1 for the default control flow
    for node in ast.walk(tree):
        if isinstance(
            node,
            (
                ast.If,
                ast.For,
                ast.While,
                ast.Try,
                ast.ExceptHandler,
            ),
        ):
            complexity += 1
    return complexity


code = """
def example_function(a, b):
    if a > b:
        return a
    else:
        return b
"""
print(f"Cyclomatic Complexity: {cyclomatic_complexity(code)}")
