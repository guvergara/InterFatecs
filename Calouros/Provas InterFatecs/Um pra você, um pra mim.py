c,n = input().split()
n = int(n)
v = a = 0
for i in range(n):
    if c == 'V':
        v += int(input())
        c = 'A'
    else:
        a += int(input())
        c = 'V'
    

print(f'VOCE: {v} AMIGO: {a}')
