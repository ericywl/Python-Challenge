from string import ascii_lowercase

alpha_list = list(ascii_lowercase) # generate list of ascii_lowercase
sent = "map"

x = 0
y = 2

while y < 28:
	alpha_list[x%26] = list(ascii_lowercase)[y%26]
	x = (x + 1)
	y = (y + 1)

# makes a list where every alphabet becomes the one that is two characters after in the alphabetical order
# ie. a -> c, b -> d, c -> e and so on

intab = ascii_lowercase
outtab = ''.join(alpha_list)
transtab = ''.maketrans(intab, outtab)

print(sent.translate(transtab))

# map the normal alphabets with the changed alphabets and translate sent with that translation map