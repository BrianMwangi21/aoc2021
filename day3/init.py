def run_my_boy():
    diagnostics = readFile()
    
    print(f"Part One : {part_one(diagnostics)}")


def part_one(diagnostics):
    gamma, epsilon = '', ''
    index_arrs = []
    
    for i in range( len(diagnostics[0]) ):
        index_arrs.append([])

    for diagnostic in diagnostics:
        split = list(diagnostic)
        for i in range(len(split)):
            index_arrs[i].append(split[i])
            
    # Get gamma and epsilon of each array
    for index_arr in index_arrs:
        gamma += get_gamma( index_arr )
        epsilon += get_epsilon( index_arr )

    # Convert to interger
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    power_consumption = gamma * epsilon

    print(f"Gamma: {gamma}, Epsilon: {epsilon} = Power Consumption {power_consumption}")

    return power_consumption

   
def get_gamma(arr):
    c_one, c_zero = 0, 0

    for i in arr:
        if i == '0':
            c_zero += 1
        elif i == '1':
            c_one += 1

    if c_one > c_zero:
        return "1"
    else:
        return "0"


def get_epsilon(arr):
    c_one, c_zero = 0, 0

    for i in arr:
        if i == '0':
            c_zero += 1
        elif i == '1':
            c_one += 1

    if c_one < c_zero:
        return "1"
    else:
        return "0"


def readFile():
    f = open("input.txt", "r")
    data = f.read().splitlines()
    return data
    

if __name__ == "__main__":
    run_my_boy()
