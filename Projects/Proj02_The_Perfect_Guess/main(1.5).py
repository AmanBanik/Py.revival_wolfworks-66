import random
n = random. randint(1,100)
guesses =0
a=-1
while(a != n):
    guesses +=1
    a = int(input("Guess the number:"))
    if(a >n):
        print("Lower number please")
    else:
        print("Higher number Please")
print(f"You have guessed the number correctly in {guesses} attempt,\nand the number is {n}")
