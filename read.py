#-*- coding: utf-8 -*-
import os
application = []

if os.path.isfile('item.csv'):
	print('Yeah! 有檔案')
	with open('item.csv' , 'r') as f:
	for line in f:
		if '商品名稱,商品價格' in line:
			continue
		item , price = line.strip().split(',')
		application.append([item , price])
else:
	print('找不到檔案...')

while True:
	item = input("請輸入商品名稱或按q離開:")
	if item == 'q':
		break
	price = input("請輸入商品價格:")
	price = int(price)
	application.append([item , price])
print(application)

for app in application:
	print (app[0] , '的價格是' , app[1])

with open( 'item.csv' , 'w' ) as f:	
	f.write('商品名稱,商品價格\n')
	for app in application:
		f.write(app[0] + ',' + str(app[1]) + '\n')