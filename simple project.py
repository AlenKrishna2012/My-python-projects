def take_input():
	a=int(input(' enter num1:\n'))
	b=int(input(' enter num2:\n'))
	c=input(' enter operation symbol(eg"+","-","*","/":\n')
	return a,b,c
	
a,b,c =take_input()
	
def subtraction():
	d =a-b
	return d;
    
def addition():
	e =a+b
	return e;
    
def multiplication():
	f =a-b
	return f;
    
def division():
    g =a/b
    return g;
    

if (c == '+') :print(addition());
elif(c == '-') :print(subtraction());
elif(c == '*') :print(multiplication());
elif(c == '/') :print(division());
