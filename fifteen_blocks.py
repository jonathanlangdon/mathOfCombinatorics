# Determine how many possible ways a man can walk a particular number of blocks to work (final_x blocks east & final_y blocks north)
# original problem: 7 east and 8 north

final_x = 7
final_y = 8
possibility_count = 0


def go_north(start_x, start_y):
    if start_y == final_y:
        return "stop", "stop"
    # print(start_x, start_y)
    return start_x, start_y + 1


def go_east(start_x, start_y):
    if start_x == final_x:
        return "stop", "stop"
    # print(start_x, start_y)
    return start_x + 1, start_y


def next_possible_combinations(start_x, start_y):
    if start_x == "stop":
        return
    if start_x == final_x and start_y == final_y:
        # print(start_x, start_y)
        global possibility_count
        # print("work reached")
        possibility_count += 1
        return
    next_x, next_y = go_north(start_x, start_y)
    next_possible_combinations(next_x, next_y)
    next_x, next_y = go_east(start_x, start_y)
    next_possible_combinations(next_x, next_y)


next_possible_combinations(0, 0)
print(possibility_count)
