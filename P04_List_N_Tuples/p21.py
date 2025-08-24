# Tuples
T1=()# Empty tuple
T2=(1,2,3,4,5)# Tuple with 5 elements
T3=(1,)# Tuple with 1 element, is mandatory to have a comma
# print(T1)
# print(T2)
# print(T3)
# print(type(T1))
# Methods
print(T2+(6,))# Concatenation of tuples
# T1[0]=6# Tuples are immutable, so we cannot change their elements
print(T1)
t1=('a','a','b','c','d','e','e',1,1,2,2,2,3)
print(t1.count(2))# Count the number of times 2 appears in the tuple
print(t1.index('e'))# Find the index of the first occurrence of 'e'
print(3 in t1)# membership of an element in a tuple