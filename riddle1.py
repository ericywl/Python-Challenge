from string import ascii_lowercase

alpha_list = list(ascii_lowercase)
sent = "map"

x = 0
y = 2

while y < 28:
	alpha_list[x%26] = list(ascii_lowercase)[y%26]
	x = (x + 1)
	y = (y + 1)

intab = ascii_lowercase
outtab = ''.join(alpha_list)
transtab = ''.maketrans(intab, outtab)

print(sent.translate(transtab))

