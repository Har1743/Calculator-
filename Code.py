import re

print ("HELLO\n"
       "Welcome to the dynamic calculator")
print ("\nIf you want to perform calculation enter:\n"
       "EQUATION\n"
       "OTHERWISE quit")

run = True
previous = 0

def calculation():
    global run
    global previous
    equation = ""
    
    if ( previous == 0 ):
        equation = input("Enter the equation")
    else:
        equation = input(str(previous))
    
    if ( equation == 'quit'):
        print("\nThanks for using our calculator")
        run = False
    else:
        equation = re.sub('[a-zA-Z:;""'']', '', equation)
        if ( previous == 0 ):
            previous = eval(equation)
        else:
            previous = eval( str(previous) + equation)

while run:
    calculation()
