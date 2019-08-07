#密碼重試程式.
#self write
i = 3
pwd = 'a123456'
if True:
	password = input('請輸入密碼:')
	if pwd == password:
		print('"登入成功"!')
	else :
		i = i - 1
		print('"密碼錯誤!還有', i, '次機會')
		password = input('請輸入密碼:')
		if pwd == password:
			print('"登入成功"!')
		else :
			i = i - 1	
			print('"密碼錯誤!還有', i, '次機會')
			password = input('請輸入密碼:')
			if pwd == password:
				print('"登入成功"!')
			else :	
				i = i - 1
				if i <= 0:
					print('沒機會了')
#End