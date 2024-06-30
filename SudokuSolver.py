class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid
        self.original_grid = [row[:] for row in grid]  # Copie de la grille initiale

    def is_valid(self, row, col, num):
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False
        
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.grid[i][j] == num:
                    return False
        
        return True

    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.grid[row][col] = num
                            if self.solve():
                                return True
                            self.grid[row][col] = 0
                    return False
        return True

    def print_grid(self):
        for row in range(9):
            for col in range(9):
                if self.original_grid[row][col] == 0:
                    print(f"\033[91m{self.grid[row][col]}\033[0m", end=" ")
                else:
                    print(f"\033[92m{self.grid[row][col]}\033[0m", end=" ")
            print()
