def xu_ly(a):
	a = a.split()
	so_le = []
	if len(a) == 0:
		print("Danh sách rỗng")
	else:	
		try:
			for i in a:
				if int(i) % 2 == 1 or int(i) == 1:
					so_le.append(i)
		except:
			print('Vui lòng nhập số tự nhiên')
			so_le = []
	for so in so_le:
		print(so, end = " ")

def main():
	a = input('Mời nhập các số cách nhau bởi đấu cách: ')
	xu_ly(a)

main()