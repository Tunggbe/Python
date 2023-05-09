def xu_ly(so_dong, so_cot, ma_tran):
	ket_qua = []
	try:
		for ky_tu in ma_tran[0]:
			so_lan_trung = 0
			for i in range(1,so_dong):
				for j in range(so_cot):
					if ky_tu == ma_tran[i][j]:
						so_lan_trung += 1
			if so_lan_trung == so_dong - 1:
				ket_qua.append(ky_tu)
		print('--------')
		print(" ".join(ket_qua))
	except:
		print("Danh sách hai chiều không đúng kích thước đã khai báo")

def dau_vao(so_dong, so_cot):
	ma_tran = []
	for i in range(so_dong):
		dong = input().split()
		ma_tran.append(dong)
	return ma_tran

def ket_qua(a, so_dong, so_cot, ma_tran):
	if len(a) > 2:
		print("Định dạng đầu vào không hợp lệ")
	elif so_dong <= 0 or so_cot <= 0:
		print('Vui Lòng nhập kích thước danh sách là số nguyên dương')
	else:
		xu_ly(so_dong, so_cot, ma_tran)
			

def main():
	a = input().split()
	so_dong = int(a[0])
	so_cot = int(a[1])
	ma_tran = dau_vao(so_dong, so_cot)
	ket_qua(a, so_dong, so_cot, ma_tran)
main()

