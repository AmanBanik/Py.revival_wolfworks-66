X=set({})
X.add(20)
X.add(20.0)# Implicit conversion dtype by py to higher order dtype, here float
X.add('20')
print(X, len(X))
S={}
print(type(S))# empty dictionary, not set

