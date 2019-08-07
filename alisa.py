from flask import Flask,  request
import os

app = Flask(__name__)

def check_polindrom(words):
    a = words[::-1]
    if a == words:
        return True
    esle :
        return False

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
        if check_polindrom(request.json['request']['original_utterance']) == True:
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
