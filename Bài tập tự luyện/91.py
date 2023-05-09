def xu_ly(dau_vao_list):
	print("-------")
	if dau_vao_list == "a":
		print('Định dạng đầu vào không hợp lệ!')
	elif "" in dau_vao_list or dau_vao_list == "b":
		print('Danh sách hai chiều không đúng kích thước đã khai báo')
	else:	
		for i in dau_vao_list:
			print(i)
			print(dau_vao_list)

def dau_vao(a):
	dau_vao_list = []
	try:
		for i in range(int(a[0])):
			dau_vao = input()
			dau_vao_list.append(dau_vao)
		for i in dau_vao_list:
			if len(i)+1 != int(a[1]):
				return 'b'
			else:
				return dau_vao_list
	except:
		return "a"
def main():
	a = input().split()
	if int(a[0]) <= 0:
		print('Vui lòng nhập kích thước danh sách là số nguyên dương!')
	else:	
		dau_vao_list = dau_vao(a)
		xu_ly(dau_vao_list)
main()

