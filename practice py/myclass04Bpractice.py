country_0 = 'Australia'
country_1 = 'Japan'
country_2 = 'Canada'
country_3 = 'Newzeland'
country_4 = 'Korea'
country_5 = 'China'

print('address = ',id(country_0) , 'address = ' , id(country_3))
print(type(country_1))

# -------------------------------------Topic: List--------------------------------------------
# Managing colection of values
# Slower
# Solution: Data Structure for collection of values: List

list_countries = ['Australia' , 'Japan' , 'Canada' , 'Newzeland' , 'Korea' , 'China']
print(type(list_countries) , id(list_countries))

#1. List are mutable
#2. Multiple data types are store.
#3. Nested List.


# Task: Applying Methods List
# Python has a set of built-in methods that you can use on lists.

list_countries.append('Switzerland')  #Adds an element at the end of the list
print(list_countries)

list_countries.extend(['Italy' , 'London' , 'Turkey'])#Add the elements of a list (or any iterable), to the end of the current list
print(list_countries)

list_countries.insert(2 , 'Kuwait')#Adds an element at the specified position
print(list_countries)

print(list_countries.index('Switzerland')) #Returns the index of the first element with the specified value

                                                               
print('London index Number = ',list_countries.index('London' , 5 , 10)) #list.index(elmnt , start , end)
                                                                                              #Optional 
list_countries.pop(6) #Removes the element at the specified position
print(list_countries)

list_countries.pop(-1)
print(list_countries)

list_countries.reverse() #Reverses the order of the list / important
print(list_countries)

list_countries.sort() #Sorts the list
print(list_countries)

list_countries.remove('Kuwait') #Removes the item with the specified value
print(list_countries)

list_countries.clear()
print(list_countries)

list_countries.count('Kuwait')
print(list_countries)

#copy() = Shallow copy -----------------------------------------------------

list1 = ['London', 'Italy', 'Switzerland', 'Korea', 'Newzeland', 'Canada']
list2 = list1.copy()
print(f'{id(list1)}-- Diff B/W --{id(list2)}') #. keep values at different address
                                               #. Changing values in one collection doesn't effect other  

list2.append('USA')
print(f'{list1}\n{list2}')#Copy main change aaya means memory main diff address pr store thi list2
print(f'{id(list1)} ---Diff/BW--- {id(list2)}')

list2.insert(1 , 'Africa')
print(f'{list1}\n{list2}')
print(f'{id(list1) , id(list2)}') #(2067457179520, 2067456636096) address tuple main pass kiya 

# OR 
import copy as cp
a = [1 , 2 , 3]
b = [10 , 20 , 30]

c = cp.copy(b)

print(id(c) , id(b))
print(c , b)

b.append('Q')
print(b)
print(c)

c.append('hello')
print(c)
print(b)

d = [a , b , c]
print(d)

e = cp.copy(d)
print(f'{e} Address = {id(e)}')
print(f'{d} Address = {id(d)}')

d[0][1] = 11
print(d,id(d))
print(e,id(e))

d.insert(2 , 'Pytorch')
print(d)
print(e)

e[1][3] = 100
print(id(e) , id(d))
print(f'{e}\n{d}')

# Task:
# Implement Deep copy concept on list (H.W)
# Adding values at different index without  'insert()' method
import copy
nested_list = [100 , 200 , 300 , [1000 , 5000 , 110000]]

deep_copy = copy.deepcopy(nested_list) 
print(id(deep_copy) , id(nested_list))
print(deep_copy)
print(nested_list)

nested_list.append(100000)
print(nested_list)
print(deep_copy)

nested_list[3][0] = 4000
print(deep_copy)
print(nested_list)

nested_list.append(100000)
print(nested_list)
print(deep_copy)

a = [10 , 20 , 30]
b = [40 , 50 , 60]
c = [a , b]

d = copy.deepcopy(c)
print(c , id(c))
print(d , id(d))

c.append(70)
print(c , id(c))
print(d , id(d))

