def rotate_card(bingo_card=[]):
    rotated_card = []
    for i in range(len(bingo_card[0])):
        line = []
        for j in range(len(bingo_card[i])):
            line.append(bingo_card[j][i])
        rotated_card.append(line)
    return rotated_card


def get_win(list_numbers=[], bingo_card=[]):
    win_index = -1
    win_score = 0
    rotated_card = rotate_card(bingo_card)
    win = False
    for number in list_numbers:
        for idx in range(len(bingo_card)):
            if bingo_card[idx].count(number):
                bingo_card[idx].pop(bingo_card[idx].index(number))
                if len(bingo_card[idx]) == 0:
                    win = True
                    for i in range(len(bingo_card)):
                        win_score += sum(bingo_card[i])
                    break
            if rotated_card[idx].count(number):
                rotated_card[idx].pop(rotated_card[idx].index(number))
                if len(rotated_card[idx]) == 0:
                    win = True
                    for i in range(len(rotated_card)):
                        win_score += sum(rotated_card[i])
                    break
        if win:
            win_index = list_numbers.index(number)
            win_number = number
            break
    return win_index, win_number, win_score


def main():
    with open("input.txt") as f:
        list_numbers = []
        bingo_card = []
        min_win_index = max_win_index = 0
        min_win_score = max_win_score = 0
        min_win_number = max_win_number = 0

        list_numbers = list(map(int, f.readline().split(',')))
        min_win_index = len(list_numbers)
        while True:
            bingo_card = []
            f.readline()
            for _ in range(0, 5):
                bingo_card.append(list(map(int, f.readline().split())))
            if len(bingo_card[0]) == 5:
                cur_win_index, cur_win_number, cur_win_score = get_win(
                    list_numbers, bingo_card)
                if cur_win_index < min_win_index:
                    min_win_index, min_win_score, min_win_number = cur_win_index, cur_win_score, cur_win_number
                if cur_win_index > max_win_index:
                    max_win_index, max_win_score, max_win_number = cur_win_index, cur_win_score, cur_win_number
            else:
                break

        print(
            f'FirstWin. Index: {min_win_index}, Number: {min_win_number}, Score: {min_win_score}, Result: {min_win_number * min_win_score}'
        )
        print(
            f'LastWin. Index: {max_win_index}, Number: {max_win_number}, Score: {max_win_score}, Result: {max_win_number * max_win_score}'
        )


if __name__ == "__main__":
    main()
