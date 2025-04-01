canais = []

qtd_canais = int(input())


for i in range (qtd_canais):
    nome, inscritos, monetizacao, premium = input().split(';')
    inscritos = int(inscritos)
    monetizacao = float(monetizacao)
    premium = premium == 'sim'
    canais.append([nome,inscritos,monetizacao,premium])


com_premium = float(input())
sem_premium = float(input())


print(f'''-----
BÔNUS
-----''')
for nome, inscritos, monetizacao, premium in canais:
    valor = monetizacao
    if premium:
        valor += com_premium * ( inscritos // 1000 )
        print(f'{nome}: R$ {valor:.2f}')
    else:
        valor += sem_premium * ( inscritos // 1000 )
        print(f'{nome}: R$ {valor:.2f}')
       
