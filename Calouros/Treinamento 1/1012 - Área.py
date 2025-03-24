A,B,C = map(float, input().split())

print(f"""TRIANGULO: {A*C/2:.3f}
CIRCULO: {3.14159*C*C:.3f}
TRAPEZIO: {(A+B)*C/2:.3f}
QUADRADO: {B*B:.3f}
RETANGULO: {A*B:.3f}""")

