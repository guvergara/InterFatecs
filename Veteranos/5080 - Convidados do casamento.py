listaO = set()
listaA = set()
listaF = set()

def impressao(mensagem, lista):
    print(f"""--------------------
{mensagem}
--------------------""")
    for c in lista:
        print(c)
    if mensagem != "POR APENAS UM DELES":
        print("*")

nome = input()
while nome != "ACABOU":
    nome,convite = nome.split(';')
    if convite == "noivo":
        listaO.add(nome)
    else:
        listaA.add(nome)
    nome = input()

listaF = sorted(listaO | listaA)
lista_ambos = sorted(listaA & listaO)
lista_apenasA = sorted(listaA - listaO)
lista_apenasO = sorted(listaO - listaA)
lista_apenas = sorted(listaA ^ listaO)



impressao("LISTA FINAL", listaF)
impressao("APENAS NOIVA", lista_apenasA)
impressao("APENAS NOIVO", lista_apenasO)
impressao("POR AMBOS", lista_ambos)
impressao("POR APENAS UM DELES", lista_apenas)




    
