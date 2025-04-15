#crie a funcao recursiva fat(n), que calcula o fatorial
#de um numero natural n
def fat(n):
    if n==0: return 1       #base
    else: return n*fat(n-1) #passo


#crie a funcao recursiva pot(x,n) que calcula a potencia
#de um numero real x =! 0 elevado a um numero natural n
def pot(x,n):
    if n == 0:
        return 1
    else:
        return x*pot(x,n-1)

#crie a funcao recursiva termial(n), que calcula a soma dos n
#primeiros numeros naturais(n>=0)
def termial(n):
    if n==0:
        return 0
    else:
        return n+termial(n-1)
        
#crie a funcao recursiva cr(n), que exibe uma contagem regressiva
#de n>=0 ate 1
def cr(n):
    if n==0:
        return 
    else:
       print(n)
       cr(n-1)

#crie a funcao recursiva cp(n), que exibe uma contagem progressiva
#de 1 ate n>= 0
def cp(n):
    if n==0:
        return
    else:
        cp(n-1)
        print(n)

#crie a funcao vv(n), que eexibe uma contagem regressiva e
#depois progressiva de n>=0 numeros
def vv(n):
    if n==0:
        return
    else:
        print(n)
        vv(n-1)
        print(n)
        

#crie a funcao recursiva binario(n), que exibe um natural
#n>=0 em binario
def binario(n):
    if n<2:
        print(n,end='')
    else:
        binario(n//2)
        print(n%2,end='')
