import itertools

def run_my_boy():
    signals = readFile()

    # print(f"Part One : {part_one(signals)}")
    print(f"Part Two : {part_two()}")

def part_one(signals):
    good = [2, 4, 3, 7]

    result = 0
    for output in signals:
        for digit in output:
            if len(digit) in good:
                result += 1

    return result 

def part_two():

    with open("input.txt") as fin:
        raw_data = fin.read().strip().split("\n")
        data = [
            [
                sorted(line[:line.index("|") - 1].split(" ")),
                line[line.index("|") + 2:].split(" ")
            ] for line in raw_data
        ]

    digits_key = [
        "abcefg",
        "cf",
        "acdeg",
        "acdfg",
        "bcdf",
        "abdfg",
        "abdefg",
        "acf",
        "abcdefg",
        "abcdfg"
    ]
    digits = sorted(digits_key)
    digits = tuple(digits)

    result = 0

    for line in data:
        clues = line[0]
        assert len(clues) == 10

        num = line[1]

        # Try all possible substitutions
        for sigma in itertools.permutations("abcdefg"):
            # Reencode digits
            key = {}
            for c in "abcdefg":
                key[c] = sigma["abcdefg".index(c)]

            new_clues = [] * 10
            for clue in clues:
                x = ""
                for char in clue:
                    x += key[char]
                x = "".join(sorted(x))
                new_clues.append(x)

            new_clues.sort()

            if tuple(new_clues) == digits:
                # Get the number it's supposed to be
                n = []
                for d in num:
                    x = ""
                    for char in d:
                        x += key[char]
                    x = "".join(sorted(x))
                    n.append(digits_key.index(x))

                result += int("".join([str(i) for i in n]))

                break

    return result

def readFile():
    with open("input.txt") as fin:
        raw_data = fin.read().strip().split("\n")
        data = [line[line.index("|") + 2:].split(" ") for line in raw_data]

    return data

if __name__ == "__main__":
    run_my_boy()
