def tu_dai_nhat(s):
	longest = ""
	for i in s:
		if (len(i) > len(longest)) or (len(i) == len(longest) and i < longest) :
			longest = i
		
	return longest

s = input(": ").split()

print(tu_dai_nhat(s))