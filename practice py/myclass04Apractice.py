city_0 = "Atlanta"
city_1 = "Los Angles"
city_2 = "china"
city_3 = "california"
city_4 = "Japan"

print(type(city_0)) #<class 'str'>

address = id(city_0) #Memory kmain kahan store ha ye var/str
print(type(address)  , 'address = ' , address) # <class 'int'> address =  1730215655152

# ------------------------------------------------------------------------------------------
#                                            Topic: list
# managing collection of values
# slower
# solution : Data Structure for collection of values : List

list_cities = ["Atlanta",  "Los Angles", "china", "california", "Japan"]
print(list_cities)

#. All cities name aik hi address pr aik hi var main store hain list k through.Manage krna easy ha 
print(type(list_cities) , 'Address=' , id(list_cities)) #<class 'list'> 2879876128960

list_cities.append('Karachi') #Append object to the end of the list.
print(list_cities)

list_cities.extend(['USA' , 'Paris' , 'Germani' , 'USA']) #Extend list by appending elements from the iterable.
print(list_cities)

list_cities.insert(1 , 'Lahore') #Insert object before index.
print(list_cities)

list_cities.sort() #Sort the list in ascending order and return None.
print(list_cities)

list_cities.reverse() 
print(list_cities)

print('index =',list_cities.index('USA'))
print(list_cities)

list_cities.pop(2) #Remove and return item at index (default last).
print(list_cities)

list_cities.remove('Atlanta') #Remove first occurrence of value.
print(list_cities)

# Shallow Copy..
# DIFFERENCE BETWEEN list_cities and cities_new
# 1. list_cities ki copy cities_new ha but address diff ha 
# means jo copy ki wo diff memory main diff address pr store.
# 2. list_cities ki copy cities_new ha append kiya but original main japan nahi aaya last main 

cities_new = list_cities.copy() #Return a shallow copy of the list.
print('DATA TYPE =' , type(cities_new) , '\nADDRESS =' , id(cities_new))
# Diff Between..
print('DATA TYPE =' , type(list_cities) , '\nADDRESS =' , id(list_cities))

cities_new.append('Japan')
print(cities_new)
# Diff Between..
print(list_cities)

list1 = [1,3,5,[10,20,30]]
list2 = list1
list2 = list1.copy()
print(f"ADDRESS = {id(list2)}")
print(f"ADDRESS = {id(list1)}")

list2.append(1001)
print(list2)
print(list1)

list2.extend(['s','h','a','l','l'])
print(list2)
print(list1)

# Deep Copy..
# Opposite ha Shallow copy K.
import copy 
list3 = copy.deepcopy(list2)

list3[3][1] = 1500
print(f"{list3}\nADDRESS ={id(list3)}..")

print(f"{list2}\nADDRESS ={id(list2)}..")

# --------------------------------Again PRACTICE In Above-----------------------------------------

list = ["Atlanta" , "Los Angles" , "china" ,  "california" , "Japan"]
print(list)

print(type(list), id(list))

list.append("Australia") #append(argument) argument last main add huwa list k last main
print(list)

print(list.count("china" ))

list.extend(["Islamabad", "Quetta"])
print(list)

list.insert(1, "Peshawar") #index one pr peshawar aagya ab
print(list)

list1 = list.copy()  #Return a shallow copy of the list.
print('shallow copy of a list is',list1)

list1.remove("Peshawar") #Remove first occurrence of value. Raises ValueError if the value is not present
print(list1)

list.reverse()
print(list)

list.sort()
print(list)

# Shallow / Deep Copy

city_0 = "Anlanta"
city_1 = "Los Angles"
city_2 = "china"
city_3 = "california"
city_4 = "Japan"

list_new = list.copy()
print('list var ki copy bna kr list_new naam k var main store kiya',list_new)

print(type(list_new), id(list_new))

print(id(list))

# Keep values at differnt address as show above
# Changing values in one collection does'nt effect
list_new.append("Karachi")
print(list_new)

# Task
# Implement Deep copy concept on list (HOME.WORK)
# Adding Values at different index with method (C.Work)

list[0] = "Hyderabad" # Over ride
print(list)

list_new = list  # Deep copy

list_new.append("maxico")
print(list_new)

#--------------------------------------------------------------------------------------------------  

# Slicing on list
slicing = list[2:5] #index 5 not included
print(slicing) 

slicing = list[2:]
print(slicing)

rever = slicing[::-1]
print(rever)

# Task :
# create a student list of names and apply all methods that we learn today

students = ["HAMID","AHMAD","UMER","HAMMAD","IMTIAZ"].count("UMER")
print(students)

students = ["HAMID","AHMAD","UMER","HAMMAD","IMTIAZ"].pop(4) # index 4 pr jo ha wo dikhaya
print(students)

students = ["HAMID","AHMAD","UMER","HAMMAD","IMTIAZ"].index("UMER")
print(students)

list_multiple_data_types = ["Qasim", 26,"Male",]
print(list_multiple_data_types)

del list_multiple_data_types[1] # del delete elements
print(list_multiple_data_types)

# Tuples   are immutable
list_multiple_data_types.append("Qasim")
print(list_multiple_data_types)

set = set(list_multiple_data_types)
print(set)

tuple = tuple(list_multiple_data_types) 
print(tuple) 

tuple = list_multiple_data_types[1]
print(tuple)

# list are mutable
# set are mutable
# str are immutable
# tuple are immutable
# -------------------------------------------------------------------------------------------------

# Set
set_a = {'a', 'b'}
set_b = {'c', 'd'}
universal_set = {'a','b','c','d'}

universal_set.intersection(set_a)
print(universal_set)

universal_set.update('e')
print(universal_set)

universal_set.update([21])
print(universal_set)

# Task :
# 1. Create a student tuple of names and apply all methods that we learn today
# 2. Create a student set of names and apply all methods that we learn today

# 1.

students_names_store_tuple = ("HAMID","AHMAD","UMER","HAMMAD","IMTIAZ").count("HAMID")
print(students_names_store_tuple)

students_names_store_tuple = ("HAMID","AHMAD","UMER","HAMMAD","IMTIAZ").index("AHMAD")
print(students_names_store_tuple)

students_names_store_set_a = {"HAMAD", "IMTIAZ"}
students_names_store_set = {"HAMID","AHMAD","UMER","HAMMAD","IMTIAZ"}
students_names_store_set.intersection(students_names_store_set_a)
print(students_names_store_set)