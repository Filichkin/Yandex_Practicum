from datetime import datetime as dt
from random import randint

from access_control import access_control
from constants import ADMIN_USERNAME, UNKNOWN_COMMAND


class Game:
    """Game — это базовый класс, от которого наследуются другие игровые
    объекты.
    """

    def __init__(self):
        """Конструктор класса Game - инициализирует базовые атрибуты
        объекта, такие как его позиция и цвет.
        """
        self.start_time = dt.now()

    def guess_number(self) -> None:
        username = self.get_username()
        # Счётчик игр в текущей сессии.
        total_games = 0
        while True:
            total_games += 1
            self.game(username, total_games)
            play_again = input(f'\nХотите сыграть ещё? (yes/no) ')
            if play_again.strip().lower() not in ('y', 'yes'):
                break

    def game(self, username: str, total_games: int) -> None:
        # Получаем случайное число в диапазоне от 1 до 100.
        number = randint(1, 100)
        print(
            '\nУгадайте число от 1 до 100.\n'
            'Для выхода из текущей игры введите команду "stop"'
        )
        while True:
            # Получаем пользовательский ввод, 
            # отрезаем лишние пробелы и переводим в нижний регистр.
            user_input = input('Введите число или команду: ').strip().lower()

            match user_input:
                case 'stop':
                    break
                case 'stat':
                    self.get_statistics(total_games, username=username)
                case 'answer':
                    self.get_right_answer(number, username=username)
                case _:
                    try:
                        guess = int(user_input)
                    except ValueError:
                        print(UNKNOWN_COMMAND)
                        continue

                    if self.check_number(username, guess, number):
                        break

    @access_control
    def get_statistics(self, total_games: int, *args, **kwargs) -> None:
        game_time = dt.now() - self.start_time
        print(f'Общее время игры: {game_time}, текущая игра - №{total_games}')

    @staticmethod
    def get_username() -> str:
        username = input('Представьтесь, пожалуйста, как Вас зовут?\n').strip()
        if username == ADMIN_USERNAME:
            print(
                '\nДобро пожаловать, создатель! '
                'Во время игры вам доступны команды "stat", "answer"'
            )
        else:
            print(f'\n{username}, добро пожаловать в игру!')
        return username

    @staticmethod
    def check_number(username: str, guess: int, number: int) -> bool:
        # Если число угадано...
        if guess == number:
            print(f'Отличная интуиция, {username}! Вы угадали число :)')
            # ...возвращаем True
            return True

        if guess < number:
            print('Ваше число меньше того, что загадано.')
        else:
            print('Ваше число больше того, что загадано.')
        return False

    @staticmethod
    @access_control
    def get_right_answer(number: int, *args, **kwargs) -> None:
        print(f'Правильный ответ: {number}')


if __name__ == '__main__':
    print(
        'Вас приветствует игра "Угадай число"!\n'
        'Для выхода нажмите Ctrl+C'
    )
    test = Game()
    test.guess_number()
