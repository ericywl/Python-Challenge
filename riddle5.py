import urllib.request
import pickle

website = "http://www.pythonchallenge.com/pc/def/banner.p"

with urllib.request.urlopen(website) as response:
	html = response.read()

# read website and store bytes_info in html

hint = (pickle.loads(html))
for line in hint:
	print("".join([k * v for k, v in line]))

# read a pickled object hierarchy from a bytes object and return the reconstituted object hierarchy specified therein
# print k number of v in each line
