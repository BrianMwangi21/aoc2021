def run_my_boy():
    bingo_marked, bingo_boards = readFile()
    
    print(f"Part One : Score is {part_one(bingo_marked, bingo_boards)}")
    print(f"Part Two : Score is {part_two(bingo_marked, bingo_boards)}")


def part_one(marked, boards):
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


def part_two(marked, boards):
    drawn_boards_count = [0] * len(boards)

    for mark in marked:
        for pos, board in enumerate(boards):
            for i in range(5):
                for j in range(5):
                    if board[i][j] == mark:
                        board[i][j] = "M"

            # Check if board is drawn
            drawn = check_draw( board )

            if drawn:
                drawn_boards_count[pos] = 1

            # Then check if 1 count is one
            if drawn_boards_count.count(0) < 1:
                score = calculate_score(mark, board)
                return score
            
    return 0


def check_draw(board):
    m_count_row = [0] * 5
    for row in range(5):
       for col in range(5):
            if board[row][col] == "M":
                m_count_row[row] += 1

    if 5 in m_count_row:
        return True

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

    boards = [[[0] * grid_size for _ in range( grid_size ) ] for _ in range ( num_of_boards )]

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
    marked_numbers = f.readline().strip().split(",")
    f.close()

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
