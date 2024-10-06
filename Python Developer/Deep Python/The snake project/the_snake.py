from random import randint

import pygame

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Стартовая позиция:
COORDS_START_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Цвет камня
STONE_COLOR = (139, 69, 19)

# Скорость движения змейки:
SPEED = 8

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
screen.fill(BOARD_BACKGROUND_COLOR)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


class GameObject:
    """GameObject — это базовый класс, от которого наследуются другие игровые
    объекты.
    """

    def __init__(self, position=None, body_color=None):
        """Конструктор класса GameObject - инициализирует базовые атрибуты
        объекта, такие как его позиция и цвет.
        """
        self.position = position
        self.body_color = body_color

    def draw(self):
        """Это абстрактный метод, который предназначен для переопределения
        в дочерних классах. Этот метод должен определять, как объект будет
        отрисовываться на экране.
        """
        raise NotImplementedError(
            'Этот метод должен быть переопределен'
        )


class Apple(GameObject):
    """Класс унаследованный от GameObject, описывающий яблоко
    и действия с ним.
    """

    def __init__(self, body_color=APPLE_COLOR):
        """Конструктор класса Apple."""
        super().__init__()
        self.body_color = body_color
        self.randomize_position()

    def randomize_position(self,
                           occuped_positions=[COORDS_START_CENTER]):
        """Устанавливает случайное положение яблока и камня на игровом поле."""
        self.position = (randint(0, GRID_SIZE) * GRID_SIZE,
                         randint(0, GRID_SIZE) * GRID_SIZE)
        if self.position in occuped_positions:
            self.randomize_position(occuped_positions)

    def draw(self):
        """Отрисовывает яблоко и камень на игровой поверхности."""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Stone(Apple):
    """Класс унаследованный от Apple, описывающий камень
    и действия с ним.
    """

    def __init__(self):
        """Конструктор класса Stone."""
        super().__init__(body_color=STONE_COLOR)

    def reset_stone(self):
        """Затирает старый камень при съедании яблока."""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, rect)


class Snake(GameObject):
    """Класс унаследованный от GameObject, описывающий змейку
    и действия с ней.
    """

    def __init__(self):
        super().__init__(body_color=SNAKE_COLOR)
        self.reset()

    def update_direction(self):
        """Обновляет направление движения змейки."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        """Обновляет позицию змейки (координаты каждой секции),
        добавляя новую голову в начало списка positions и
        удаляя и затирая последний элемент, если длина змейки не увеличилась.
        """
        x_head, y_head = self.get_head_position()
        x_point, y_point = self.direction

        new_x = (x_head + x_point * GRID_SIZE) % SCREEN_WIDTH
        new_y = (y_head + y_point * GRID_SIZE) % SCREEN_HEIGHT

        self.positions.insert(0, (new_x, new_y))
        if len(self.positions) > self.length:
            self.last = self.positions.pop()
        else:
            self.last = None

    def draw(self):
        """Oтрисовывает змейку на экране."""
        x_point, y_point = self.get_head_position()

        rect = pygame.Rect(x_point, y_point, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def get_head_position(self):
        """Возвращает позицию головы змейки."""
        return self.positions[0]

    def reset(self):
        """Сбрасывает змейку в начальное состояние после столкновения
        с собой или с камнем.
        """
        self.length = 1
        self.last = None
        self.positions = [COORDS_START_CENTER]
        self.direction = RIGHT
        self.next_direction = None


def handle_keys(game_object):
    """Управляет движениями клавиш."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    """Функция запуска кода."""
    pygame.init()
    snake = Snake()
    stone = Stone()
    apple = Apple()
    while True:
        clock.tick(SPEED)
        handle_keys(snake)
        snake.update_direction()
        snake.move()
        apple.draw()
        stone.draw()
        if snake.get_head_position() == apple.position:
            stone.reset_stone()
            apple.randomize_position(snake.positions)
            stone.randomize_position(snake.positions + list(apple.position))
            snake.length += 1
        elif (snake.positions.count(snake.get_head_position()) > 1
                or snake.get_head_position() == stone.position):
            snake.reset()
            apple.randomize_position(snake.positions)
            stone.randomize_position(snake.positions + list(apple.position))
            screen.fill(BOARD_BACKGROUND_COLOR)
        snake.draw()
        pygame.display.update()


if __name__ == '__main__':
    main()
