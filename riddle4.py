import urllib.request
import re

website = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'

while True:
	with urllib.request.urlopen(website) as response:
		php = response.read()
		decphp = php.decode('UTF-8')
		num = "".join(re.findall("[0-9]", decphp))
		core = re.sub(r'\d+', '', website)
		if num == "16044":
			i = int(num)
			num = str(i//2)
			new_website = core + num
			website = new_website
			print(website)
		else: 
			new_website = core + num
			website = new_website
			print(website)



