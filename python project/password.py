passw_informaion = [
{'zhanghao':'LJY','mima':'12345'},
{'zhanghao':'LJY','mima':'12345'}
]

def password(zhanghao,mima):
	for item in passw_informaion:
		if zhanghao == item["zhanghao"] and item["mima"] == mima:
			return "true"