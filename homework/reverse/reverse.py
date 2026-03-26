long_string="😎!rim et nup ejn ereB"

def reverse(long_string):
    new_string = long_string[::-1]
    print(new_string)
    return new_string


def reverse2(long_string):
    length = len(long_string)
    new_string = ''
    for i in range(length-1,-1,-1):
        new_string += long_string[i]
    print(new_string)
reverse(long_string)
reverse2(long_string)