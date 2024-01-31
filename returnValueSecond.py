def greet(lang):
    if lang == "es":
        return 'Hola'
    elif lang == 'ru':
        return 'Здравствуйте'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('en'), 'Glenn')
print(greet('es'), 'Nicolas')
print(greet('ru'), 'Иван')
print(greet('fr'), 'Pierre')
