# SEEDS_DICT = []
GROW_DATA = []

def read_input(file_location):
    with open(file_location) as file:
        file_content = file.read().strip().split("\n")

    return file_content

def get_seeds(first_line):
    return list(map(int, first_line.split(" ")[1:]))

def populate_grow_data(file_content):
    global GROW_DATA
    number_block = False
    sections = ['seed-to-soil map:',
                'soil-to-fertilizer map:',
                'fertilizer-to-water map:',
                'water-to-light map:',
                'light-to-temperature map:',
                'temperature-to-humidity map:',
                'humidity-to-location map:']
    for line in file_content[1:]:
        if line == '':
            number_block = False
        if line in sections:
            global GROW_DATA
            GROW_DATA.append([])
            number_block = True 
        elif number_block:
            data = list(map(int, line.split(" ")))
            GROW_DATA[-1].append(data)
            print('populate_grow_data TEST')
            # destination, source, total_range = data

def calculate_locations(seeds):
    for data in GROW_DATA:
        updated_indexes = []
        for line in data:
            # pass
            destination, source, total_range = line
            
            for index, seed in enumerate(seeds):
                # pass
                if seed >= source and seed < (source + (total_range)) and index not in updated_indexes:
                    seeds[index] = seed - source + destination
                    updated_indexes.append(index)
                    # test = difference + destination
                    print('calculate_locations TEST')
    
    return seeds

# def calculate_locations(seeds):
#     # for seed in seeds:
    
#     for data in GROW_DATA:
#         section = {}
#         for info in data:
#             destination, source, total_range = info
#             for x in range(total_range):
#                  section[source + x] = destination + x
#         # seed_data = []
#         for index, x in enumerate(seeds):
#             if x in section.keys():
#                 seeds[index] = section[x]
#         print('calculate_locations TEST')

#     return seeds




if __name__ == '__main__':
    file_location = 'day05/input'
    file_content = read_input(file_location)
    first_line = file_content[0]
    seeds = get_seeds(first_line)
    populate_grow_data(file_content)
    locations = calculate_locations(seeds)
    print(f'min location: {min(locations)}')
    print('EOF')


# SEEDS = []
# SEED_TO_SOIL_MAP = {}
# SOIL_TO_FERTILIZER_MAP = {}
# FERTILIZER_TO_WATER_MAP = {}
# WATER_TO_LIGHT_MAP = {}
# LIGHT_TO_TEMP_MAP = {}
# TEMP_TO_HUMIDITY_MAP = {}
# HUMIDITY_TO_LOCATION_MAP = {}

# def process_grow_data(grow_data):
#     global SEED_TO_SOIL_MAP 
#     global SOIL_TO_FERTILIZER_MAP 
#     global FERTILIZER_TO_WATER_MAP 
#     global WATER_TO_LIGHT_MAP 
#     global LIGHT_TO_TEMP_MAP 
#     global TEMP_TO_HUMIDITY_MAP 
#     global HUMIDITY_TO_LOCATION_MAP
#     max_number = 0
#     section_map = {
#         'seed-to-soil map:': SEED_TO_SOIL_MAP,
#         'soil-to-fertilizer map:': SOIL_TO_FERTILIZER_MAP,
#         'fertilizer-to-water map:': FERTILIZER_TO_WATER_MAP, 
#         'water-to-light map:': WATER_TO_LIGHT_MAP, 
#         'light-to-temperature map:': LIGHT_TO_TEMP_MAP,
#         'temperature-to-humidity map:': TEMP_TO_HUMIDITY_MAP,
#         'humidity-to-location map:': HUMIDITY_TO_LOCATION_MAP
#         }
#     for section in grow_data:
#         for data in grow_data[section]:
#             destination, source, total_range = data
#             for x in range(total_range):
#                 section_map[section][source + x] = destination + x
#             # print('TEST')
#         if max_number < max(section_map[section]):
#             max_number = max(section_map[section])
#         for y in range(max_number):
#             if y not in section_map[section].keys():
#                 section_map[section][y] = y

# def extract_data(file_content):
#     sections = ['seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:', 'water-to-light map:', 
#                 'light-to-temperature map:', 'temperature-to-humidity map:', 'humidity-to-location map:']
    
#     data = {section: [] for section in sections}
#     current_section = None

#     for line in file_content:
#         line = line.replace('\n', '')
#         if line in sections:
#             current_section = line
#         elif current_section:
#             try:
#                 numbers = [int(n) for n in line.split()]
#                 if numbers:
#                     data[current_section].append(numbers)
#             except ValueError:
#                 current_section = None

#     return data

# def read_input(file_location):
#     file_content = []
#     with open(file_location, 'r') as file:
#         file_content = file.readlines()
#         for line in file_content:
#             if line.find('seeds: ') != -1:
#                 # print('Line:', line)
#                 line = line.strip().replace('seeds: ', '')
#                 global SEEDS
#                 SEEDS = [int(x) for x in line.split()]
#                 # global SEED_TO_SOIL_MAP
#                 # for x in SEEDS:
#                 #     SEED_TO_SOIL_MAP[x] = x

#             # elif line.find('seed-to-soil map:') != -1:
#             #     pass

#     return file_content


# if __name__ == '__main__':
#     file_content = read_input('day05/input')
#     grow_data = extract_data(file_content)
#     calcualte_grow_data = process_grow_data(grow_data)
#     first_time_flag = True
#     # closest_plot = -1
#     for x in SEEDS:
#         seed = x
#         soil = SEED_TO_SOIL_MAP[x]
#         fertilizer = SOIL_TO_FERTILIZER_MAP[soil]
#         water = FERTILIZER_TO_WATER_MAP[fertilizer]
#         light = WATER_TO_LIGHT_MAP[water]
#         temperature = LIGHT_TO_TEMP_MAP[light]
#         humidity = TEMP_TO_HUMIDITY_MAP[temperature]
#         location = HUMIDITY_TO_LOCATION_MAP[humidity]
#         if first_time_flag:
#             first_time_flag = False
#             closest_plot = location
#         else:
#             if location < closest_plot:
#                 closest_plot = location
#     print(f'closest_plot: {location}')
#         # print(f'Seed {seed}, soil {soil}, fertilizer {fertilizer}, water {water}, light {light}, temperature {temperature}, humidity {humidity}, location {location}.')
    