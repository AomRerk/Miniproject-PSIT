"""Check TH or ENG"""
import random

def trans(cate, words):
    if cate == 'THAI':
        transs = {'ๅ':'1', '/':'2', '-':'3', 'ภ':'4', 'ถ':'5', 'ุ':'6', 'ึ':'7', 'ค':'8', 'ต':'9', 'จ':'0', 'ข':'-', 'ช':'=',\
            'ๆ':'q', 'ไ':'w', 'ำ':'e', 'พ':'r', 'ะ':'t', 'ั':'y', 'ี':'u', 'ร':'i', 'น':'o', 'ย':'p', 'บ':'[', 'ล':']', 'ฃ':'\\', 'ฟ':'a',\
            'ห':'s', 'ก':'d', 'ด':'f', 'เ':'g', '้':'h', '่':'j', 'า':'k', 'ส':'l', 'ว':';', 'ง':'\'', 'ผ':'z', 'ป':'x','แ':'c',\
            'อ':'v', 'ิ':'b', 'ื':'n', 'ท':'m', 'ม':',', 'ใ':'.', 'ฝ':'/', '+':'!', '๑':'@', '๒':'#', '๓':'$', '๔':'%', 'ู':'^', \
            '฿':'&', '๕':'*', '๖':'(', '๗':')', '๘':'_', '๙':'+','๐':'Q', '"':'W', 'ฎ':'E', 'ฑ':'R' ,'ธ':'T' ,'ํ':'Y' ,'๊':'U' ,'ณ':'I', \
            'ฯ':'O', 'ญ':'P', 'ฐ':'{', ',':'}', 'ฅ':'|', 'ฤ':'A', 'ฆ':'S', 'ฏ':'D', 'โ':'F', 'ฌ':'G', '็':'H', '๋':'J', 'ษ':'K', 'ศ':'L', \
            'ซ':':', '.':'"', '(':'Z', ')':'X', 'ฉ':'C', 'ฮ':'V', 'ฺ':'B', '์':'N', '?':'M', 'ฒ':'<', 'ฬ':'>', 'ฦ':'?', '_':'`', '~':'%'}

    if cate == 'ENGLISH':
        transs = {'1':'ๅ', '2':'/', '3':'-', '4':'ภ', '5':'ถ', '6':'ุ','7': 'ึ', '8':'ค', '9':'ต', '0':'จ', '-':'ข', '=':'ช',\
            'q':'ๆ', 'w':'ไ', 'e':'ำ', 'r':'พ', 't':'ะ', 'y':'ั', 'u':'ี', 'i':'ร', 'o':'น', 'p':'ย', '[':'บ', ']':'ล', '\\':'ฃ', 'a':'ฟ',\
            's':'ห', 'd':'ก', 'f':'ด', 'g':'เ', 'h':'้', 'j':'่', 'k':'า', 'l':'ส', ';':'ว', '\'':'ง', 'z':'ผ', 'x':'ป','c':'แ',\
            'v':'อ', 'b':'ิ', 'n':'ื', 'm':'ท', ',':'ม', '.':'ใ', '/':'ฝ', '!':'+', '@':'๑', '#':'๒', '$':'๓', '%':'๔', '^':'ู', \
            '&':'฿', '*':'๕', '(':'๖', ')':'๗', '_':'๘', '+':'๙','Q':'๐', 'W':'"', 'E':'ฎ', 'R':'ฑ' ,'T':'ธ' ,'Y':'ํ' ,'U':'๊' ,'I':'ณ', \
            'O':'ฯ', 'P':'ญ', '{':'ฐ', '}':',', '|':'ฅ', 'A':'ฤ', 'S':'ฆ', 'D':'ฏ', 'F':'โ', 'G':'ฌ', 'H':'็', 'J':'๋', 'K':'ษ', 'L':'ศ', \
            ':':'ซ', '"':'.', 'Z':'(', 'X':')', 'C':'ฉ', 'V':'ฮ', 'B':'ฺ', 'N':'์', 'M':'?', '<':'ฒ', '>':'ฬ', '?':'ฦ', '~':'%', '`':'_'}
    return transs[words]


