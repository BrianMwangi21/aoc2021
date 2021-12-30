def run_my_boy():
    heightmap, width, height = readFile()

    print(f"Part One : {part_one(heightmap, width, height)}")
    # print(f"Part Two : {part_two()}")

def part_one(heightmap, width, height):
    lowest_points = []

    # Loop through the boards
    for i in range(height):
        for j in range(width):
            _current = heightmap[i][j]
            _around = [_current]
            # Check around, if possible
            
            # Check up if not first row
            if i != 0:
                _around.append( heightmap[i-1][j] )

            # Check down if now last row
            if i != height-1:
                _around.append( heightmap[i+1][j] )

            # Check left if not first col
            if j != 0:
                _around.append( heightmap[i][j-1] )

            # Check right ig not last col
            if j != width-1:
                _around.append( heightmap[i][j+1] )


            # Now compare all the values in around
            if min(_around) == _current and _around.count(_current) == 1:
                lowest_points.append([i,j])
    
    risk_level = 0
    for i in lowest_points:
        risk_level += heightmap[i[0]][i[1]] + 1 

    return risk_level


def part_two():
    pass


def readFile():
    data = []
    with open("input.txt") as f:
        raw_data = f.read().splitlines()
        for i in raw_data:
            data.append(list(map(int, list(i))))

    width = len(data[0])
    height = len(data)

    return data, width, height

if __name__ == "__main__":
    run_my_boy()
