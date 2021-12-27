def run_my_boy():
    crab_data, min_pos, max_pos = readFile()

    print(f"Part One : {part_one(crab_data, min_pos, max_pos)}")

def part_one(crab_data, min_pos, max_pos):
    sum_of_fuels = []
    sum_of_fuels_only = []

    for x in range(min_pos, max_pos + 1):
        sum_of_fuel = 0

        for location in crab_data:
            sum_of_fuel += abs( x - location )

        sum_of_fuels.append({
            "sum" : sum_of_fuel,
            "pos" : x,
            "desc": f"Sum of fuel to location {x} is {sum_of_fuel}"
        })
        sum_of_fuels_only.append( sum_of_fuel )
    
    
    return min(sum_of_fuels_only)

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
