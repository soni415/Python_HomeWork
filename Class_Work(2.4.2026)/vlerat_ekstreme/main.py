lista=[1,2,3,4,5]

def find_max(lista):
    max = lista[0]
    for i in lista:
        if i > max:
            max = i
    return max

def find_min(lista):
    min = lista[0]
    for i in lista:
        if i < min:
            min = i
    return min

max=find_max(lista)
min=find_min(lista)

print("max:",max," min:",min)