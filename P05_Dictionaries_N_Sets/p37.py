FavLang={}
for i in range(4):
    k=input('Enter your name:')
    v=input('Enter your fav lang:')
    FavLang.update({k:v})# input takes in str so no worries😁
print(f'The dict {FavLang}')

# part 2 : testing if we have 2 same keys with unique vales what will happen👇

# observation the one key value pair entered latter the first instance is considered in the final dictionary
# Enter your name:Aman
# Enter your fav lang:Bengali
# Enter your name:Rupesh
# Enter your fav lang:Russian
# Enter your name:Kartik
# Enter your fav lang:Kannada
# Enter your name:Aman
# Enter your fav lang:Punjabbi
# The dict {'Aman': 'Punjabbi', 'Rupesh': 'Russian', 'Kartik': 'Kannada'}


# but if 2 unique keys have same vale no problemo as both will showcase the same val🙅‍♂️🥸