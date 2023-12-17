from part1 import read_csv, hash_value

def get_box_number(label):
    return hash_value(label)

def process_labels(all_labels):
    boxes = {x: {} for x in range(256)}
    for label in all_labels:
        if '-' in label:
            symbol_pos = label.find('-')
            short_label = label[:symbol_pos]
            box_number = get_box_number(short_label)
            if short_label in boxes[box_number].keys():
                del boxes[box_number][short_label]
        elif '=' in label:
            symbol_pos = label.find('=')
            short_label = label[:symbol_pos]
            box_number = get_box_number(short_label)
            lens = label[(symbol_pos + 1):]
            boxes[box_number][short_label] = lens
        else:
            raise Exception
        
    return boxes

def calculate_focusing_power(boxes):
    total = 0
    for box_number in boxes:
        for index, (short_label, lens) in enumerate(boxes[box_number].items()):
            print(f'{short_label} box {box_number} {(box_number + 1) * (index + 1) * int(lens)}')
            total = total + (box_number + 1) * (index + 1) * int(lens)
    return total

if __name__ == '__main__':
    all_labels = read_csv('day15/input.csv')
    # all_labels = ['rn=1','cm-','qp=3','cm=2','qp-','pc=4','ot=9','ab=5','pc-','pc=6','ot=7']
    boxes = process_labels(all_labels)
    focusing_power = calculate_focusing_power(boxes)
    print(f'focusing_power: {focusing_power}')
