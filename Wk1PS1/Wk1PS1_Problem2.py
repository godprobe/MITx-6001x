count = 0
s = 'bobazcbobobegghaklbob'
for x in range(0,len(s)-2):
	if (s[x:x+3] == 'bob'):
		count += 1
print("Number of times bob occurs is:", count)

