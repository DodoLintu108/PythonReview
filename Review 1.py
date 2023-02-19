#FOR GIU STUDNETS. beltawfeek ya gama3a <3

#This is a comment.

""" 
This is a comment
It can multilined
"""

#In python, you dont need a class to run some code. you can run it just like this.
print("\nLine 9 \n")

print("Hello World!") #no more shitty semi-collum! ";"

#In python we dont use { } for if statments, we isntead decrimante under the if statment by one "Press tab"
if 5 > 2:
    print("5 is more than 2!")
    #anything thats under the if statment by one indicrimant is a part of the if statment,
    #If i want to get out of the print stamtnet I just go back to the begging of the line.

#Code here (outisde if statment)

#Now lets say you want to create a variable, in python you do not choose the variable type, instead python figures it out!

#Let's create a variable named X that has the integer 12 in it.
x = 12

#Let's create a variable named Y that has the integer 10 in it.
y = 10

#Let's create a varibale thats called name and has a name in it.
name = "Mersal"

#Let's add x and y in a varible called z.
z = x+y

#Let's create a varibale thats called Q and add the floating point number 32.2 in it.
q = 32.2

#Let's create a variable called charecter and set it to the char value 'c'.
charecter = 'c'

#Let's create a varibale called bool and set it to (True).
bool = True

#Let's create a complex number called complex with the value of 1j.
complex = 1j

#Let's print out z.
print(z)

#let's print out name.
print(name)

#note you cannot start a varible name with a number. for example "2name".

#you can print out the type of the variable in the following way.
print("\nLine 58\n")

print(type(x))
print(type(name))
print(type(q))
print(type(bool))

#Type casting exists in python, lets do a small example:
#Turn x into a floating numeber and print out its type.
print("\nLine 67\n")

x = float (x)
print(type(x))
print(x)


x = str(x)
print(type(x))
print(x)

#this type casting wont work because you can't turn a string into a int or a float.
"""
x = int(x)
print(type(x))
print(x)
"""

#let's focus on strings.

#Slicing 
print("\nLine 88\n")
slicingTest = "Hello, Slice me up!"
print(slicingTest[0:5]) #you can also write [:5]
print(slicingTest[7:19])

#Change to upper or lower case.
a = "Lower Case"
b = "Upper Case"

print("\nLine 97\n")

print(a.upper)
print(b.lower)

#trim up any extra space
c = "I'm writing so much spaces in the end                "
print(c)
print(c.strip)

#A really cool thing to use in python with string is format.
print()

age = 36
txt = "My name is Mersal, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


#Now let's learn functions

print("\nLine 123\n")
def my_function():
  print("Hello from a function")

my_function()


#Now let's learn Classes
print("\nLine 131\n")

class MyClass:
    x = 5

p1 = MyClass()

print(p1.x)