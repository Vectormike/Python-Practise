#DICT[key] --> value
#{key1: value1, key2: value2, key3: value3}

phone_book = {
    'mike': ['08086249721', 'mike@mike.com'],
    'victor': ['08086245698', 'victor@jona.com'],
    'mahel': ['08867327688', 'mahel@majid.com'],
    'nikki': ['07068685758', 'niki@tunde.com'],
    }

#to output a contact
print(phone_book['mike'][1])
print(phone_book['victor'][0])
print(phone_book['mahel'][1])
print(phone_book['nikki'][0])



cinema_movies = {
    'center1': 'Jumanji',
    'center2': 'Thor Ragnarok',    
    'center3': 'Infinity War',
    'center4': 'Hit man',
    'center5': 'The intern',
    'center6': 'Amateur',
    'center7': 'Rampage',
    'center8': 'Den of Theives',
    'center9': 'Special Ops',
    'center10': 'G.I Joe',
    'center11': 'Silicon valley',
    }

print('Available movies are: Jumanji, Thor Ragnarok, Infinity War, Hit man,  The intern, Amateur, Rampage, Den of Theives, Special Ops, G.I Joe' )
choice = input('What movie do you want?')
