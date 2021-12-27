def run_my_boy():
    crab_data, min_pos, max_pos = readFile()

    print(f"Part One : {part_one(crab_data, min_pos, max_pos)}")
    print(f"Part Two : {part_two(crab_data, min_pos, max_pos)}")

def part_one(crab_data, min_pos, max_pos):
    sum_of_fuels = []

    for x in range(min_pos, max_pos + 1):
        sum_of_fuel = 0

        for location in crab_data:
            sum_of_fuel += abs( x - location )

        sum_of_fuels.append( sum_of_fuel )
    
    
    return min(sum_of_fuels)

def part_two(crab_data, min_pos, max_pos):
    sum_of_fuels = []

    for x in range(min_pos, max_pos + 1):
        sum_of_fuel = 0

        for location in crab_data:
            diff = abs( x - location )
            sum_of_fuel += diff * ( diff + 1 ) // 2

        sum_of_fuels.append( sum_of_fuel )
    
    
    return min(sum_of_fuels)

def readFile():
    with open("input.txt") as f:
        data = f.readline().strip()
        data = data.split(",")
        data = [int(x) for x in data]
        min_pos = min(data)
        max_pos = max(data)

    return data, min_pos, max_pos

if __name__ == "__main__":
    run_my_boy()
