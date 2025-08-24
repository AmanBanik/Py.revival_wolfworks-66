# Typing(adv)

from typing import List,Union,Tuple,Dict

# list of integers

num:List[int] = [1,2,3,4,5,6,7]

# Tuple of string and integer

person: Tuple[str,int] = (23,5,'Aman','B',5)

# Dictionary with str key and int values

d: Dict[str,int] = {'Alice': 18,'Mickey':55}

# Union with multiple types

idf1: Union[int,str] = 'ID123'
idf2 = 12345

print(f'{num} , {person}, {d}, {idf1}, {idf2}')