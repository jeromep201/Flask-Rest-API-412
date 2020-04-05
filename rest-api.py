import flask
import hashlib
import math
import requests
import json
from flask import request, jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = False
 
@app.route('/', methods=['GET'])
def home():
    return "<h1>Rest API</h1><p>This site is under construction.</p>"

@app.route('/factorial/<int:num>', methods=['GET'])
def factorial(num):
    return jsonify({'input':num, 'result': math.factorial(num)})

# MD5 Hash Function
@app.route('/md5/<string:string>', methods=['GET'])
def hash_function(string):
    result = hashlib.md5(string.encode()) #Encode string
    return jsonify(result.hexdigest()) #Print md5 hash

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
        
@app.route('/is-prime/<int:n>', methods=['GET'])
def is_prime(n):
    if (n==1):
        return jsonify("False")
    elif (n==2):
        return jsonify("True")
    else:
        for x in range(2,n):
            if(n % x==0):
                return jsonify("False")
        return jsonify("True") 
       
#Slack Alert Function
@app.route('/slack-alert/<string:string>', methods=['GET'])
def slack_alert(string):
    url = 'https://hooks.slack.com/services/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'
    requests.post(url,data=json.dumps(string))
    return jsonify({'input':string, 'result': "True"})

app.run()
