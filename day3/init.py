def run_my_boy():
    diagnostics = readFile()
    
    print(f"Part One : {part_one(diagnostics)}")
    print(f"Part Two : {part_two(diagnostics)}")


def get_index_arrs(diagnostics):
    index_arrs = []
    
    for i in range( len(diagnostics[0]) ):
        index_arrs.append([])

    for diagnostic in diagnostics:
        split = list(diagnostic)
        for i in range(len(split)):
            index_arrs[i].append(split[i])
    
    return index_arrs


def part_one(diagnostics):
    gamma, epsilon = '', ''
    index_arrs = get_index_arrs(diagnostics)

    # Get gamma and epsilon of each array
    for index_arr in index_arrs:
        gamma += get_gamma( index_arr )
        epsilon += get_epsilon( index_arr )

    # Convert to interger
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    power_consumption = gamma * epsilon

    return power_consumption


def part_two(diagnostics):
    oxygen_rating, c02_scrubber = '', ''
    index_arrs = get_index_arrs(diagnostics)
            
    # Get o2 rating and c02 scrubber
    oxygen_rating = get_oxygen_rating(diagnostics, index_arrs, 0)
    c02_scrubber = get_c02_rating(diagnostics, index_arrs, 0)

    # Convert to interger
    oxygen_rating = int(oxygen_rating, 2)
    c02_scrubber = int(c02_scrubber, 2)
    life_support_rating = oxygen_rating * c02_scrubber

    return life_support_rating

   
def get_gamma(arr):
    c_one, c_zero = 0, 0

    for i in arr:
        if i == '0':
            c_zero += 1
        elif i == '1':
            c_one += 1

    if c_one >= c_zero:
        return "1"
    else:
        return "0"


def get_oxygen_rating(diagnostics, index_arrs, index):
    if index < len(index_arrs):
        gamma = get_gamma( index_arrs[index] ) 

        # Now check if matches gamma
        new_diagnostics = []
        for i in range( len(diagnostics) ):
            if diagnostics[i][index] == gamma:
                new_diagnostics.append( diagnostics[i] ) 

        index_arrs = get_index_arrs(new_diagnostics)

        if len(new_diagnostics) == 1:
            return new_diagnostics[0]
        else:
            return get_oxygen_rating( new_diagnostics, index_arrs, index + 1)
    else:
        return diagnostics[0]


def get_epsilon(arr):
    c_one, c_zero = 0, 0

    for i in arr:
        if i == '0':
            c_zero += 1
        elif i == '1':
            c_one += 1

    if c_zero <= c_one:
        return "0"
    else:
        return "1"


def get_c02_rating(diagnostics, index_arrs, index):
    if index < len(index_arrs):
        epsilon = get_epsilon( index_arrs[index] ) 

        # Now check if matches gamma
        new_diagnostics = []
        for i in range( len(diagnostics) ):
            if diagnostics[i][index] == epsilon:
                new_diagnostics.append( diagnostics[i] ) 
        
        index_arrs = get_index_arrs(new_diagnostics)

        if len(new_diagnostics) == 1:
            return new_diagnostics[0]
        else:
            return get_c02_rating( new_diagnostics, index_arrs, index + 1)
    else:
        return diagnostics[0]


def readFile():
    f = open("input.txt", "r")
    data = f.read().splitlines()
    return data
    

if __name__ == "__main__":
    run_my_boy()
