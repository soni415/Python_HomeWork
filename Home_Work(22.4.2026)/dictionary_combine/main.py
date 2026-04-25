first_dictionary={'United Kingdom': 'London', 'USA': 'Washington DC', 'Germany': 'Berlin'}
second_dictionary={'Germany': 'Berlin again', 'Russia': 'Moscow', 'France': 'Paris'}


def combine_dictionaries(dict1, dict2):
    new_dict = dict1
    for key in dict2:
        new_dict[key] = dict2[key]

    return new_dict


new_dict = combine_dictionaries(first_dictionary, second_dictionary)

print(new_dict)