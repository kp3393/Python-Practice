#implementing Identity operator
# is --> Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.
# is not --> Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.
#declaring variables
x1=5
y1=5
x2=8
y2=8
string1="Hello world"
string2="hello World"

#Identity operator
print(x1 is x2)
print(x1 is y1)
print(y1 is y2)
print(string1 is string2)
print(string1 is not string2)