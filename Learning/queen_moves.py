number = input()
charm = ["a", "b", "c", "d", "e", "f", "g", "h"]

matrix_cube = [["."] * 8 for _ in range(8)]
start_string = 8 - int(number[1])
start_column = charm.index(number[0])

if start_string > start_column:
    max_top_left = start_column
else:
    max_top_left = start_string

if start_string > 7 - start_column:
    max_top_right = 7 - start_column
else:
    max_top_right = start_string

if 7 - start_string > start_column:
    max_bot_left = start_column
else:
    max_bot_left = 7 - start_column

if 7 - start_string > 7 - start_column:
    max_bot_right = start_column
else:
    max_bot_right = 7 - start_column


for i in range(8):
    for j in range(8):
        if i == start_string or j == start_column:
            matrix_cube[i][j] = "*"

        if i == start_string - max_top_left and j == start_column - max_top_left:
            matrix_cube[i][j] = "*"
            max_top_left -= 1
        if i == start_string - max_top_right and j == start_column + max_top_right:
            matrix_cube[i][j] = "*"
            max_top_right -= 1

        if i == start_string + max_bot_left and j == start_column - max_bot_left:
            matrix_cube[i][j] = "*"
            max_bot_left -= 1
        if i == start_string + max_bot_right and j == start_column + max_bot_right:
            matrix_cube[i][j] = "*"
            max_bot_right -= 1

matrix_cube[start_string][start_column] = "Q"

for row in matrix_cube:
    print(*row)
