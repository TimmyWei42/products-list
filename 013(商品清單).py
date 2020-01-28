products = []
while True:	
	name = input('請輸入商品名: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
print(products)
with open('products list.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')