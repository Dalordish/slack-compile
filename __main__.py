from flask import Flask, jsonify, request
import requests
app = Flask(__name__)
portNum = 5000 # initialise variables


@app.route('/in', methods = ['POST'])
def recieve_message():
	print("form")
#	print(request.form['user_id'])
#	print(request.form['user_name'])

	print(request.form['text'])
	args = request.form['text'].split(' ')
	if len(args) != 2:
		return("Error, Correct Syntax is /compile cpp publicslacksnippeturl.com")
	print(args[0])
	print(args[1])

	return("working")
'''
pseudo

Get the request
Send request to compile
get returned compiole
send to url
'''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=portNum)