class Chuoi:
	def __init__(self, chuoi):
		self.chuoi = chuoi
		self.mot_nua = len(self.chuoi) // 2
		self.nua_dau = self.chuoi[:self.mot_nua]
		self.nua_cuoi = self.chuoi[self.mot_nua:]

def print_(chuoi):
		for tu in chuoi:
			print(tu, end = " ")
		print("")

def xu_ly(a,b):
	a = Chuoi(a.split(" "))
	b = Chuoi(b.split(" "))
	chuoi_1_moi = a.nua_dau + b.nua_cuoi
	chuoi_2_moi = b.nua_dau + a.nua_cuoi
	print_(chuoi_1_moi)
	print_(chuoi_2_moi)

def main():
	a = input('Mời nhập mã chuỗi 1: ')
	b = input('Mời nhập mã chuỗi 2: ')
	xu_ly(a,b)
main()