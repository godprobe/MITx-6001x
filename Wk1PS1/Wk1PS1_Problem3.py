s = 'abcdefghijklmnopqaidtheresneveranotherproblemsherwoodgabcdrapefruyzitoccurrencefghjlmnopqrsssstuyvz'
longest = 0
current = ''
best = ''
for letter in s:
	if current.isalpha() and letter >= current[-1]:
		current += letter
		# print("Current eval:",current)
		if len(current) > longest:
			# print("New best:",current)
			longest = len(current)
			best = current
	else:
		current = letter
print("Longest substring in alphabetical order is:", best)
