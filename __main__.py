from flask import Flask, jsonify, request
import urllib.request
from bs4 import BeautifulSoup
app = Flask(__name__)
portNum = 5000 # initialise variables
opener = urllib.request.FancyURLopener({})
supportedLangCodes = ["cpp","python2","python3"]

@app.route('/in', methods = ['POST'])
def recieve_message():
	print("form")
#	print(request.form['user_id'])
#	print(request.form['user_name'])

	print(request.form['text'])
	args = request.form['text'].split(' ')
	if len(args) != 2:
		return("Error, Correct Syntax is /compile cpp publicslacksnippeturl.com")	
	lang = args[0]
	url = args[1]
	if url[0:23] != "https://slack-files.com/":
		print(url[0:23])
		return("Error, not a public slack file")
	if lang not in supportedLangCodes:
		return("Error, wrong language or unsupported" + str(lang))

	#Passed all checks
	soup = BeautifulSoup(opener.open(url),'html.parser')
	userCode = soup.body.div.div.div.text
	print(userCode)
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



