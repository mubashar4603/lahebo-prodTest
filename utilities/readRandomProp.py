import configparser
import random


# utility which read data from prop file (loc id and dept id and org id)
def read_random_value_from_section(section_name):
    config = configparser.ConfigParser()
    file_path = "/home/mubashar4603/PycharmProjects/lahebo-prodTest/Configurations/prop.ini"
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
