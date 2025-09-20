# sets
# sets are mutable
# distinct/unique object
sets = {'a' , 'b' , 1 , 2E2}
print(sets)
print(type(sets))

a , b = {'a' , 'b' , 'c'} , {'d' , 'e' , 'a'}
print(a.intersection(b)) 

print(a.difference(b))

a , b = {'a' , 'p' , 'l' , 'e'} , {'a' , 'p' , 'l' , 'e'}
print(a.issubset(b))

a , b = {2e2 , 31e9 , 221e2} , {2e3 , 3e2 , -221e1}

a.discard(2e2)
b.add('O')

print(a , b)

a.add(101)
print(a)

print(b.pop())

b.remove(3e2)
print(b)

print(b.union(a))

a.update(b)
print(a)

fruits = {'kiwi' , 'apple' , 'banana' , 'orange'}
fruits.add('cherry')
print(fruits)
# -----------------------------------------------------------
fruits.update({'Guava'})
print(fruits)

CS1 , CS2 = {"Google" , "Microsoft"} , {"Open AI" , "Amazon"}
CS1.update(CS2)
print(CS1)

CS3 , CS4 = {100 , 2 , 4} , {100 , 10001 , 100001}
print(CS3.intersection(CS4))

AI , types = {'ML' , 'DL'} , {'SL' , 'USL' , 'SSL' , 'RL' , 'ANN'}
print(AI.union(types))

# ==============================================================
my_set = {'a' , 'b'}
MySet = {'c' , 'd'}
no_common = my_set.intersection(MySet)
print(no_common)

my_set , Set = {1 , 2 , 3} , {1 , 'b' , 3}
print(my_set.intersection(Set))



