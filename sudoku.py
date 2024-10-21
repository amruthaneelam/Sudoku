import tkinter as tk
import random

def print_board(board):
    for row in range(9):
        for col in range(9):
            cell = board[row][col]
            entry = tk.Entry(root, width=5, font=('Arial', 18), justify='center')
            entry.grid(row=row, column=col)
            if cell != 0:
                entry.insert(tk.END, str(cell))
                entry.config(state='readonly')

def check_valid(board, row, col, num):
    # Check row
    if num in board[row]:
        return False
    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False
    # Check 3x3 square
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return (r, c)
    return None

def solve(board):
    empty = find_empty(board)
    if not empty:
        return True  # Puzzle solved
    row, col = empty

    for num in range(1, 10):
        if check_valid(board, row, col, num):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0  # Backtrack
    return False

def generate_sudoku():
    board = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(3):
        fill_box(board, i * 3, i * 3)
    solve(board)
    remove_numbers(board, 40)  # Adjust difficulty
    return board

def fill_box(board, row, col):
    nums = list(range(1, 10))
    random.shuffle(nums)
    for r in range(3):
        for c in range(3):
            board[row + r][col + c] = nums.pop()

def remove_numbers(board, count):
    while count > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            count -= 1

def check_solution():
    board = [[0 if entry.get() == '' else int(entry.get()) for entry in row] for row in entries]
    if find_empty(board) is None:
        result_label.config(text="Congratulations! You've solved the Sudoku!")
    else:
        result_label.config(text="Keep trying!")

def main():
    global root, entries, result_label
    root = tk.Tk()
    root.title("Sudoku Game")
    
    board = generate_sudoku()
    
    entries = [[None for _ in range(9)] for _ in range(9)]
    
    print_board(board)
    
    result_label = tk.Label(root, text="", font=('Arial', 16))
    result_label.grid(row=9, column=0, columnspan=9)
    
    check_button = tk.Button(root, text="Check Solution", command=check_solution)
    check_button.grid(row=10, column=0, columnspan=9)

    root.mainloop()

if __name__ == "__main__":
    main()
