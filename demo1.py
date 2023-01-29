# s= {1, 1, 1, 2, 3, 4};
# print(s)
# ss= set()
# ss.add(1)
# ss.add(2)
# ss.add(1)
# ss.add(4)
# ss.add("sjs")
# print(ss)



# l= [1, 1, 2, "1, 2", {1 , 2, 1, "kilo"}, ("hi", 88, True), True]
# print

# def power(x, y):
# 	n= 1
# 	for i in range(y):
# 		n= n*x
# 	return n 


# def exponentiation(x, y):
# 	if(y==1):
# 		return x
# 	elif(y==0):
# 		return 1
# 	elif(y%2==1):
# 		return exponentiation(x*x, y/2)*x 
# 	else:
# 		return exponentiation(x*x, y/2)

# print(power(2, 4))
# print(exponentiation(2, 8))

def checker(k):
	if k>2: 
		return True
	return False

def somefuntion(k):
	kk= tuple(
		for i in k
		if i>1
	)
	return kk

def somefuntion1(k):
	kk= tuple(
		checker(current)  #the returned value from the funtion is added to the tuple, not value in k
		for current in k  	# the above funtion is called for each current in k list
	)
	return kk

# l1= [1, 2, 3, 4, 5, 6, 0, -1, "silly"] gives error when this list is passed as argument
l1= [1, 2, 3, 4, 5, 6, 0, -1]
kk = somefuntion(l1)
print(kk)

kk = somefuntion1(l1)
print(kk)

class myclass:
	def __init__(self, x):
		self.x= x

	type ="integer" #nothing special , just myclass now has a new attribute
	

obj1= myclass(7)
print(obj1.x)
print(obj1.type)




