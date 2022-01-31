import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])

 
def helloworld():
    message = os.environ['MSG']
    if(request.method == 'GET'):
        data = {"message": message}
        return jsonify(data)
  
if __name__ == '__main__':    
    port = int(os.environ['PORT'])
    app.run(host="0.0.0.0",port=port)
