"""
# Ternary operator
is_friend = True
permission = "passed" if is_friend else "failed"
print(is_friend)

# short circuting
is_friend = True
is_user = True
print()


# for Loop
for i in [1,2,3,4,5]:
	for j in ['a','b','c','d']:
		print(i,j)
"""
"""
# iterable can be a list, tuple, dictionary, string,...True

user = {
	'name': 'myname',
	'age': 50,
	'can_swim':False
}

for key ,value in user.items():
	print(key ,value)
for j in user.keys():
	print(j)
for k in user.values():
	print(k)

# create a summer
sum = 0
for i in range (1, 50, 5):
	sum+= i
print(sum)

# range
for _ in range(2):
	print(list(range(10)))

# enumerate
for i, char in enumerate(list(range(10))):
	print(i, char)
	if char == 5:
		print(f'index of 5 is: {i}')
"""

"""
# while Loop 

age = 1
while age <= 11:
	print (f'I am happy that I have {age}  year old')
	age +=  1
"""
"""
# while / break
my_list =  [1,2,3]

for item in [1,2,3]:
	print(item)

i = 0
while i < (len(my_list)):
	print(my_list[i])
	i +=1
"""

"""	
# while loop 2

while True:
	response = input('Enter something: ')
	if(response == 'bye'):
		break
"""
"""
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

fill = '*'
empty = ''

for row in picture:
	for pixel in row:
		if pixel:
			print(fill, end='')
		else:
			print(empty, end = '')
	print('')
"""
"""
# find dupplicate
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
		# count = Return number of occurrences of value
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
"""
"""
# Argument vs parameter
def my_func(name = 'Reza', emoji = ' :)'): # parameter
	print(f' Hi {name} {emoji}')

my_func() # positional Argument
"""

""""
#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

def checkDriverAge():
	age = input("What is your age?: ")
	if int(age) < 18:
		print("Sorry, you are too young to drive this car. Powering off")
	elif int(age) > 18:
		print("Powering On. Enjoy the ride!");
	elif int(age) == 18:
		print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge()
"""
"""
#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.


def checkDriverAge(age):
	if int(age) < 18:
		print("Sorry, you are too young to drive this car. Powering off")
	elif int(age) > 18:
		print("Powering On. Enjoy the ride!");
	elif int(age) == 18:
		print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge(22)
"""
"""

# globalk variable -dependecy injection

total = 0

def count(total):
	total += 1
	return total
print(count(count(count(total))))
"""

"""
# Scope - what variables do I have access to?
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()

#1 - start with local
#2 - Parent local?
#3 - global
#4 - built in python functions
"""



"""
# Decorator Pattern
def my_decorator(func):
	def wrap_func(*args, **kwargs):
		func(*args, **kwargs)
	return wrap_func

@my_decorator
def hello(greeting, emkoji = ':)'):
	print(greeting, emkoji)
hello('Hi')
"""

"""
# Decorator
from time import time

def performance(fn):
	def wrapper(*args, **kwargs):
		t1=time()
		result = fn(*args ,**kwargs)
		t2=time()		
		print(f'took {t2-t1} ms')
		return result
	return wrapper

@performance
def long_time():
	for i in range(1000000):
		i*5

long_time()

"""
"""

user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
	def wrapper(*args, **kwargs):
		if args[0]['valid']:
			return fn(*args, **kwargs)
	return wrapper	
  

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
"""







