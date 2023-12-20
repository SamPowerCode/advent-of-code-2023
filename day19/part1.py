def read_input(file_location):
    with open(file_location) as file:
        file_content = file.read().strip().split("\n")

    return file_content

def convert_workflow_to_dict(dicty_str):
    dicty_str_list = dicty_str.split(',')
    new_dict = {}
    for dict_item in dicty_str_list:
        key, value = dict_item.split('=')
        new_dict[key] = int(value)
    
    return new_dict

def convert_rules_to_dict(rules):
    rules_dict = {}
    for rule in rules:
        first_curly_brace = rule.find('{')
        rules_dict[rule[:first_curly_brace]] = {}
        temp_value_str = rule[first_curly_brace + 1:-1]        
        temp_value_list = temp_value_str.split(',')
        temp_value_list[-1] = f'FINAL:{temp_value_list[-1]}'
        for dict_item in temp_value_list:
            key, value = dict_item.split(':')
            rules_dict[rule[:first_curly_brace]][key] = value

    return rules_dict

def parse_data(file_content):
    workflows = []
    temp_rules = []
    parse_rules = True
    for line in file_content:
        if parse_rules:
            temp_rules.append(line)
        else:
            workflows.append(line)
        if line == '':
            parse_rules = False
    
    rules = convert_rules_to_dict(temp_rules)
    
    return rules, workflows

def process_workflows(rules, workflows):
    result = 0
    
    for workflow_entry in workflows:
        rules_complete = False
        current_workflow = convert_workflow_to_dict(workflow_entry[1:-1])
        x, m, a, s = current_workflow.values()
        current_rule = 'in'
        while rules_complete == False:
            for key, value in rules[current_rule].items():
                if key == 'FINAL':
                    if value == 'A':
                        result = result + sum(current_workflow.values())
                        rules_complete = True
                        break
                    elif value == 'R':
                        rules_complete = True
                        break
                    else:
                        current_rule = value
                elif eval(key):                    
                    if value == 'A':
                        result = result + sum(current_workflow.values())
                        rules_complete = True
                        break
                    elif value == 'R':
                        rules_complete = True
                        break
                    else:
                        current_rule = value
                        break

    return result

if __name__ == '__main__':
    file_location = 'day19/input'
    file_content = read_input(file_location)
    rules, workflows = parse_data(file_content)
    result = process_workflows(rules, workflows)
    print('EOF')
