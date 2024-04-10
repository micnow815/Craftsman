def list_to_string(unorganised_list):
    '''Rearanges a list into a string with each position being separated by \n'''
    rearanged_list = ''

    for item in unorganised_list:
        rearanged_list += item + '\n'

    return rearanged_list
