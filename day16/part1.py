def create_2d_matrix(txt):
    matrix = []
    with open(txt, 'r') as file:
        all_lines = file.readlines()
        for line in all_lines:
            line = line.replace('\n', '')
            matrix.append(list(line))

    return matrix

def is_valid(matrix, row, column):
    if row < 0 or row > (len(matrix[0]) - 1) or column < 0 or column > (len(matrix) -1):
        return False
    else:
        return True

def send_beam(matrix, current_direction='right', row=0, column=0):
    max_height = len(matrix)
    max_width = len(matrix[0])
    beam = 1
    direction = {
        'right': (+1, 0),
        'left': (-1, 0),
        'up': (0,-1),
        'down': (0, +1)
    }
    direction_text = {
        'right': '>',
        'left': '<',
        'up': '^',
        'down': 'v'
    }

    while beam > 0:
        print(f'row, col = [{row}, {column}] - {matrix[row][column]}')
        print()
        if matrix[row][column] == '.':

            matrix[row][column] = direction_text[current_direction]
            column = column + 1
        elif matrix[row][column] == '/':
            pass
        elif matrix[row][column] == '\\':
            pass
        elif matrix[row][column] == '|':
            # current_direction = 'up'
            # row = row + 1
            if is_valid(matrix, row - 1, column):
                send_beam(matrix, current_direction, row, column)
            # current_direction = 'down'
            row = row + 2
            current_direction = 'down'
            
        elif matrix[row][column] == '-':
            pass

        print_matrix(matrix)
        print()
        
        # start in top left corner
        # what is first cell
        # move in that direction
        # beam = 0
        

def print_matrix(matrix):
    for line in matrix:
        print("".join(line))

if __name__ == '__main__':
    # matrix = create_2d_matrix('day16/input.txt')
    matrix = create_2d_matrix('day16/input_test.txt')
    # is_valid(matrix, 0, 0)
    print_matrix(matrix)
    print()
    send_beam(matrix, current_direction = 'right', row = 0, column = 0)
    print_matrix(matrix)
    print()
    print("TEST")
