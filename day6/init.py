def run_my_boy():
    data = readFile()

    print(f"Part One: {part_one(data)}")

def part_one(data):
    total_days = 80

    # Now loop through the number of days 
    for _ in range( total_days ):
        # Now loop through the data doing what is needed
        for timer in range( len(data) ):
            data[timer] -= 1

            if data[timer] < 0:
                data[timer] = 6
                data.append(8)

    # Get the number of total fish
    total_fish = len(data)
    return total_fish
    
def readFile():
    with open("input.txt") as f:
        data = f.readline().strip()
        data = data.split(",")
        data = [ int(x) for x in data ]    


    return data


if __name__ == "__main__":
    run_my_boy()
