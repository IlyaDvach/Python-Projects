score = input("Enter Score: ")
s = float(score)
e = "Error"

if s >= 0.9:
	e = 'A'
elif s >=0.8:
	e='B'
elif s >=0.7:
	e='C'
elif s >= 0.6:
	e='D'
elif s < .6:
	e ='F'
else:
	e ="Out of Range"
print (e)
