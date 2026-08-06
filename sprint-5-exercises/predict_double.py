def half(value):
    return value / 2 

def double(value):
    return value * 2 

def second(value):
    return value[1]


# predict what double("22") will do

print(double("22"))

# I predict that the function will return "2222", as the * operator is overloaded in python. 
# So that if a number is given, it performs the arithmetic operation, but if a string is given it just repeats
# the string 2 times