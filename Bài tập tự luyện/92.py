def xu_ly(dau_vao_list):
	ket_qua = []
	if dau_vao_list == "a":
		print('Định dạng đầu vào không hợp lệ!')
	elif dau_vao_list == "b":
		print('Danh sách  hai chiều không đúng với kích thước đã khai báo')
	else:
		for dau_vao in dau_vao_list:
			dau_vao = dau_vao.split()
			tu_dai_nhat = dau_vao[0]
			for i in range(1, len(dau_vao)):		
				if len(dau_vao[i]) > len(tu_dai_nhat):
					tu_dai_nhat = dau_vao[i]

			ket_qua.append(tu_dai_nhat)
		print(" ".join(ket_qua))

def dau_vao():
	dau_vao_list = []
	kiem_tra = True
	a = input().split()
	if len(a) <= 2:
		try:
			if int(a[0]) <= 0 or int(a[1]) <= 0:
				print('Vui lòng nhập kích thước danh sách là số nguyên dương!')
			for i in range(int(a[0])):
				dau_vao = input()
				dau_vao_list.append(dau_vao)
				dau_vao = dau_vao.split()
				if len(dau_vao) != int(a[1]):
					kiem_tra = False
			if "" in dau_vao_list or " " in dau_vao_list or kiem_tra == False:
				return "b"
			else:
				return dau_vao_list
		except:
			return "a"
	else:
		return "a"

def main():
	a = dau_vao()
	xu_ly(a)
main()
