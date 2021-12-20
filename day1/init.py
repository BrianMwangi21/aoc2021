def run_my_boy():
    # Get data from the file 
    depths = readFile()

    # Print the depths like in the example
    prev_depth = depths[0]
    count_inc = 0
    print(f"{prev_depth} - (N/A - no previous measurement)")

    for depth in depths[1:]:
        if depth > prev_depth:
            print(f"{depth} (increased)")
            count_inc += 1
        else:
            print(f"{depth} (decreased)")

        prev_depth = depth

    print(f"The total count increase is : {count_inc}")


def readFile():
    f = open("input.txt", "r")
    data = f.read().splitlines()
    return data 
    

if __name__ == "__main__":
    run_my_boy()
