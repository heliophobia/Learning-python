def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
    
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b
    
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b
    
print "Let's do some math with just functions!"

age = float(raw_input("how old are you? \n"))
height = float(raw_input("how tall are you? \n"))
weight = float(raw_input("what do you wheigh? \n"))
iq = float(raw_input("how smart are you? \n"))

print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"