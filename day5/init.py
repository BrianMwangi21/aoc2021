def run_my_boy():
    coordinates, size_x, size_y = readFile()
    
    print(f"Part One : {part_one(coordinates, size_x, size_y)}")
    print(f"Part Two : {part_two(coordinates, size_x, size_y)}")


def part_one(coordinates, size_x, size_y):
    board = [[0] * (size_y) for _ in range( size_x )] 

    # Loop through the coordinates
    for coordinate in coordinates:
        coord_one = coordinate[0].split(",")
        coord_two = coordinate[1].split(",")

        # Check for only horizontal / vertical lines
        if coord_one[0] == coord_two[0]:
            # Get start point and end point on Y axis
            x = int(coord_one[0])
            start_y = min( int(coord_one[1]) , int(coord_two[1]) )
            end_y = max( int(coord_one[1]) , int(coord_two[1]) )

            # Then loop appending the value in the row
            for col in range(size_y):
                if col >= start_y and col <= end_y:
                    board[x][col] += 1
        elif coord_one[1] == coord_two[1]:
            # Get start point and end point on X axis
            y = int(coord_one[1])
            start_x = min( int(coord_one[0]) , int(coord_two[0]) )
            end_x = max( int(coord_one[0]) , int(coord_two[0]) )

            # Then loop appending the value in the row
            for row in range(size_x):
                if row >= start_x and row <= end_x:
                    board[row][y] += 1

    # Now count occurences of > 2
    overlap_count = 0
    for row in range(size_x):
        for col in range(size_y):
            if board[row][col] >= 2:
                overlap_count += 1
    
    return overlap_count

def part_two(coordinates, size_x, size_y):
    board = [[0] * (size_y) for _ in range( size_x )] 

    # Loop through the coordinates
    for coordinate in coordinates:
        coord_one = coordinate[0].split(",")
        coord_two = coordinate[1].split(",")
        
        # Check for only horizontal / vertical lines
        if coord_one[0] == coord_two[0]:
            # Get start point and end point on Y axis
            x = int(coord_one[0])
            start_y = min( int(coord_one[1]) , int(coord_two[1]) )
            end_y = max( int(coord_one[1]) , int(coord_two[1]) )

            # Then loop appending the value in the row
            for col in range(size_y):
                if col >= start_y and col <= end_y:
                    board[x][col] += 1
        elif coord_one[1] == coord_two[1]:
            # Get start point and end point on X axis
            y = int(coord_one[1])
            start_x = min( int(coord_one[0]) , int(coord_two[0]) )
            end_x = max( int(coord_one[0]) , int(coord_two[0]) )

            # Then loop appending the value in the row
            for row in range(size_x):
                if row >= start_x and row <= end_x:
                    board[row][y] += 1
        else:
            x1, x2 = int(coord_one[0]), int(coord_two[0])
            y1, y2 = int(coord_one[1]), int(coord_two[1])

            # Check for absolute difference
            x_diff= abs( x1 - x2 )
            y_diff = abs( y1 - y2 )

            if x_diff == y_diff:
                x_step = 1 if x1 < x2 else -1
                y_step = 1 if y1 < y2 else -1
                t_steps = max( x_diff, y_diff )

                for _ in range(t_steps + 1):
                    board[x1][y1] += 1
                    x1 += x_step
                    y1 += y_step
    
    # Now count occurences of > 2
    overlap_count = 0
    for row in range(size_x):
        for col in range(size_y):
            if board[row][col] >= 2:
                overlap_count += 1
    
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


    return coordinates, ( size_x + 1 ) , ( size_y + 1 )

if __name__ == "__main__":
    run_my_boy()
