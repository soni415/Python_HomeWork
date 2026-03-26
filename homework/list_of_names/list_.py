usernames = ["ana", "mark", "john", "ana", "john", "ana"]

frequency_list={}

for name in usernames:
    frequency_list[name] = usernames.count(name)

for key, value in frequency_list.items():
    print(key," : ",value)