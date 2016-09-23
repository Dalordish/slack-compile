from flask import Flask, jsonify, request
import urllib.request
from bs4 import BeautifulSoup
import requests
app = Flask(__name__)
portNum = 5000 # initialise variables
opener = urllib.request.FancyURLopener({})
supportedLangCodes = ["cpp","python2","python3"]

@app.route('/test', methods = ['POST'])
def recieve_test():
    print(request)
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
	if url[0:24] != "https://slack-files.com/":
		print(url[0:24])
		return("Error, not a public slack file")
	if lang not in supportedLangCodes:
		return("Error, wrong language or unsupported" + str(lang))

	#Passed all checks
	soup = BeautifulSoup(opener.open(url),'html.parser')
	userCode = soup.body.div.div.div.text
	print(userCode)
	requests.post("http://api.hackerrank.com/checker/submission.json",data = JSON)
	return("working")
#curl -sX POST api.hackerrank.com/checker/submission.json -d 'source=print 1&lang=5&testcases=["1"]&api_key=hackerrank|1160459-992|7e7802c25e5a971b56773cc6443fc31168f6e664'                                                                                                                                            
	#hackerrank|1160459-992|7e7802c25e5a971b56773cc6443fc31168f6e664
'''
pseudo

Get the request
Send request to compile
get returned compiole
send to url
'''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=portNum)



