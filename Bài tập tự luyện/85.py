def xu_ly(a):
	a= a.split()
	so_lon_nhat = float('-inf')
	dem_so_lon_nhat = 0
	vi_tri_so_lon_nhat = []
	try:
		for i in a:
			if so_lon_nhat < float(i):
				so_lon_nhat = float(i)
		for i in range(len(a)):
			if so_lon_nhat == float(a[i]):
				dem_so_lon_nhat += 1
				vi_tri_so_lon_nhat.append((i))
		in_so(so_lon_nhat, dem_so_lon_nhat, vi_tri_so_lon_nhat)
	except:
		so_lon_nhat = 'a'
		dem_so_lon_nhat = 0
		vi_tri_so_lon_nhat = []
		in_so(so_lon_nhat, dem_so_lon_nhat, vi_tri_so_lon_nhat)

def in_so(so_lon_nhat, dem_so_lon_nhat, vi_tri_so_lon_nhat):	
	if so_lon_nhat == float('-inf'):
		print('Danh sách rỗng!')
	elif so_lon_nhat =='a':
		print('Đầu vào không hợp lệ')
	else:
		print(str(so_lon_nhat))
		print(str(dem_so_lon_nhat))
		for i in vi_tri_so_lon_nhat:
			print(i, end = " ")

def main():
	a = input("Vui lòng nhập chuỗi: ")
	xu_ly(a)
main()