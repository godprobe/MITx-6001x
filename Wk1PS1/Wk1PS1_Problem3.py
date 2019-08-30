# NOTE: This could be more robust: results in an error if s is a blank string.
s = 'z'
longest = 1
current = s[0]
best = current
for letter in s[1:]:
	if letter >= current[-1]:
		current += letter
		# print("Current eval:",current)
		if len(current) > longest:
			# print("New best:",current)
			longest = len(current)
			best = current
	else:
		current = letter
print("Longest substring in alphabetical order is:", best)
