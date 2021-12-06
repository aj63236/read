application = []

while True:
	item = input("請輸入商品名稱或按q離開:")
	if item == 'q':
		break
	price = input("請輸入商品價格:")
	application.append([item , price])
print(application)

for app in application:
	print(app)