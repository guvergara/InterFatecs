# ╔═════════════════════════════════════════════════════╗
# ║ Autor: Prof. Lucio Nunes de Lira                    ║
# ╠═════════════════════════════════════════════════════╣
# ║ Arquivo...: Resumo sobre conjuntos em Python.       ║
# ║ Compilador: CPython (3.11.4)                        ║
# ║ Versão....: A (rev. 2)                              ║
# ╚═════════════════════════════════════════════════════╝

# ═══════════════════════════════════════════════════════
# DEFINIÇÃO
# ═══════════════════════════════════════════════════════

# Um conjunto é uma coleção não ordenada de itens únicos.

# ═══════════════════════════════════════════════════════
# OPERAÇÕES COMUNS SOBRE UM CONJUNTO
# ═══════════════════════════════════════════════════════

# ─────────────────────────────────────────────────
# Criação de um conjunto vazio
# ─────────────────────────────────────────────────

C = set()

# Obs.: C = {} não cria um conjunto vazio, mas sim 
#       um dicionário vazio.

# ─────────────────────────────────────────────────
# Verificação do tipo
# ─────────────────────────────────────────────────

print(type(C))

# ─────────────────────────────────────────────────
# Criação de um conjunto com itens
# ─────────────────────────────────────────────────

C = {10, 20, 10, 30, 10, 40, 40, 50}
print(C) 

C = set([10, 20, 10, 30, 10, 40, 40, 50])
print(C)

C = set((10, 20, 10, 30, 10, 40, 40, 50))
print(C)

C = set(range(10))
print(C)

C = set('Abracadabra')
print(C)

# ─────────────────────────────────────────────────
# Tamanho do conjunto (quantidade de itens)
# ─────────────────────────────────────────────────

print(len(C))

# ─────────────────────────────────────────────────
# Adição de itens
# ─────────────────────────────────────────────────
# Caso o item já exista no conjunto, a operação
# não terá efeito.
# ─────────────────────────────────────────────────

# Um item por vez.

C = set()
C.add('ana')
C.add(3.1415)
C.add(123)
C.add(True)
C.add(('Matrix 4', 2021))
C.add(range(10, 16, 2))
C.add(['Luiz', 'Bruno', 'Danilo']) # lançará uma exceção
                                   # (lista é unhashable).

# Vários itens de uma vez.

C = set()
C.update([10, False, 89.5, 30])

# Obs.: O método adiciona todos os itens do argumento
#       iterável, mas não o iterável em si.

# ─────────────────────────────────────────────────
# Remoção de itens
# ─────────────────────────────────────────────────

# Tentativas de remover itens que não pertencem ao
# conjunto são ignoradas.

C.discard(10)
C.discard(10) 

# Tentativas de remover itens que não pertencem ao
# conjunto geram exceções.

C.remove(False)
C.remove(False) 

# Remove e retorna um item arbitrário.
# Lança uma exceção se o conjunto estiver vazio.

x = C.pop() 

# Remove todos os itens do conjunto.

C.clear() 

# ─────────────────────────────────────────────────
# Verificação de pertinência
# ─────────────────────────────────────────────────

C = set('Megan Denise Fox')
print(C)

x = 'F'

if x in C:
    print(f'{x} está no conjunto')
else:
    print(f'{x} não está no conjunto')

if x not in C:
    print(f'{x} não está no conjunto')
else:
    print(f'{x} está no conjunto')

# ─────────────────────────────────────────────────
# Iteração sobre os itens
# ─────────────────────────────────────────────────

C = set('Lucio')

for x in C:
    print(x)

# ─────────────────────────────────────────────────
# Cópia (rasa, não faz sentido cópia profunda)
# ─────────────────────────────────────────────────    

A = {10, 20, 30}
B = A.copy()
print(f'A = {A}\nB = {B}')
B.discard(20)
print(f'A = {A}\nB = {B}')

# ═══════════════════════════════════════════════════════
# OPERAÇÕES COMUNS ENTRE CONJUNTOS
# ═══════════════════════════════════════════════════════

# ─────────────────────────────────────────────────
# Igualdade
# ─────────────────────────────────────────────────

A = {5, 3, 1, 4, 2, 5, 4}
B = {1, 2, 3, 4, 5}
print(f'A = {A}\nB = {B}')

resp = (A == B)
print(f'A == B -> {resp}')

resp = (A != B)
print(f'A != B -> {resp}')

# ─────────────────────────────────────────────────
# Disjunção
# ─────────────────────────────────────────────────
# Verifica se os conjuntos são disjuntos, isto é,
# se não há itens comuns entre os conjuntos.
# ─────────────────────────────────────────────────

A = {'a', 'e', 'i', 'o', 'u'}
B = {'b', 'c', 'd'}
C = {'x', 'y', 'z', 'u'}
print(A.isdisjoint(B))
print(A.isdisjoint(C))

