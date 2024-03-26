import configparser
import random


# utility which read data from prop file (loc id and dept id and org id) randomly
def read_random_value_from_section(section_name, file_name):
    config = configparser.ConfigParser()
    file_path = f"/home/mubashar4603/PycharmProjects/lahebo-prodTest/Configurations/{file_name}"
    config.read(file_path)

    # Check if the specified section exists
    if section_name not in config:
        return print(f"{section_name} section is empty"), None

    # Get all key-value pairs from the specified section
    section_items = config[section_name]

    # Choose a random key-value pair from the section
    random_key = random.choice(list(section_items.keys()))
    random_value = section_items[random_key]
    return random_value


def read_data_from_propFile(section_name, file_name, n):
    config = configparser.ConfigParser()
    file_path = f"/home/mubashar4603/PycharmProjects/lahebo-prodTest/Configurations/{file_name}"
    config.read(file_path)

    # Check if the specified section exists
    if section_name not in config:
        return None

    # Get all values from the specified section
    section_values = list(config[section_name].values())
    # print(len(section_values))

    # Check if the section has enough values
    if len(section_values) < n:
        return None

    # Retrieve the nth value (1-based index)
    nth_value = section_values[n - 1]
    return nth_value


# res = read_data_from_propFile('Usernames', 'prod_users.ini', 1)
# print(res)
