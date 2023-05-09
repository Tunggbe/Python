print('nhap ten cua ban thu nhat')
ten_a = input()
print("nhap chieu cao cua ban", ten_a)
chieu_cao_a = int(input())
print('nhap ten cua ban thu hai')
ten_b = input()
print('nhap chieu cao cua ban', ten_b)
chieu_cao_b = int(input())
if chieu_cao_a > chieu_cao_b: 
	print(ten_a ,"cao hon", ten_b)
elif chieu_cao_a == chieu_cao_b:
	print(ten_a, 'va', ten_b, 'cao bang nhau')
elif chieu_cao_a < chieu_cao_b:
	print(ten_a ,'thap hon', ten_b)