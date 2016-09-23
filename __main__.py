from flask import Flask, jsonify, request
import urllib.request
from bs4 import BeautifulSoup
import requests
import json
app = Flask(__name__)
portNum = 5000 # initialise variables
opener = urllib.request.FancyURLopener({})

#Getting keys
fin = open('hackerrankApiKey.key','r')
APIkey = fin.readline().strip('\n')
print(APIkey)
print("Hackerrank api key is " + str(APIkey))
fin.close()

#Getting languages

langReq = requests.get("http://api.hackerrank.com/checker/languages.json")

supportedLangCodes = json.loads(langReq.json)['codes']




@app.route('/test', methods = ['POST'])
def recieve_test():
    print(request)
    print(request.form)
    return("asadf")
@app.route('/in', methods = ['POST'])
def recieve_message():
	print("form")
#	print(request.form['user_id'])
#	print(request.form['user_name'])
	print(request.form['response_url'])
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

	hackRequest = {
		"source":str(userCode),
		"lang":str(supportedLangCodes['lang']),
		"testcases": '["1","2"]', #TODO MAKE REAL TESTCASES BY USER
		"api_key":str(APIkey)
	}

	postback = requests.post("http://api.hackerrank.com/checker/submission.json",data = hackRequest)
	postbackJSON = json.loads(postback.text)
	print("POSTBACK JSON")
	print(postbackJSON)
	finalResponse = {
    "response_type": "in_channel",
    "text": str(postbackJSON['result']['stdout'])
	}
	print("FINAL RESPONSE")
	print(finalResponse)

	finalRequest = requests.post(str(request.form['response_url']), data= json.dumps(finalResponse))
	return("Compiling...")
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



