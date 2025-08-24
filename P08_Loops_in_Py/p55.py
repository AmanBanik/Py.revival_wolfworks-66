# while loop
i=1
while i<12:
    print(i)
    i+=1.3

# Print aman 5 times

i=1
while i<=5:
    print('aman')
    i+=1 


L=['Aman','Sujal',3,1,4,5,3.1415,2.78,{2,9}] # len =9
Z=[1,2,3,4,5,6,7,8,9] # len =9



# print the contents of a list -while loop
a=0
while a<len(L):# 0 to 8 -->True
    print(L[a])
    a+=1
'''Output seen
  a=0...'Aman'
  a=1...'Sujal'
  a=2...3
  a=3...1
  a=4...4
  a=5...5
  a=6...3.1415
  a=7...2.78
  a=8...{2,9}
  a=9...condition breaks the loop stops
'''