s = "this is a test!" # Number of vowels: 5
s = "THIS IS A CAPITAL TEST!" # Number of vowels: 7
s = "ThIs Is A mIxEd CaSe TeSt!" # Number of vowels: 8

count = 0
for x in s.lower():
	if x in 'aeiou': count += 1

print("Number of vowels:", count)

