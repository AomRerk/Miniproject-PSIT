from flask import Flask, request, abort
import requests
import json
from Translazy.Config import *
from Translazy.translazy_main import *

app = Flask(__name__)


@app.route('/webhook', methods=['POST','GET'])
def webhook():
    #get ได้ข้อมูลมาจาก webhook
    #post เอาข้อมูลที่มีป้อนขึ้นไปบน webhook -> line ส่งต่อให้ webhook
    if request.method == 'POST':
        event_reply = request.json

        Reply_token = event_reply['events'][0]['replyToken']
        message = event_reply['events'][0]['message']['text']
        Reply_messasge = translazymain(message)
        ReplyMessage(Reply_token,Reply_messasge,channel_access_token)

        return request.json, 200
    elif request.method == 'GET' :
        return 'this is method GET!!!' , 200
    else:
        abort(400)
    #request.method เช็คว่า method อะไรเข้ามา

@app.route('/')
def hello():
    return 'hello', 200

def ReplyMessage(Reply_token, TextMessage, channel_access_token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(channel_access_token)
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

    data = json.dumps(data)
    r = requests.post(LINE_API, headers=headers, data=data)
    return 200