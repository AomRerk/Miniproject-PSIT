"""Check English"""

def check_eng():
    """Check English"""
    text = input()
    alphabet_no_shift = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',\
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',\
         '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-','=',\
         '[', ']', '\\', ';', '\'', ',', '.', '/']
    alphabet_shift = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',\
         'M', 'N', 'O', 'P' ,'Q' ,'R' ,'S' ,'T', 'U', 'V', 'W', 'X','Y', 'Z',\
         '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',\
         '_', '+', '{', '}', '|', ':', '"', '<', '>', '?']
    for i in text:
        if i in alphabet_no_shift:
            print('ENG NO SHIFT')
        elif i in alphabet_shift:
            print('ENG SHIFT')
        else:
            print('OTHER LANGUAGES')

check_eng()
