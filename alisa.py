from flask import Flask,  request
import os

app = Flask(__name__)

def check_polindrom(words):
    lin = len(words)/2
    linf = len(words)
    if linf%2 == 1:
        lin-=1
    i=int(0)
    while i < lin:
        if word[i] != word[linf-1-i]:
            return False
        i = i +1
    return True
    

@app.route('/', methods=['POST'])
def echo():
    
    if request.json['request']['original_utterance'] == '':
        response = {
            'version':request.json['version'],
            'session':request.json['session'],
            'response':{
              'text':  'Спасаев в пути ... Назовите слово'
            }
        }
    else:
        if check_polindrom(request.json['request']['original_utterance']) == Trues:
            response = {
                'version':request.json['version'],
                'session':request.json['session'],
                'response':{
                  'text':  'True. Спасаев в пути ... Назовите слово'
                }
            }
        else:
            response = {
                'version':request.json['version'],
                'session':request.json['session'],
                'response':{
                  'text':  'Fak. Спасаев в пути ... Назовите слово'
                }
            }
    return response

app.run(host='0.0.0.0', port=os.getenv('PORT',5000))
