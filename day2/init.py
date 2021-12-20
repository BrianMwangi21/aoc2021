def run_my_boy():
    commands = readFile()
    
    print(f"Part One : {part_one(commands)}")


def part_one(commands):
    h_pos, v_pos = 0, 0

    for command in commands:
        direction, offset = command.split(" ")
                
        if direction == "forward":
            h_pos += int(offset)
        elif direction == "down":
            v_pos += int(offset)
        elif direction == "up":
            v_pos -= int(offset)
        
    return h_pos * v_pos


def readFile():
    f = open("input.txt", "r")
    data = f.read().splitlines()
    return data
    

if __name__ == "__main__":
    run_my_boy()
