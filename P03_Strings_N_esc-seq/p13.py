Name='NORMAN'#A string... immutable
print(len(Name))#to obtain the number of characters in the string
#indexing
#to obtain R
print(Name[2])
#to obtain R from end
print(Name[-4])
#slicing
#to obtain NOR
print(Name[0:3])#ending index is always excluded
#to obtain NORM
print(Name[0:4])
#to obtain NOR lefty
print(Name[-7:-3])

print(Name[:])#all char
print(Name[2:])#from idx 2 till end
print(Name[:4])#right from start till idx 3
#skiping or adding steps
Alp="abcdefghijklmnopqrstuvwxyz"
print(Alp[1:17:3])#otp{s1(idx 1 to 16):bcdefghijklmnopq , s2(step of 3): b e h k n q} > behknq