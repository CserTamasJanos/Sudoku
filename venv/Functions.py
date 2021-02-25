# Check whether input is a number, if so it checks if it is between in the given interval.
def InputIsANumber(number):
    try:
        sudSize = int(number)
        if 3 < sudSize < 10:
            return True, sudSize
        else:
            return False, sudSize
    except:
        return False, -1


#Asks the filtered sudoku list and the size. Returns an a list of indexes based on the sudokuSize.
#  In addition to the above, it also writes to the file named after the size of it (Task 8).
def IndexesOfTheFoundSudoku(sudokuSize, foundSudokus):
    file = open(f"sudoku{sudokuSize}.txt", "w")
    indexek = []
    index = 0
    for aSudoku in foundSudokus:
        actualSudo = ""
        if aSudoku.Ssize == sudokuSize:
            indexek.append(index)
            for sz in aSudoku.beginning:
                actualSudo += str(sz)
            file.write(f"{actualSudo}\n")
        index += 1

    return indexek


#The function runs through the random list of previously requested sizes
# and returns the printable format and occupancy in percentage.
def ChoosenPercent(allList):
    numbers = ""
    percent = 0
    for actualNumber in allList.beginning:
        numbers += str(actualNumber)
        if actualNumber != '0':
            percent += 1

    return numbers, round((percent/len(numbers))*100)