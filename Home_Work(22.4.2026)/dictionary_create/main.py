list_Countries=["United Kingdom","USA","Germany","Russia","France"]
list_Capitals=["London","Washington DC","Berlin","Moscow","Paris"]


#Long solution
def dictionary_create(list1,list2):
    new_dictionary = {}
    if len(list1) != len(list2):
        return "Error The list must have the same size"

    for i in range (len(list1)):
        new_dictionary[list1[i]] = list2[i]

    return new_dictionary

#Short solution

def dictionary_create_2(list1,list2):
    if len(list1) != len(list2):
        return "Error The list must have the same size"
    return dict(zip(list1,list2))



new_dictionary = dictionary_create(list_Countries,list_Capitals)
new_dictionary2=dictionary_create_2(list_Countries,list_Capitals)

print(new_dictionary)
print()
print(new_dictionary2)


