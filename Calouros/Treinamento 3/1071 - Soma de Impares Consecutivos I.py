menor = int(input())
maior = int(input())
soma = 0

if menor > maior:
    menor,maior = maior,menor


if menor%2 == 0:
    i = menor+1
else:
    i = menor+2


while i > menor and i<maior:
    soma += i
    i += 2

print(soma)
    

