#逢7跳过游戏
'''for循环实现
for i in range(1,101):
	if i%7 == 0 or i%10 == 7 or i//10 == 7:
		continue
	print(i)
'''
#while循环实现
i = 1
while i <=100:
	if i%7 == 0 or i%10 == 7 or i//10 == 7:
		i += 1
		continue
	print(i)
	i += 1	