# ─────────────────────────────────────────────────
# Subconjunto
# ─────────────────────────────────────────────────
# Verifica se o conjunto da esquerda está contido
# no conjunto da direita.
# ─────────────────────────────────────────────────

A = {10, 20, 30}
B = {10, 20, 30, 40}
print(f'A = {A}\nB = {B}')

# 1ª opção
resp = (A <= B)
print(f'A é subconjunto de B? {resp}')

# 2ª opção (B é convertido se necessário)
resp = A.issubset(B)
print(f'A é subconjunto de B? {resp}')

# ─────────────────────────────────────────────────
# Subconjunto próprio
# ─────────────────────────────────────────────────
# Verifica se o conjunto da esquerda está contido
# no conjunto da direita, porém são diferentes.
# ─────────────────────────────────────────────────

A = {10, 20, 30, 40}
B = {10, 20, 30}
C = {10, 20, 30, 40}
print(f'A = {A}\nB = {B}\nC = {C}')

resp = (A < B)
print(f'A é subconjunto próprio de B? {resp}')

resp = (A < C)
print(f'A é subconjunto próprio de C? {resp}')

# ─────────────────────────────────────────────────
# Superconjunto
# ─────────────────────────────────────────────────
# Verifica se o conjunto da esquerda contém o
# conjunto da direita.
# ─────────────────────────────────────────────────

A = {10, 20, 30, 40}
B = {10, 20, 30}
print(f'A = {A}\nB = {B}')

# 1ª opção
resp = (A >= B)
print(f'A é superconjunto de B? {resp}')

# 2ª opção (B é convertido se necessário)
resp = A.issuperset(B)
print(f'A é superconjunto de B? {resp}')

# ─────────────────────────────────────────────────
# Superconjunto próprio
# ─────────────────────────────────────────────────
# Verifica se o conjunto da esquerda contém o
# conjunto da direita, porém são diferentes.
# ─────────────────────────────────────────────────

A = {10, 20, 30, 40}
B = {10, 20, 30}
C = {10, 20, 30, 40}
print(f'A = {A}\nB = {B}\nC = {C}')

resp = (A > B)
print(f'A é superconjunto próprio de B? {resp}')

resp = (A > C)
print(f'A é superconjunto próprio de C? {resp}')

# ─────────────────────────────────────────────────
# União entre conjuntos
# ─────────────────────────────────────────────────
# Gera um novo conjunto com todos os itens de ambos
# os conjuntos.
# ─────────────────────────────────────────────────

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(f'A = {A}\nB = {B}')

# 1ª opção
C = A | B
print(f'A | B -> {C}')

# 2ª opção (B é convertido se necessário)
C = A.union(B)
print(f'A | B -> {C}')

# A diferença entre o operador | e o método union
# é que o operador exige que ambos os operandos
# sejam conjuntos, com o método basta que o
# argumento seja um iterável. Veja os exemplos:

A | [4, 5, 77, 99] # Erro, o operando da direita não é um conjunto.
A.union([4, 5, 77, 99]) # Funciona, pois o argumento será convertido 
                        # para conjunto antes da aplicação da união.
A | set([4, 5, 77, 99]) # Equivalente ao método union.

# ─────────────────────────────────────────────────
# Intersecção entre conjuntos
# ─────────────────────────────────────────────────
# Gera um novo conjunto com os itens comuns entre
# ambos os conjuntos.
# ─────────────────────────────────────────────────

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(f'A = {A}\nB = {B}')

# 1ª opção
C = A & B
print(f'A & B -> {C}')

# 2ª opção (B é convertido se necessário)
C = A.intersection(B)
print(f'A & B -> {C}')

# ─────────────────────────────────────────────────
# Diferença entre conjuntos
# ─────────────────────────────────────────────────
# Gera um novo conjunto com os itens do conjunto da
# esquerda que não estejam no conjunto da direita.
# ─────────────────────────────────────────────────

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(f'A = {A}\nB = {B}')

# 1ª opção
C = A - B
print(f'A - B -> {C}')

# 2ª opção (B é convertido se necessário)
C = A.difference(B)
print(f'A - B -> {C}')

# ─────────────────────────────────────────────────
# Diferença simétrica entre conjuntos
# ─────────────────────────────────────────────────
# Gera um novo conjunto com os itens dos dois
# conjuntos, exceto aqueles que perteçam a ambos.
# ─────────────────────────────────────────────────

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(f'A = {A}\nB = {B}')

# 1ª opção
C = A ^ B
print(f'A ^ B -> {C}')

# 2ª opção (B é convertido se necessário)
C = A.symmetric_difference(B)
print(f'A ^ B -> {C}')

# Equivalente.
print(f'A ^ B -> {(A | B) - (A & B)}')

# Equivalente.
print(f'A ^ B -> {(A - B) | (B - A)}')
