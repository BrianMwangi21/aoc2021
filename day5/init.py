def run_my_boy():
    coordinates, size_x, size_y = readFile()
    
    print(f"Part One : {part_one(coordinates, size_x, size_y)}")


def part_one(coordinates, size_x, size_y):
    board = [[0] * (size_x) for _ in range( size_y )] 

    # Loop through the coordinates
    for coordinate in coordinates:
        coord_one = coordinate[0].split(",")
        coord_two = coordinate[1].split(",")
        found_x_y = False

        # Check for only horizontal / vertical lines
        if coord_one[0] == coord_two[0]:
            found_x_y = True
            # Get start point and end point on Y axis
            x = int(coord_one[0])
            start_y = min( int(coord_one[1]) , int(coord_two[1]) )
            end_y = max( int(coord_one[1]) , int(coord_two[1]) )

            # Then loop appending the value in the row
            for col in range(size_y):
                if col >= start_y and col <= end_y:
                    board[col][x] += 1

        elif coord_one[1] == coord_two[1]:
            found_x_y = True
            # Get start point and end point on X axis
            y = int(coord_one[1])
            start_x = min( int(coord_one[0]) , int(coord_two[0]) )
            end_x = max( int(coord_one[0]) , int(coord_two[0]) )

            # Then loop appending the value in the row
            for row in range(size_x):
                if row >= start_x and row <= end_x:
                    board[y][row] += 1
    
    # Now count occurences of > 2
    overlap_count = 0
    for row in range(size_y):
        for col in range(size_x):
            if board[row][col] >= 2:
                overlap_count += 1
    
    print(f"For all coordinates, 2 or more lines overlap {overlap_count} times")
    return overlap_count

def print_board(board):
    for x in board:
        print(x)
    print("\n")

def readFile():
    f = open("input.txt")
    data = f.read().splitlines()
    coordinates = []
    size_x, size_y = 0, 0

    for x in data:
        pair = x.split(" -> ")

        # First, append pair
        coordinates.append(pair)

        # Get the highest x and highest y to form the size of board
        coord_one = pair[0].split(",")
        coord_two = pair[1].split(",")
        size_x = max( size_x, int(coord_one[0]) )
        size_x = max( size_x, int(coord_two[0]) )
        size_y = max( size_y, int(coord_one[1]) )
        size_y = max( size_y, int(coord_two[1]) )

    print(f"After reading data, the board size is {size_x} by {size_y}")

    return coordinates, ( size_x + 1 ) , ( size_y + 1 )

if __name__ == "__main__":
    run_my_boy()
