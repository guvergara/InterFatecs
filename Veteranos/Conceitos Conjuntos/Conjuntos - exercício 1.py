# Suponha que você foi contratado para desenvolver uma funcionalidade
# no sistema do RH de um novo banco digital. Esse banco teve acesso
# ao cadastro de clientes de outras três empresas concorrentes
# (Nubank, C6 e Inter) e gostaria de saber quais são os potenciais
# clientes. Para isso, pediu que você gerasse um relatório com 12
# itens. Atenção, use apenas um print por item.

nubank = set(['ana', 'bia', 'clara', 'duda', 'fabio'])
c6     = set(['bia', 'elena', 'fabio', 'gabriel', 'helio'])
inter  = set(['duda', 'fabio', 'ilma', 'joão', 'katia', 'luiza'])

# 01) Quais são os clientes de cada uma, separadamente.
print(f'nubank: {nubank}, \nc6:{c6}, \ninter:{inter}')

# 02) Quais são os clientes de todas as concorrentes.
print("\ntodos:", nubank | c6 | inter)

# 03) Quais são os clientes da Nubank que também são clientes do C6.
print("\nnubank e c6:", nubank & c6)

# 04) Quais são os clientes da Nubank que também são clientes do Inter.
print("\nnubank e inter:",nubank & inter)

# 05) Quais são os clientes do C6 que também são clientes do Inter.
print("\nc6 e inter:", c6 & inter)

# 06) Quais são os clientes apenas da Nubank.
print("\napenas n6:",nubank-c6-inter)

# 07) Quais são os clientes apenas do C6.
print("\napenas c6:",c6-nubank-inter)

# 08) Quais são os clientes apenas do Inter.
print("\napenas inter:",inter-c6-nubank)

# 09) Clientes da Nubank e C6, mas não das duas ao mesmo tempo.
print("\nnubank ou c6:", (nubank | c6) - (nubank & c6) )

# 10) Clientes da Nubank e Inter, mas não das duas ao mesmo tempo.
print("\nnubank ou inter:", (nubank | inter) - (nubank & inter) )

# 11) Clientes do C6 e Inter, mas não dos dois ao mesmo tempo.
print("\nc6 ou inter:", (c6 | inter) - (c6 & inter))

# 12) Quais são os clientes das três simultaneamente.
print("\nTodas simultaneamente:",c6 & inter & nubank)

