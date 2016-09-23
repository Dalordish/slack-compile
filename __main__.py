from flask import Flask, jsonify, request
app = Flask(__name__)
portNum = 5000 # initialise variables


@app.route('/in', methods = ['POST'])
def recieve_message():
	print(request)

'''
pseudo

Get the request
Send request to compile
get returned compiole
send to url
'''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=portNum)