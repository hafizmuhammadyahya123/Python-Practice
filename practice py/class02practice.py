# variables
my_num_1 = 22
my_num_2 = 10
print(f"this number is equal to {my_num_1}and{my_num_2} ")

# additional stuff
# 1. id() method
# 2. type() method

print(type(my_num_1))
print(id(my_num_1))
print((id(my_num_2)))

# PEMDAS RULE

print(((2*3)**3)*2) #eq----A
# solve eq----A
# print((2*3)) = 6
# print(6**3) = 216
# print(216*2)

print((2+3)+((2*3)**2)) #eq----B
# solve eq----B
print(2 + 3) #step 1
print(2 * 3) #step 2
print((2*3)**2) #step 3
print((5)+(6)**2) #step 4

print(1 + (2+4) * (2*2) ** (2 / 4 ) - 1) #eq----C
# solve eq----C
print(2 + 4) #6  step1
print(2 * 2) #4  step2
print(2 / 4) #0.5 step3
print(4 ** 0.5) #2.0 step4
print(6 * 2.0) #12.0 step5
print(1 + 12.0) #13.0 step6
print(13.0 -1) #12.0 step7

# OPERATORS:-
# ADVANCE OPERATORS / AUGMENT STATEMENT:-
# +=, -=, /=, *=

x = 10
x += 20
print(x)

x = 20
x -= 10
print(x)

y = 50
y *= 2
print(y)

z = 40
z /= 2
print(20)

int = 40
int //= 3
print(int)

int_a = 30
int_b = 40
int_a %= 2
int_b %= 3
print(f"Reminder__Respectively = {int_a} , {int_b}")

# comparison operators
NumberOne = 100
NumberTwo = 10

print(NumberOne == NumberTwo) #False
print(NumberOne == NumberOne) #True
print(NumberOne > NumberTwo) #True
print(NumberOne > NumberOne) #False
print(NumberOne <= NumberOne) #True
print(NumberOne >= NumberTwo) #True

# LOGICAL OPERATORS
# most usefull 1.and, 2.or, 3.not
print(f"True and True = {NumberOne == NumberOne and NumberOne >= NumberTwo}.") #True
print(f"True and False = {NumberTwo < NumberOne and NumberOne == NumberTwo}.") #False
print(f"True and True = {NumberOne > NumberTwo and NumberTwo < NumberOne}.")  #True
print(f"False or True = {NumberOne == NumberTwo or NumberTwo == NumberTwo}.") #True
print(f"TRue or True = {NumberOne >= NumberTwo or NumberOne <= NumberOne}.")  #True
print(f"False or False = {NumberOne < NumberTwo or NumberTwo > NumberOne}.") #False
print(f"Actual_value_is_True_but_show--->{not NumberOne > NumberTwo}.") #False


# Concatenating text strings:-
# there are three methods

MyString1 = 'hello'
MyString2 = 'programmers'

#using method1 + operator  
print(MyString1 + MyString2) # helloprogrammers
print(MyString1+MyString2) # helloprogrammers

print(MyString1 +' '+ MyString2) # hello programmers
print(MyString1+' '+MyString2) # hello programmers

# using method2 f"this is {var1}{var2}..."
print(f"{MyString1}{MyString2}") #helloprogrammers

print(f"{MyString1} {MyString2}") #hello hello

print(f"{MyString1}All{MyString2}") #helloAllprogrammers

print(f"hi{MyString1}{MyString2}") #hihelloprogrammers


# using method3 "{index}{index}...".format("str1","str2",...)
# OR...
# using method3 "{index}{index}...".format(var1,var2,...)

print("{0}{1}".format(MyString1,MyString2)) #helloprogrammers

print("{0} {1}".format(MyString1,MyString2)) #hello programmers

print("{1} {0}".format(MyString1,MyString2)) #programmers hello

print("{0}{1}{2}{3}{4}".format(MyString1,'how','are','you',MyString2)) #hellohowareyouprogrammers

print("{4} {1} {2} {3} {0}".format(MyString1,'programmers','are','you','busy',MyString2)) # busy programmers are you hello

