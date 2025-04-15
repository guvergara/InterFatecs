post_amount = 0
language_amount = 0
posts = []
languages = []
amounts = []

post_amount = int(input())
for i in range(post_amount):
    posts.append(input())

language_amount = int(input())
for i in range(language_amount):
    languages.append(input())
    amounts.append(0)

for p in posts:
    pos = 0
    for l in languages:
        if (' ' +l + ' ').lower() in p.lower():
            amounts[pos] += 1
        pos += 1

for pos in range(language_amount):
    print(f'{languages[pos]} {amounts[pos]}')
            
            
