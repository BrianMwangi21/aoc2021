def run_my_boy():
    bingo_marked, bingo_boards = readFile()
    
    print(f"Part One : Score is {part_one(bingo_marked, bingo_boards)}")


def part_one(marked, boards):
    # Loop through the marked numbers and mark positions on board
    for mark in marked:
        for board in boards:
            for i in range(5):
                for j in range(5):
                    if board[i][j] == mark:
                        board[i][j] = "M"

            # Check if board is drawn
            drawn = check_draw( board )

            if drawn:
                score = calculate_score(mark, board)
                return score

    return 0


def check_draw(board):
    # First check the rows
    m_count_row = [0] * 5
    for row in range(5):
       for col in range(5):
            if board[row][col] == "M":
                m_count_row[row] += 1

    if 5 in m_count_row:
        return True

    # Then check the cols
    m_count_col = [0] * 5
    for col in range(5):
        for row in range(5):
            if board[row][col] == "M":
                m_count_col[col] += 1

    if 5 in m_count_col:
        return True

    return False


def calculate_score(mark, board):
    unmarked_sum = 0

    for row in range(5):
        for col in range(5):
            if board[row][col] != "M":
                unmarked_sum += int(board[row][col])

    return unmarked_sum * int(mark)


def generate_boards(boards_raw):
    grid_size = 5
    num_of_boards = int(len(boards_raw) / 25)
    counter = 0

    # Create boards
    boards = [[[0] * grid_size for _ in range( grid_size ) ] for _ in range ( num_of_boards )]

    # Input the raw data
    for board in boards:
        for i in range( grid_size ):
            for j in range( grid_size ):
                board[i][j] = boards_raw[counter]
                counter += 1

    return boards


def get_file():
    f = open("input.txt", "r")
    return f


def readFile():
    f = get_file()
    # First get the marked numbers
    marked_numbers = f.readline().strip().split(",")
    f.close()

    # Then get the boards
    f = get_file()
    boards = []

    for pos, line in enumerate(f):
        if pos != 0 and pos != 1:
            if len(line) != 1:
                split = line.strip().split(" ")
                for s in split:
                    if s != "":
                        boards.append(s)


    boards = generate_boards( boards )
    return marked_numbers, boards
    

if __name__ == "__main__":
    run_my_boy()
