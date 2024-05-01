class Board:
    def __init__(self):
        self.size = 6
        self.grid = [['O' for _ in range(self.size)] for _ in range(self.size)]
        self.ships = []
        self.attacks = []

    def place_ship(self, ship):
    
        for pos in ship.positions():
            if not (0 <= pos[0] < self.size and 0 <= pos[1] < self.size):
                raise ValueError("Корабль находится за пределами границ")
            for other_ship in self.ships:
                if pos in other_ship.positions():
                    raise ValueError("Корабли перекрываются или находятся слишком близко")
        self.ships.append(ship)
        for row, col in ship.positions():
            self.grid[row][col] = '■'

    def attack(self, row, col):
        if (row, col) in self.attacks:
            raise ValueError("Уже атаковали эту позицию")
        self.attacks.append((row, col))
        for ship in self.ships:
            if ship.hit(row, col):
                self.grid[row][col] = 'X'
                if ship.is_sunk():
                    print(f"Корабль{ship.start_row+1},{ship.start_col+1} затонул!")
                return True
        self.grid[row][col] = 'T'
        return False

    def all_ships_sunk(self):
        return all(ship.is_sunk() for ship in self.ships)

    def display(self):
        header = "  | " + " | ".join(str(i + 1) for i in range(self.size)) + " |"
        print(header)
        for i in range(self.size):
            row_display = f"{i + 1} | " + " | ".join(self.grid[i]) + " |"
            print(row_display)