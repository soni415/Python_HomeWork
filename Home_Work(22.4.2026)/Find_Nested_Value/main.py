People = {
    "student1": {
        "Name": "Arber",
        "Age": 20,
        "Gender": "Man"
    },
    "student2": {
        "Name": "Mira",
        "Age": 21,
        "Gender": "Woman"
    },
    "student3": {
        "Name": "Ilir",
        "Age": 19,
        "Gender": "Man"
    },
    "student4": {
        "Name": "Ana",
        "Age": 18,
        "Gender": "Woman"
    }
}

def find_age(nested_dict,student):
    if student not in nested_dict:
        return "Value not found"
    our_student = nested_dict[student]
    age=our_student["Age"]

    return age


age_of_student = find_age(People,"student1")
print(age_of_student)


