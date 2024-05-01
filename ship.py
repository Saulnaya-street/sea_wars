class Ship:
    def __init__(self, start_row, start_col, length, horizontal):
        self.start_row = start_row
        self.start_col = start_col
        self.length = length
        self.horizontal = horizontal
        self.hits = 0

    def positions(self):
        return [(self.start_row + i if not self.horizontal else self.start_row,
                 self.start_col + i if self.horizontal else self.start_col) for i in range(self.length)]

    def hit(self, row, col):
        if (row, col) in self.positions():
            self.hits += 1
            return True
        return False

    def is_sunk(self):
        return self.hits == self.length