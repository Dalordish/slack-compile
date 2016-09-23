import urllib.request
from bs4 import BeautifulSoup

opener = urllib.request.FancyURLopener({})

soup = BeautifulSoup(opener.open('https://slack-files.com/T08QR618F-F2F1ZC34P-216e30e88a'),'html.parser')

print(soup.body.div.div.div.text)