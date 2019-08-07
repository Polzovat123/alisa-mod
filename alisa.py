from flask import Flask,  request
import os

app = Flask(__name__)

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
        if request.json['request']['original_utterance'] == 'шалаш':
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
