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
	print (app[0] , '的價格是' , app[1])

with open( 'item.csv' , 'w' ) as f:
	for app in application:
		f.write(app[0] + ',' + app[1] + '\n')