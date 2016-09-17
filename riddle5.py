import urllib.request
import pickle

website = "http://www.pythonchallenge.com/pc/def/banner.p"

with urllib.request.urlopen(website) as response:
	html = response.read()

hint = (pickle.loads(html))
for line in hint:
	print("".join([k * v for k, v in line]))

