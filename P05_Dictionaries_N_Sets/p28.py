# Dictionary methods
D={
    'key':'value',
    'Aman':'coader',
    'L':[1,2,3,['Aman','IP']],
    'f':3.1415,
    'd':{'a':1,'b':(2,)},
    'w':'VolksWagen',
    69:'Is well respected'
}
# print(D.items())# prints the dictionary contents in a tuple
# print(D.keys())# prints all the keys of the dictionary in a list
# print(D.values)# prints all the values of the dictionary in a list
# D.update({69:'Very much respected',100:'one hundred'})# modify and add new
# print(D.get(69))# llr to indexing but for any thing not present returns None
# D.setdefault(45,'forty five')# give an exisating or new key a default value
# D.clear()# clears the dict
# print(D.copy())# creates a shallow copy of the dict
# print(f'the key removed:{D.pop('w')} and the dict now: {D}')# removes and returns what removed
# print(D.popitem())# removes the last entered key-value pair
# print(dict.fromkeys(['a','b','c','d'],3.1415))# here dict is the dtype not any blank dictionary createa a new dict with keys in the list and the single common value