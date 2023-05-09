def list_(n):
	list_ = [i for i in range(n)] 
	list_ = list_[::-1]
	return list_
try:
	n = int(input("Mời nhập số tự nhiên: "))

	if n < 0:
		print("Vui lòng nhập số tự nhiên")
	else:
		list_=list_(n)
		print(*list_)
except: 
	print("Vui lòng nhập số tự nhiên")