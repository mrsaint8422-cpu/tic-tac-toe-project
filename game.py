import pygame
from gameparts import Board
# from gameparts.exceptions import FieldIndexError, CellOccupiedError


pygame.init()

# Здесь определены разные константы, например
# размер ячейки и доски, цвет и толщина линий.
# Эти константы используются при отрисовке графики
CELL_SIZE = 100
BOARD_SIZE = 3
WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (84, 84, 84)
O_COLOR = (242, 235, 211)
X_WIDTH = 15
O_WIDTH = 15
SPACE = CELL_SIZE // 4

# Настройка экрана
# Задать размер графического окна для игрового поля
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Установить заголовок окна
pygame.display.set_caption('Крестики-нолики')
# Заполнить фон окна заданным цветом
screen.fill(BG_COLOR)


# Функция, которая отвечает за отрисовку горизонтальных и вертикальных линий
def draw_lines():
    # Горизонтальные линии
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * CELL_SIZE),
            (WIDTH, i * CELL_SIZE),
            LINE_WIDTH
        )

    # Вертикальные линии
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * CELL_SIZE, 0),
            (i * CELL_SIZE, HEIGHT),
            LINE_WIDTH
        )


# Функция, которая отвечает за отрисовку фигур
# (крестиков и ноликов) на доске
def draw_figures(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    X_WIDTH
                )
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (
                        col * CELL_SIZE + SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + SPACE
                    ),
                    X_WIDTH
                )
            elif board[row][col] == 'O':
                pygame.draw.circle(
                    screen,
                    O_COLOR,
                    (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2
                    ),
                    CELL_SIZE // 2 - SPACE,
                    O_WIDTH
                )


def save_result(result):
    with open('results.txt', 'a', encoding='utf-8') as f:
        # Записать в файл содержимое переменной result
        f.write(result + '\n')


def main():
    game = Board()
    current_player = 'X'
    running = True
    draw_lines()
    # Основной цикл игры
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]

                clicked_col = mouse_x // CELL_SIZE
                clicked_row = mouse_y // CELL_SIZE

                if game.board[clicked_row][clicked_col] == ' ':
                    game.make_move(clicked_row, clicked_col, current_player)
                    # После каждого хода проверяем статус победителя.
                    if game.check_win(current_player):
                        # Сформировать строку
                        result = f'Победили {current_player}.'
                        # Вывести строку на печать
                        print(result)
                        # Добавить строку в файл
                        save_result(result)
                        running = False
                    elif game.is_board_full():
                        result = 'Ничья!'
                        print(result)
                        save_result(result)
                        running = False
                    current_player = 'O' if current_player == 'X' else 'X'
                    draw_figures(game.board)

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()

    # Запускается бесконечный цикл
    # while True:
    # В этом блоке содержатся операции, которые
    # могут вызвать исключение
    # try:
    # row = int(input('Введите номер строки: '))
    # if row < 0 or row >= game.field_size:
    #     raise FieldIndexError

    # column = int(input('Введите номер столбца: '))
    # if column < 0 or column >= game.field_size:
    #     raise FieldIndexError

    # Проверка свободной ячейки
    #     if game.board[row][column] != ' ':
    #         raise CellOccupiedError

    # except FieldIndexError:
    #     print(
    #         'Значение должно быть неотрицательным и меньше '
    #         f'{game.field_size}.'
    #     )
    #     print('Пожалуйста, введите значения для строки '
    #           'и столбца заново.')
    #     continue

    # except CellOccupiedError:
    #     print('Ячейка занята.')
    #     print('Введите другие координаты.')
    #     continue

    # except ValueError:
    #     print('Буквы вводить нельзя. Только числа.')
    #     print('Пожалуйста, введите значения для строки '
    #           'и столбца заново.')
    #     continue

    # except Exception as e:
    #     print(f'Возникла ошибка: {e}')
    #     continue

    # # Если в блоке try исключения не возникло...
    # else:
    #     break

    # game.make_move(row, column, current_player)
    # print('Ход сделан!')
    # game.display()
