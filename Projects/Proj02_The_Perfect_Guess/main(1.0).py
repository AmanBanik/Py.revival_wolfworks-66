import random
n = random. randint(1,100)
a=-1
guesses =1
while(a != n):
    a = int(input("Guess the number:"))
    if(a > n):
        print("Lower number please")
        guesses +=1
    elif(a < n):
        print("Higher number Please")
        guesses +=1
print(f"You have guessed the number correctly in {guesses} attempt,\nand the number is {n}")
