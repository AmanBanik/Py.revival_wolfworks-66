#str func cont
#lower or upper
a='aman'
b='BANIK'
print(a.upper(), b.lower())
#strip
c='####aman##banik###'
print(c.strip('#'))
#Replace
d='Donald Trump'
print(d.replace('Donald','Doland'))
#split
e='eni meni mini moe'
print(e.split(' ', 2))
#join
f=['any','body','can','dance']
print('&&'.join(f))
#find/index
g='helo world'
print(g.find('world'))
#is digit alpha alpha num
h='1256'
print(h.isdigit())
i='abcd'
print(i.isalpha())
j='45ab'
print(j.isalnum())