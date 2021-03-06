import flask
from flask import request, jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = False


@app.route('/', methods=['GET'])
def home():
    return "<h1>Rest API</h1><p>This site is under construction.</p>"

@app.route('/factorial/<int:num>', methods=['GET'])
def factorial(num):
    return jsonify({'input':num, 'result': math.factorial(num)})

@app.route('/fibonacci/<int:num>', methods=['GET'])
def fibonacci(num):
    if (num <= 0) : 
        return 0
   
    fibo =[0] * (num+1) 
    fibo[1] = 1
   
    # Initialize result 
    sm = fibo[0] + fibo[1] 
   
    # Add remaining terms 
    for i in range(2,num+1) : 
        fibo[i] = fibo[i-1] + fibo[i-2] 
        sm = sm + fibo[i] 
          
    return jsonify({"input":num, "output":sm})
        
@app.route('/factorial/<string:message>', methods=['GET'])
def md5(message):
    return jsonify({'input':message, 'result': hashlib.md5(message)})


app.run()
