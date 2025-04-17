from radon.complexity import cc_visit
from radon.metrics import h_visit
from radon.raw import analyze

with open("calculator_module.py") as f:
    code = f.read()

print("Цикломатична складність:")
for block in cc_visit(code):
    print(block)

print("\nМетрики Холстеда:")
print(h_visit(code))

print("\nSLOC:")
print(analyze(code))
