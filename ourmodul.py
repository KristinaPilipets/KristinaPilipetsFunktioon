def start():
	"""Teeme valik kellega mängima
	tagastame m muutja int formaadis
	
	:rtype: int
	"""
	print("kivi, käärid, paber")
	m=3
	while m not in [1,2]:
		try:
			m=int(input("Kellega mängimine?\n1-botid \n2-robotiga"))
		except:
			ValueError
	return m