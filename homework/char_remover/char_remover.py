new_string='123456789'
index_ch=10

def char_remover(new_string, index_ch):
    final_string = ""
    for i in range(len(new_string)):
        if i != index_ch:
            final_string += new_string[i]
    print(final_string)
char_remover(new_string, index_ch)