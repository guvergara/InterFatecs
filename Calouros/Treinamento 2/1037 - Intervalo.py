A = float(input())
aux = 25
inter = False
if A >= 0:
    for i in range(4):
        if A/aux <=1 and not inter:
            if aux == 25:
                print(f'Intervalo [{aux-25},{aux}]')
                inter = not inter
            else:
                print(f'Intervalo ({aux-25},{aux}]')
                inter = not inter
        aux += 25
if not inter:
    print("Fora de intervalo")