def capslock(cate, words):
    """ กด caplock ค้างไว้ """
    thai = {'+':'ๅ', '๑':'/', '๒':'-', '๓':'ภ', '๔':'ถ', 'ู':'ุ', '฿':'ึ'\
    , '๕':'ค', '๖':'ต', '๗':'จ', '๘':'ข', '๙':'ช', '๐':'ๆ', '"':'ไ'\
    , 'ฎ':'ำ', 'ฑ':'พ', 'ธ':'ะ', 'ํ':'ั', '๊':'ี', 'ณ':'ร', 'ฯ':'น', 'ญ':'ย'\
    , 'ฐ':'บ', 'ฅ':'ฃ', 'ฤ':'ฟ', 'ฆ':'ห', 'ฏ':'ก', 'โ':'ด', 'ฌ':'เ', '็':'้'\
    , '๋':'่', 'ษ':'า', 'ศ':'ส', 'ซ':'ว', '.':'ง', '(':'ผ', ')':'ป', 'ฉ':'แ', \
    'ฮ':'อ', 'ฺ':'ิ', '์':'ื', '?':'ท', 'ฒ':'ม', 'ฬ':'ใ', 'ฦ':'ฝ'}

    eng = {'`':'`', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', '0':'0', '-':'-', '=':'='\
    , 'Q':'q', 'W':'w', 'E':'e', 'R':'r', 'T':'t', 'Y':'y', 'U':'u', 'I':'i', 'O':'o', 'P':'p', '[':'[', ']':']', '\\':'\\', 'A':'a'\
    , 'S':'s', 'D':'d', 'F':'f', 'G':'g', 'H':'h', 'J':'j', 'K':'k', 'L':'l', ';':';', '\'':'\'', 'Z':'z', 'X':'x', 'C':'c', 'V':'v'\
    , 'B':'b', 'N':'n', 'M':'m', ',':',', '.':'.', '/':'/'}


def main():
    """Check if English or Thai"""
    alphabet_eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',\
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',\
         '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-','=',\
         '[', ']', '\\', ';', '\'', ',', '.', '/', 'A', 'B', 'C', 'D', 'E', 'F',\
         'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P' ,'Q' ,'R' ,'S' ,'T',\
         'U', 'V', 'W', 'X','Y', 'Z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',\
         '_', '+', '{', '}', '|', ':', '"', '<', '>', '?']

    alphabet_thai = ['ๅ', '/', '-', 'ภ', 'ถ', 'ุ', 'ึ', 'ค', 'ต', 'จ', 'ข', 'ช',\
         'ๆ', 'ไ', 'ำ', 'พ', 'ะ', 'ั', 'ี', 'ร', 'น', 'ย', 'บ', 'ล', 'ฃ', 'ฟ',\
         'ห', 'ก', 'ด', 'เ', '้', '่', 'า', 'ส', 'ว', 'ง', 'ผ', 'ป','แ',\
         'อ', 'ิ', 'ื', 'ท', 'ม', 'ใ', 'ฝ', '_', '+', '๑', '๒', '๓', '๔', 'ู', \
         '฿', '๕', '๖', '๗', '๘', '๙','๐', '"', 'ฎ', 'ฑ' ,'ธ' ,'ํ' ,'๊' ,'ณ', \
         'ฯ', 'ญ', 'ฐ', ',', 'ฅ', 'ฤ', 'ฆ', 'ฏ', 'โ', 'ฌ', '็', '๋', 'ษ', 'ศ', \
         'ซ', '.', '(', ')', 'ฉ', 'ฮ', 'ฺ', '์', '?', 'ฒ', 'ฬ', 'ฦ', '%']
    the_same_thing = ['-', '(', ')', '_', '"', '/', '%']
    contr = input().lower().strip() #เอาไว้บอกว่าอยากใช้ฟังก์ไหน
    text = input()
    count_eng = 0
    count_thai = 0
    for i in text:
        if i in alphabet_eng:
            count_eng += 1
        elif i in alphabet_thai:
            count_thai += 1
    for i in text:
        if i in the_same_thing:
            if count_eng > count_thai:
                cate = trans('ENGLISH', i)
            elif count_thai > count_eng:
                cate = trans('THAI', i)
            else:
                cate = random.choice(trans('ENGLISH', i) or trans('THAI', i))
        elif i in alphabet_eng:
            cate = trans('ENGLISH', i)
        elif i in alphabet_thai:
            cate = trans('THAI', i)
        elif i == ' ':
            print(" ", end="")
            continue
        print(cate, end="")

main()
