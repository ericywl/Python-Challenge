import urllib.request
import re

website = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022'

flag = True

while flag:
	with urllib.request.urlopen(website) as response: 
		php = response.read()								# read website and store bytes_info in php
		decphp = php.decode('UTF-8')						# decode php into UTF-8
		num = "".join(re.findall("[0-9]", decphp))			# find digits in decphp
		core = re.sub(r'\d+', '', website)					# strip website of digits
		if num == "16044":									
			i = int(num)
			num = str(i//2)
			new_website = core + num
			website = new_website
			print(website)
		elif num == "":
			flag = False
		else: 
			new_website = core + num
			website = new_website
			print(website)

# if the num = "16044", divide the number by 2 and concatenate the number to core
# else if there's no number, stop loop
# else just concatenate the number to core

