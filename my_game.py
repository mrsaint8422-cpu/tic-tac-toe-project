from gameparts import Board
from gameparts.exceptions import FieldIndexError
print(Board.__doc__)


def main():
    # Создать игровое поле — объект класса Board
    game = Board()
    game_running = True
    while game_running:
        game.display()
        try:
            user_input = input(
                'Для совершения хода введите номер строки, столбца и символ '
                'игрока (например, 0 1 X/O) или exit для выхода:')
            if user_input.lower() == 'exit':
                print('Игра завершена!')
                break
            else:
                parts = user_input.split()

                # 1. Проверка количества частей
                if len(parts) != 3:
                    raise FieldIndexError

                # 2. Проверка и конвертация строки
                row = int(parts[0])

                # 3. Умная проверка строки
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError

                # 4. Проверка и конвертация столбца
                col = int(parts[1])

                # 5. Умная проверка столбца
                if col < 0 or col >= game.field_size:
                    raise FieldIndexError

                # 6. Проверка игрока
                player = parts[2].upper()
                if player not in ('X', 'O'):
                    raise FieldIndexError

                game.make_move(row, col, player)

        except (FieldIndexError,):
            print()
            print('Пожалуйста, введите правильные значения!')
            continue

        except ValueError:
            print()
            print('Буквы для номера строки и столбца вводить'
                  ' нельзя. Только числа.')
            print('Пожалуйста, введите значения для строки и столбца заново.')
            continue

        except Exception as e:
            print(f'Возникла ошибка: {e}')
            continue


if __name__ == '__main__':
    main()
