def xu_ly(a):
	a = a.split()
	tong = 0
	nho_hon = []
	lon_hon = []
	try:
		for i in a:
			tong += float(i)
		tbc = tong / len(a)
		for i in a:
			if float(i) < tbc:
				nho_hon.append(i)
			else:
				lon_hon.append(i)
		print(tbc)
		print_(nho_hon)
		print('')
		print_(lon_hon)
	except:
		print('Vui lòng nhập đúng cú pháp')


def print_(a):
	for i in range(len(a)):
		print(a[i],end = " ")




def main():
	a = input('Mời dãy số cần tính trung bình cộng: ')
	xu_ly(a)
main()