a = "abcdefg"
a= list(a)
print(a)
b = []
len_a = len(a)
for i in range(len(a)//2):
	tg = a[i]
	a[i] = a[len_a-i-1]
	a[len_a-i-1] = tg
print(a)

