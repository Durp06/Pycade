import random
#def print_thing():
high = input("What is the highest number you would like?")
low = input("What is the lowest number you would like?")

high= int(high)
low = int(low)

ret = random.randint(low, high)
print(ret)

#print_thing()