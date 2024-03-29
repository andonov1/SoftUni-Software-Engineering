class InvalidColumnError(Exception):
    pass


class FullColumnError(Exception):
    pass


def print_matrix(ma):
    # print matrix
    for el in ma:
        print(el)


def validate_column_choice(selected_column_num, max_column_index):
    # verify player choice of column number of is correct
    if not (0 <= selected_column_num <= max_column_index):
        raise InvalidColumnError


def place_player_choice(ma, selected_column_index, player_num):
    # Place player marker on the spot.
    # Check if the column  is full if so - throw error.

    rows_count = len(ma)
    for row_index in range(rows_count - 1, -1, -1):
        current_element = ma[row_index][selected_column_index]
        if current_element == 0:
            ma[row_index][selected_column_index] = player_num
            return row_index, selected_column_index
    raise FullColumnError


def is_player_num(ma, row, col, player_num):
    if col < 0 or row < 0:
        return False
    try:
        if ma[row][col] == player_num:
            return True
    except IndexError:
        return False
    return False


def is_horizontal(ma, row, col, player_num, slots_count):
    right = []
    for index in range(slots_count):
        if is_player_num(ma, row, col + index, player_num):
            right.append(True)
        else:
            break
    left = []
    for index in range(slots_count):
        if is_player_num(ma, row, col - index, player_num):
            left.append(True)
        else:
            break
    # count_right = [ for index in range(slots_count) if ].count(True)
    # count_left = [is_player_num(ma, row, col-index, player_num) for index in range(slots_count)].count(True)
    # It should be strict '>' because we are counting the current element as well
    return len(left + right) > slots_count


def is_right_diagonal(ma, row, col, player_num, slots_count):
    """
    We check for both (up right and left down) so we can look for the same problem -
    adding element which is not only to one side with 4 but for both
    """
    top_right = []
    for index in range(slots_count):
        if is_player_num(ma, row - index, col + index, player_num):
            top_right.append(True)
        else:
            break
    bottom_left = []
    for index in range(slots_count):
        if is_player_num(ma, row + index, col - index, player_num):
            top_right.append(True)
        else:
            break
    return (len(top_right) + len(bottom_left)) > 4


def is_left_diagonal(ma, row, col, player_num, slots_count):
    """
    We check for both (up left and right down) so we can look for the same problem -
    adding element which is not only to one side with 4 but for both
    """
    top_left = []
    for index in range(slots_count):
        if is_player_num(ma, row - index, col - index, player_num):
            top_left.append(True)
        else:
            break
    bottom_right = []
    for index in range(slots_count):
        if is_player_num(ma, row + index, col + index, player_num):
            bottom_right.append(True)
        else:
            break
    return (len(top_left) + len(bottom_right)) > 4


def is_winner(ma, row, col, player_num, slots_count=4):
    """
    We check for horizontal (both sides)
    Only down (because we fill the matrix from bottom to top).
    Check for right and left diagonal
    """
    is_down = all([is_player_num(ma, row + index, col, player_num) for index in range(slots_count)])
    if any(
            [
                is_horizontal(ma, row, col, player_num, slots_count),
                is_right_diagonal(ma, row, col, player_num, slots_count),
                is_left_diagonal(ma, row, col, player_num, slots_count),
                is_down,
            ]
    ):
        return True
    return False


rows_count = 6
cols_count = 7

# create matrix
matrix = [[0 for _ in range(cols_count)] for row_num in range(rows_count)]
# Print initial board
print_matrix(matrix)

player_num = 1
while True:
    # Decide correct player num (only 1 and 2 are possible - only 2 players)
    player_num = 2 if player_num % 2 == 0 else 1
    try:
        # Read column choice from input
        colum_num = int(input(f"Player {player_num}, please choose a column: ")) - 1
        validate_column_choice(colum_num, cols_count - 1)
        row, col = place_player_choice(matrix, colum_num, player_num)
        if is_winner(matrix, row, col, player_num):
            print_matrix(matrix)
            print(f"The winner is player {player_num}")
            break
        print_matrix(matrix)
    except InvalidColumnError:
        # Not in range of the game 1-7
        print(f"This column is not valid. Please select a "
              f"number between {1} and {cols_count}")
        continue
    except ValueError:
        # Not a valid number
        print("Please select a valid digit!")
        continue
    except FullColumnError:
        # This is already a full column
        print(f"This column is already full! Please, select other column number!")
        continue

    # Only if the turn was successful, we go to the next player
    player_num += 1
