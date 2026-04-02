lista= [2,3,4,5,6,7,8,9]
tr=7


def linear_search(list,target):
    for i in range(0,len(list)):
        if target == list[i]:
            return i


target=linear_search(lista,tr)
print(target)