# Adding values at different index without  'insert()' method
cities = ['Australia' , 'Japan' , 'Canada' , 'Newzeland' , 'Korea' , 'China']
print(cities)

cities[0] = 'Qatar'
print(cities)

new_cities = cities
new_cities.append('Kuwait')

print(new_cities , id(new_cities))
print(cities , id(cities))

# List Slicing
cities = ['Australia' , 'Japan' , 'Canada' , 'Newzeland' , 'Korea' , 'China']
print(cities[:4]) # index 4 not include
print(cities[0:2]) # index 2 not include
print(cities[3:6]) 
print(cities[0:]) #index 0 to n
print(cities[:6]) #index 0 to 5
print(cities[:-1]) #last index not include
print(cities[-3:]) #last 3 
print(cities[-3:-1]) #last 2

# Reverse Slicing for list
l = ['A','B','C','D','E','F','G']
print(l[::-1]) #important

# Task: Create a student list of names and apply all methods that we learn today
StudentList = ['John' , 27 , 59.99 , {'Present':True} , 'Andrew' , 30 , 71.22 , {'Present':[True]}]
print(StudentList)

StudentList.append({'Program':['DATA SCI']})
print(StudentList)

StudentList.extend([{'Start':2024} , {'subject':6}])
print(StudentList)
# -----------------------------
StudentList.remove('John')  
print(StudentList)
# similarly
del StudentList[1]
print(StudentList)
# -----------------------------
StudentList.insert(0 , 'Mike Hertz')
print(StudentList)

print(StudentList.count({'Present':True})) #1

print(f'Index_No# {StudentList.index({'Present':True})}')  # Index_No# 3
print(f'Index_No# {StudentList.index({'Present':[True]})}') # Index_No# 7
print(f'Index_No# {StudentList.index({'subject':6})}') # Index_No# 10

StudentList.pop(9) #Remove and return item at index (default last).
print(StudentList) #Raises IndexError if list is empty or index is out of range

StudentList.reverse()
print(StudentList)

# copy() Shallow Copy---------------------------------------------------------  
ShallowCopy = StudentList.copy()

print(id(ShallowCopy))
print(id(StudentList))

StudentList.insert(0 , 'Andrew NG')
print(StudentList)
print(ShallowCopy)

ShallowCopy.insert(0 , 'Founder of Deep Learning.')
print(ShallowCopy)
# -----------------------OR---------------------------------------------------
import copy as cp
shallow_copy = cp.copy(ShallowCopy)

print(f'Address For First Shallow Copy ={id(shallow_copy)}\n' f'Address For Second Shallow Copy ={id(ShallowCopy)}')
print(shallow_copy)
print(ShallowCopy)

ShallowCopy.append('Py')
print(ShallowCopy)
print(shallow_copy)

shallow_copy.append('C#')
print(shallow_copy)
print(ShallowCopy)

# DeepCopy
import copy 
l =  ['Founder of Deep Learning.', {'subject': 6}, {'Program': ['DATA SCI']}]
d = copy.deepcopy(l)

print(d , id(d)) #adderss=1287234792128
print(l , id(l)) #address=1287234791424

d[0] = 1421
print('ADDRESS=',id(d),d)
print('ADDRESS=',id(l),l)

l[1] = -3E14
print(l)
print(d)

d[1] = 4e2  
print(d)
print(l)
# ---------------------------------------------------------------
# Practice
list = ['a' , 'b' , 'c' , 'd' , 'e']
list.append('f')
print(list)

list.extend(['x' , 'y' , 'z'])
print(list)

print(list.count('x'))

list.reverse()  #important
print(list)

print(list.index('y'))

list.insert(1 , 'Q')
print(list)

list.remove('x')
print(list)  

list.sort()
print(list)

list.pop(1)
print(list)

ListCopy = list.copy()
print(ListCopy)
print(id(ListCopy) , id(list))

ListCopy.insert(1 , 'a')
print(ListCopy)