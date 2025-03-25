peso_bandeja = float(input())
peso_total = float(input())
preco = float(input())
peso_comida = peso_total - peso_bandeja
print(f'{peso_comida * preco:.2f}')
