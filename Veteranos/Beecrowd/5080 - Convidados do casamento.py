def impressao(mensagem, lista):
    print('-' * 20)
    print(mensagem)
    print('-' * 20)
    for convidado in lista:
        print(convidado)
    if mensagem != "POR APENAS UM DELES":
        print("*")

listaO = set()
listaA = set()

nome = input()
while nome != "ACABOU":
    nome,convite = nome.split(';')
    if convite == "noivo":
        listaO.add(nome)
    else:
        listaA.add(nome)
    nome = input()

impressao("LISTA FINAL", sorted(listaO | listaA) )
impressao("APENAS NOIVA", sorted(listaA - listaO) )
impressao("APENAS NOIVO", sorted(listaO - listaA) )
impressao("POR AMBOS", sorted(listaA & listaO) )
impressao("POR APENAS UM DELES", sorted(listaA ^ listaO) )




    
