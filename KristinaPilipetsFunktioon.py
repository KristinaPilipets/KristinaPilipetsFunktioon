from random import*
from keyboard import*
from ourmodul import*
v1=["Kivi","Käärid","Paber"]
v2=["Kivi","Käärid","Paber"]

m=start()
if m==1:
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
if m==2:
	while 1:
		pass
