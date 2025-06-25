
def matrix(a):
    m = []
    while len(m) != a:
        row = input().split()
        if not row:
            continue
        else:
            int_row = []
            for digit in row:
                int_row.append(int(digit))
            m.append(int_row)
    return m

matrix_cube = [["."] * number for _ in range(number)]

for row in matrix_cube:
    print(*(str(elem).ljust(3) for elem in row))


#'1', '2', '3', '4', '5', '6', '7', '8', '9', '10' 
#'10', '9', '8', '7', '6', '5', '4', '3', '2', '1'

#['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] 
#['10', '9', '8', '7', '6', '5', '4', '3', '2', '1']


# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]