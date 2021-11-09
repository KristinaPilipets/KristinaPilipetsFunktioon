from keyboard import*
from random import*
def start():
	"""Teeme valik kellega mängima
	tagastame m muutja int formaadis
	
	:rtype: int
	"""
	print("kivi, käärid, paber")
	m=0
	while m not in [1,2]:
		try:
			m=int(input("Kellega mängimine?\n1-botid \n2-inimesega"))
		except:
			ValueError
	return m
def bot_vs_bot(v1:list,v2:list):
	"""robotite mäng 
	Näitame ekraanile võitja nime
	:param list v1: järjend esimese roboti jaoks
	:param list v2: järjend teise roboti jaoks
	
	"""
	while True:
		print("kas mängime? q - välja, enter - mängimine")
		if read_key()=="q":
			break
		elif read_key()=="enter":
			p1=choice(v1)
			print("Esimine bot: ",p1)
			p2=choice(v2)
			print("Teine bot: ",p2)
			if p1==p2:
				print("Viik")
			elif p1==v1[0] and p2==v2[1] or p1==v2[0] or p1==v1[1] and p2==v2[2]:
				print("Võitis 1")
			else:
				print("Võitis 2")
def human_vs_human():
	fair=0
	wina=0
	winans=0
	f=0
	b=""
	c=""
	while True:
		print("kas mängime? q - välja, enter - mängimine")
		if read_key()=="q":
			break
		elif read_key()=="enter":
			print(" Камень >> r","\n","Ножницы >> s","\n","Бумага >> p")
			print("Игрок 1. Выберите камень, ножницы или бумага")
			while True:
				if read_key()=="r":
					ans=1
					break
				elif read_key()=="s":
					ans=2
					break
				elif read_key()=="p":
					ans=3
					break
			print("Игрок 2. Выберите камень, ножницы или бумага")
			print(" Камень >> r","\n","Ножницы >> s","\n","Бумага >> p")
			while True:
				if read_key()=="r":
					a=1
					break
				elif read_key()=="s":
					a=2
					break
				elif read_key()=="p":
					a=3
					break
			if int(a)==1 and int(ans)==1:
				win="ничья"
				fair+=1
				f=0+fair
			elif int(a)==2 and int(ans)==2:
				win="ничья"
				fair+=1
				f=0+fair
			elif int(a)==3 and int(ans)==3:
				win="ничья"
				fair+=1
				f=0+fair
			elif int(a)==1 and int(ans)==2:
				win="Вы проиграли"
				wina+=1
				wa=0+wina
			elif int(a)==1 and int(ans)==3:
				win="Вы победили"
				winans+=1
				wans=0+winans
			elif int(a)==2 and int(ans)==1:
				win="Вы победили"
				winans+=1
				wans=0+winans
			elif int(a)==2 and int(ans)==3:
				win="Вы проиграли"
				wina+=1
				wa=0+wina
			elif int(a)==3 and int(ans)==1:
				win="Вы проиграли"
				wina+=1
				wa=0+wina
			elif int(a)==3 and int(ans)==2:
				win="Вы победили"
				winans+=1
				wans=0+winans
			else:
				print("нет такого варианта")
	
			if int(a)==1:
				b="камень"
			elif int(a)==2:
				b="ножницы"
			elif int(a)==3:
				b="бумага"

			if int(ans)==1:
				c="камень"
			elif int(ans)==2:
				c="ножницы"
			elif int(ans)==3:
				c="бумага"
		
			print(f"игрок 1 выбрал {b}, игрок 2 выбрал {c}")
			print()