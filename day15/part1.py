def read_csv(csv):
    sequence_list = []
    with open(csv, 'r') as file:
        csv_content = file.read().replace('\n', '')
        sequence_list = csv_content.split(',')

    return sequence_list

def hash_value(sequence):
    current_value = 0
    for char in sequence:
        current_value = current_value + ord(char)
        current_value = current_value * 17
        current_value = current_value % 256

    return current_value

if __name__ == '__main__':
    initialization_sequence = read_csv('day15/input.csv')
    total = 0
    for sequence in initialization_sequence:
        result = hash_value(sequence)
        total = total + result

    print(total)