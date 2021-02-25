import AGame
import Functions
import random

sudokus = []
sizeIsOk = False
sudokuSize = 0

[sudokus.append(AGame.ASudoku(sor.strip())) for sor in open("feladvanyok.txt")]

print(f"Task 3.: {len(sudokus)} sudoku are loaded.")

while not sizeIsOk:
    sizeIsOk, sudokuSize = Functions.InputIsANumber(input("Task 4.: Please type in the size of the sudoku [4..9]: "))
    if sizeIsOk:
        sudokus_i = Functions.IndexesOfTheFoundSudoku(sudokuSize, sudokus)
        print(f"There are {len(sudokus_i)} from the {sudokuSize}x{sudokuSize} size of sudoku in the file.")
        random_kiv = sudokus_i[random.randint(0, len(sudokus_i) - 1)]
        actualSudokuNumbers, actualSudokuPercent = Functions.ChoosenPercent(sudokus[random_kiv])
        print(f"Task 5.: The choosen sudoku is: \n{actualSudokuNumbers} ")
        print(f"Task 6.: The completition of the sudoku is: {actualSudokuPercent} %")
        print(f"Task 7.: Sudoku is drawn")
        sudokus[random_kiv].DrawOut()
        print(f"Task 8.: sudoku{sudokuSize}.txt file with {len(sudokus_i)} sudoku(s) have been created.")

# Console.ReadKey()
input(f"\nPress Enter to close.")
