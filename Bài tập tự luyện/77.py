def xu_ly(a):
	a = a.split()
	so_nho_nhat = float("Inf")
	if len(a) == 0:
		print('nothing!!')	
	else:
		try:
			for i in a:
				if float(i) < so_nho_nhat:
					so_nho_nhat = float(i)
			print(so_nho_nhat)
		except:
			print('Vui lòng nhập số hợp lệ')
	
def main():
	a = input("Nhập vào các số cách nhau bởi dấu cách: ")
	xu_ly(a)

main()