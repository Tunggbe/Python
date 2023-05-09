def xu_ly(ma_tran, dong_cot):
	dong = int(dong_cot[0])
	cot = int(dong_cot[1])
	print("-------")
	for j in range(cot):
		for i in range(dong):
			print(ma_tran[i][j], end = " ")
		print('')

def dau_vao(a):
	ma_tran = []
	for i in range(int(a[0])):
		dong = input().split()
		ma_tran.append(dong)
	return ma_tran

def kiem_tra(dong_cot, ma_tran):
	try:
		dong = int(dong_cot[0])
		cot = int(dong_cot[1])
		if dong <= 0 or cot <= 0:
				return "a"
		elif len(dong_cot) > 2:
				return "c"
		else:
			for i in ma_tran:
				if len(i) != cot:
					return "b"
	except:
		return "c"

def running(kiem_tra, dong_cot, ma_tran):
	if kiem_tra == "a":
		print("Vui lòng nhập kích thước dánh sách là số nguyên dương!")
	elif kiem_tra == "b":
		print("Danh sách hai chiều không đúng kích thước đã khai báo!")
	elif kiem_tra == "c":
		print("Định dạng đầu vào không hợp lệ!")
	else:
		xu_ly(ma_tran, dong_cot)

def main():
	dong_cot = input().split()
	ma_tran = dau_vao(dong_cot)
	kiem_tra1 = kiem_tra(dong_cot, ma_tran)
	running(kiem_tra1, dong_cot, ma_tran)
main()