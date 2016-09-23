import requests
import json
data = "source=print 1&lang=5&testcases=['1']&api_key=hackerrank|1160459-992|7e7802c25e5a971b56773cc6443fc31168f6e664"

fin = open('hackerrankApiKey.txt','r')
key = fin.readline()
print(key)
fin.close()
data2 = {
	"source":"print 1",
	"lang":5,
	"testcases": '["1","2"]',
	"api_key":str(key)
}
darta = json.dumps(data2)
r = requests.post("http://api.hackerrank.com/checker/submission.json",data = data2)
#print(json.dumps(data2))
print(r.raise_for_status)
print(r.text)
#curl -sX POST api.hackerrank.com/checker/submission.json -d 'source=print 1&lang=5&testcases=["1"]&api_key=hackerrank|1160459-992|7e7802c25e5a971b56773cc6443fc31168f6e664'

