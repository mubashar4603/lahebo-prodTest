import configparser


def save_to_properties_file(loc_ids, dep_ids, org_id):
    config = configparser.ConfigParser()
    config.add_section('Locations')
    config.add_section('Departments')
    config.add_section('Organisation')
    prop_file_path = "/home/mubashar4603/PycharmProjects/lahebo-prodTest/Configurations/prop.ini"
    for index, value in enumerate(loc_ids):
        config['Locations']['value{}'.format(index + 1)] = value
    for index, value in enumerate(dep_ids):
        config['Departments']['value{}'.format(index + 1)] = value
    config['Organisation']['value'] = org_id

    with open(prop_file_path, 'w') as configfile:
        config.write(configfile)


# Example list of values
# location_ids = [
#     '36227077-acee-4512-bf56-5024fc2c703f',
#     'd586a35c-850c-4ea5-8df8-bb28f6b4fe31',
#     'a0dcbd65-328e-484c-ad93-79393ecc1d7a',
#     '73f18df9-1f48-4dee-b424-c71513e49989',
#     'ca859626-29b6-4afd-a9e6-e3287236737d'
# ]
# department_ids = [
#     '36227077-acee-4512-bf56-5024fc2c703f',
#     'd586a35c-850c-4ea5-8df8-bb28f6b4fe31',
#     'a0dcbd65-328e-484c-ad93-79393ecc1d7a',
#     '73f18df9-1f48-4dee-b424-c71513e49989',
#     'ca859626-29b6-4afd-a9e6-e3287236737d'
# ]
#
# save_to_properties_file(location_ids, department_ids)
