from SudokuSolver import SudokuSolver
from SudokuReader import read_sudoku

def main():
    file_name = input("Entrez le nom du fichier contenant la grille de Sudoku : ")
    grid = read_sudoku(file_name)
    solver = SudokuSolver(grid)

    print("Grille de Sudoku initiale :")
    solver.print_grid()
    print()

    if solver.solve():
        print("Grille de Sudoku résolue :")
        solver.print_grid()
    else:
        print("Impossible de résoudre cette grille de Sudoku.")

if __name__ == "__main__":
    main()