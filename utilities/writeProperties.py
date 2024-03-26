import configparser
import openpyxl


def save_to_properties_file(loc_ids=None, dep_ids=None, org_id=None, token=None, prop_file_path=None, usernames=None, passwords=None):
    config = configparser.ConfigParser()
    config.add_section('Usernames')
    config.add_section('Passwords')
    config.add_section('Token')
    config.add_section('Locations')
    config.add_section('Departments')
    config.add_section('Organisation')
    prop_file_path = f"/home/mubashar4603/PycharmProjects/lahebo-prodTest/Configurations/{prop_file_path}"

    # for writing the locs IDs into prop file
    if isinstance(loc_ids, list) and loc_ids:
        for index, value in enumerate(loc_ids):
            config['Locations']['value{}'.format(index + 1)] = value

    # for writing the dept IDs into prop file
    if isinstance(dep_ids, list) and dep_ids:
        for index, value in enumerate(dep_ids):
            config['Departments']['value{}'.format(index + 1)] = value

    # for writing the usernames
    if isinstance(usernames, list) and usernames:
        for index, value in enumerate(usernames):
            config['Usernames']['value{}'.format(index + 1)] = value

    # for writing the passwords
    if isinstance(passwords, list) and passwords:
        for index, value in enumerate(passwords):
            config['Passwords']['value{}'.format(index + 1)] = value

    # for writing the org ID into prop file
    if org_id is not None:
        config['Organisation']['value'] = org_id

    # for writing the token into prop file
    if token is not None:
        config['Token']['value'] = token

    with open(prop_file_path, 'w') as configfile:
        config.write(configfile)

































# read data from excel and store that into dict
# def readExcel_writeProp(file_path, column_a, column_b):
#     data = {}
#
#     try:
#         # Load the workbook
#         workbook = openpyxl.load_workbook(file_path)
#         # Get the active worksheet
#         worksheet = workbook.active
#
#         # Extract data from the specified column
#         for cell_a, cell_b in zip(worksheet[column_a][1:], worksheet[column_b][1:]):
#             key = cell_a.value
#             value = cell_b.value
#             # Only add to dictionary if both key and value are not None
#             if key is not None and value is not None:
#                 data[key] = value
#
#     except FileNotFoundError:
#         print(f"File '{file_path}' not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
#     return data
#
#
# path = "/home/mubashar4603/PycharmProjects/lahebo-prodTest/TestData/credential.xlsx"
# res = readExcel_writeProp(path, 'A', 'B')
# print(res)
