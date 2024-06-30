def read_sudoku(file_name):
    with open(file_name, 'r') as file:
        grid = []
        for line in file:
            grid.append([int(num) if num != '_' else 0 for num in line.strip()])
    return grid
