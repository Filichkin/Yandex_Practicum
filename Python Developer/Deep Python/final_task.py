DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return 'У тебя ' + str(count) + ' друзей.'
    # Здесь проверьте, что переменная query равна строке 'Кто все мои друзья?'
    elif query == 'Кто все мои друзья?':
        friends_string = ''
        # Чтобы получить перечень друзей - 
        # переберите словарь DATABASE в цикле
        for i in DATABASE.keys():
            friends_string = friends_string + i + ' '    # Добавляйте к переменной friends_string имя друга и пробел
        # Верните строку, составленную из 'Твои друзья: ' и friends_string 
        return 'Твои друзья: ' + friends_string
    elif query == 'Где все мои друзья?':
        city_string = ''
        for c in set(DATABASE.values()):
            city_string = city_string + c + ' '
        return 'Твои друзья в городах: ' + city_string
    else:
        return '<неизвестный запрос>'


print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))
