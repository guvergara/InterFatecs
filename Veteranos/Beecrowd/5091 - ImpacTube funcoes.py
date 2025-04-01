def cria_canais(qtd_canais):
    canais = []
    for i in range (qtd_canais):
        nome, inscritos, monetizacao, premium = input().split(';')
        inscritos = int(inscritos)
        monetizacao = float(monetizacao)
        premium = premium == 'sim'
        canais.append([nome,inscritos,monetizacao,premium])
    return canais

def cria_bonus(canais, com_premium, sem_premium):
    bonus = []
    for n,i,m,p in canais:
        v = m
        if p:
            v += com_premium * (i // 1000)
        else:
            v += sem_premium * (i // 1000)
        bonus.append([n,v])
    return bonus

def exibe_bonus(bonus):
    print('-' * 5)
    print("BÔNUS")
    print('-' * 5)
    for n, v in bonus:
        print(f'{n}: R$ {v:.2f}')

def main():  
    qtd_canais = int(input())
    canais = cria_canais(qtd_canais)
    com_premium = float(input())
    sem_premium = float(input())
    bonus = cria_bonus(canais, com_premium, sem_premium)
    exibe_bonus(bonus)

main()



       
