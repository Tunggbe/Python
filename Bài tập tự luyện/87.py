def xu_ly(a,b):
	a = a.split()
	b = b.split()
	try:
		for i in a:
			test = float(i)
		for i in b:
			test = float(i)
		if len(a) != len(b):
			print('Vui lòng nhập 2 chuỗi bằng nhau!')
		else:
			#cach 1
			x = zip(a,b)
			y = tuple(x)
			for i in range(len(y)):
				tich = float(y[i][0])*float(y[len(y)-1 - i][1])
				print(tich, end =" ")
			
			# #cach 2
			# b = b[::-1]
			# x = zip(a,b)
			# y = tuple(x)
			# for i in range(len(y)):
			# 	tich = float(y[i][0])*float(y[i][1])
			# 	print(tich, end =" ")
	except:
		print('Vui lòng nhập các phần tử là số thực!')

def main():
	a = input('Mời nhập chuỗi 1: ')
	b = input('Mời nhập chuỗi 2: ')
	xu_ly(a,b)
main()