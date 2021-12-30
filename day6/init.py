from collections import defaultdict

def run_my_boy():
    data = readFile()

    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")

def part_one(data):
    total_days = 80

    # Now loop through the number of days 
    for _ in range( total_days ):
        # Now loop through the data doing what is needed
        for timer in range( len(data) ):
            if data[timer] == 0:
                data[timer] = 6
                data.append(8)
            else:
                data[timer] -= 1

    # Get the number of total fish
    total_fish = len(data)
    return total_fish

 
def part_two(data):
    total_days = 256
    freq = defaultdict(int)
    for i in data:
        freq[i] += 1

    for _ in range(total_days):
        # New dict to store frequencies
        new_freq = defaultdict(int)

        for key in freq:
            if key == 0:
                new_freq[6] += freq[key]
                new_freq[8] = freq[key]
            else:
                new_freq[key - 1] += freq[key]

        freq = new_freq

    total_fish = 0
    for key in freq:
        total_fish += freq[key]

    return total_fish
       
def readFile():
    with open("input.txt") as f:
        data = f.readline().strip()
        data = data.split(",")
        data = [ int(x) for x in data ]    


    return data

if __name__ == "__main__":
    run_my_boy()
