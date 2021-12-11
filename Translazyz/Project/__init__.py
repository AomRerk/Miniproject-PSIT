from flask import Flask, request, abort
import requests
import json
from Project.Config import *
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


def translazymain(message):
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
    count_eng = 0
    count_thai = 0
    for i in message:
        if i in alphabet_eng:
            count_eng += 1
        elif i in alphabet_thai:
            count_thai += 1
    for i in message:
        if i in alphabet_eng:
            cate = trans('ENGLISH', i)
        elif i in alphabet_thai:
            cate = trans('THAI', i)
        elif i == ' ':
            cate = ' '
        return cate

app = Flask(__name__)

@app.route('/webhook', methods = ['POST', 'GET'])
def webhook():
    if request.method == 'POST':
        payload = request.json

        Reply_token = payload['events'][0]['replyToken']
        print(Reply_token)
        message = payload['events'][0]['message']['text']
        Reply_messasge = ''
        for i in message:

            Reply_messasge += translazymain(i)
        print(message)
        ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        return request.json, 200

    elif request.method == 'GET':
        return 'This is method GET' , 200
    
    else:
        abort(400)

@app.route('/')
def hello():
    return 'hello world book',200

def ReplyMessage(Reply_token, TextMessage, Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Line_Acees_Token) ##ที่ยาวๆ
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }

    data = {
        "replyToken":Reply_token,
        "messages":[{
            "type":"text",
            "text":TextMessage
        }]
    }

    data = json.dumps(data) ## dump dict >> Json Object
    r = requests.post(LINE_API, headers=headers, data=data) 
    return 200
