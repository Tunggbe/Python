def xu_ly(a,b):
	a = a.split(",")
	b = b.split(",")
	if len(a) == len(b):
		for i in range(len(a)):
			xoa_space(a,i)
			xoa_space(b,i)
			print(a[i] + ' - ' + b[i])
	elif len(a) != len(b):
		print('Vui lòng nhập danh sách cùng kích thước')
def xoa_space(stri, i):
	stri[i] = stri[i].strip()
	stri[i] = stri[i].replace('  ', ' ')
	return stri[i]



def main():
	a = input('Mời nhập tên: ')
	b = input('Mời nhập quốc tịch: ')
	xu_ly(a,b)
main()
	