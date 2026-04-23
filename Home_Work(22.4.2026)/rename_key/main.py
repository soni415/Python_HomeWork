def rename_key(d, old_key, new_key):
    if old_key not in d:
        raise KeyError(f"Key '{old_key}' not found")

    if new_key in d:
        raise KeyError(f"Key '{new_key}' already exists")

    d[new_key] = d.pop(old_key)
    return d



my_dict = {'a': 1, 'b': 2, 'c': 3}

rename_key(my_dict, 'b', 'beta')

print(my_dict)