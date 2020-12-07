def get_input():
    coordinates = []
    while True:
        print("Enter the coordinates: ", end="")
        coordinates_str = input().split()

        try:
            coordinates = [int(x) for x in coordinates_str]
        except:
            print("[Error]: Only enter numeric digits.")
            continue
        if coordinates[0] < 1 or coordinates[0] > 3 or coordinates[1] < 1 or coordinates[1] > 3:
            print("[Error]: Only enter numerics in the inclusive range 1 to 3.")
            continue
        break
    return coordinates


def convert_input(a_coords):
    return [a_coords[0] - 1, 4 - a_coords[1] - 1]


def process_matrix(a_matrix, a_player_one):
    while True:
        coords = get_input()
        processed_coords = convert_input(coords)
        x = processed_coords[0]
        y = processed_coords[1]

        if a_matrix[y][x] != "_":
            print("This cell is occupied! Choose another one!")
            continue

        a_matrix[y][x] = "X" if a_player_one else "O"
        # print_matrix(a_matrix)
        return a_matrix


def get_init_matrix():
    return [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]


def print_matrix(a_matrix):
    print("---------")
    for row in a_matrix:
        print("|", end=" ")
        for element in row:
            print(element, end=" ")
        print("|")
    print("---------")


def get_filled_matrix(a_input):
    return [[a_input[0], a_input[1], a_input[2]],
            [a_input[3], a_input[4], a_input[5]],
            [a_input[6], a_input[7], a_input[8]]]


def get_game_state(a_matrix):
    x_total_counter = 0
    o_total_counter = 0
    x_has_three = False
    o_has_three = False
    has_empty = False

    # Horizontal checks
    for row in a_matrix:
        x_row_counter = 0
        o_row_counter = 0
        for element in row:
            if element == "_":
                has_empty = True
            elif element == "X":
                x_total_counter += 1
                x_row_counter += 1
            elif element == "O":
                o_total_counter += 1
                o_row_counter += 1

            if x_row_counter == 3:
                x_has_three = True
            if o_row_counter == 3:
                o_has_three = True

    # Vertical and Diagonal checks
    if a_matrix[0][0] == "X" and a_matrix[1][0] == "X" and a_matrix[2][0] == "X"\
            or a_matrix[0][1] == "X" and a_matrix[1][1] == "X" and a_matrix[2][1] == "X"\
            or a_matrix[0][2] == "X" and a_matrix[1][2] == "X" and a_matrix[2][2] == "X"\
            or a_matrix[0][0] == "X" and a_matrix[1][1] == "X" and a_matrix[2][2] == "X"\
            or a_matrix[0][2] == "X" and a_matrix[1][1] == "X" and a_matrix[2][0] == "X":
        x_has_three = True

    if a_matrix[0][0] == "O" and a_matrix[1][0] == "O" and a_matrix[2][0] == "O"\
            or a_matrix[0][1] == "O" and a_matrix[1][1] == "O" and a_matrix[2][1] == "O"\
            or a_matrix[0][2] == "O" and a_matrix[1][2] == "O" and a_matrix[2][2] == "O"\
            or a_matrix[0][0] == "O" and a_matrix[1][1] == "O" and a_matrix[2][2] == "O"\
            or a_matrix[0][2] == "O" and a_matrix[1][1] == "O" and a_matrix[2][0] == "O":
        o_has_three = True

    # Impossible checks
    if abs(x_total_counter - o_total_counter) >= 2\
            or x_has_three and o_has_three:
        print("Impossible")
        return False
    elif x_has_three:
        print("X wins")
        return False
    elif o_has_three:
        print("O wins")
        return False
    elif has_empty:
        # print("Game not finished")
        return True
    else:
        print("Draw")
        return False


matrix = get_init_matrix()
print_matrix(matrix)

is_running = True
is_player_one = True
while is_running:
    matrix = process_matrix(matrix, is_player_one)
    print_matrix(matrix)
    is_player_one = not is_player_one
    is_running = get_game_state(matrix)
