import random
from Board import Board
from ship import Ship

class Game:
    def __init__(self):
        self.player_board = Board()
        self.ai_board = Board()
        self.setup_boards()

    def is_valid_position(self, board, ship):
        # Проверка на размещение
        for (row, col) in ship.positions():
            if not (0 <= row < board.size and 0 <= col < board.size):
                return False
            # Проверяем клетки 
            for d_row in [-1, 0, 1]:
                for d_col in [-1, 0, 1]:
                    check_row, check_col = row + d_row, col + d_col
                    if 0 <= check_row < board.size and 0 <= check_col < board.size:
                        if board.grid[check_row][check_col] == '■':
                            return False
        return True

    def place_ships(self, board, ships):
        # Расставление на доске
        for length, count in ships:
            for _ in range(count):
                placed = False
                while not placed:
                    horizontal = random.choice([True, False])
                    row = random.randint(0, board.size - (length if horizontal else 1))
                    col = random.randint(0, board.size - (1 if horizontal else length))
                    new_ship = Ship(row, col, length, horizontal)
                    if self.is_valid_position(board, new_ship):
                        board.place_ship(new_ship)
                        placed = True

    def setup_boards(self):
        ships_to_place = [(3, 1), (2, 2), (1, 4)]  # дл кораб, кол кораб
        self.place_ships(self.player_board, ships_to_place)
        self.place_ships(self.ai_board, ships_to_place)

    def player_move(self):
        while True:
            try:
                row = int(input("Введите строку (1-6): ")) - 1
                col = int(input("Введите столбец (1-6): ")) - 1
                if not (0 <= row < 6 and 0 <= col < 6):
                    raise ValueError("Некорректные координаты. Пожалуйста, введите число от 1 до 6 для строки и столбца.")
                hit = self.ai_board.attack(row, col)
                print("Попадание!" if hit else "Промах!")
                break
            except ValueError as e:
                print(e)

    def ai_move(self):
        while True:
            row, col = random.randint(0, 5), random.randint(0, 5)
            if (row, col) not in self.ai_board.attacks:
                self.player_board.attack(row, col)
                break

    def play(self):
        print("Добро пожаловать в игру 'Морской бой'!")
        while not (self.player_board.all_ships_sunk() or self.ai_board.all_ships_sunk()):
            print("\nДоска игрока:")
            self.player_board.display()
            print("\nДоска ИИ:")
            self.ai_board.display()
            self.player_move()
            if self.ai_board.all_ships_sunk():
                print("Игрок побеждает!")
                break
            self.ai_move()
            if self.player_board.all_ships_sunk():
                print("ИИ побеждает!")
                break


game = Game()
game.play()
