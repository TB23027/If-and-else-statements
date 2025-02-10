secret = ("James Bond")
guess = input("Guess what the secret name is if you wish to enter:")
if guess == secret:
    print("You may enter")
else:
    print("Remove thy self from these premises")

age_1 = int(input("How old are you:"))
if age_1 == 15:
    print("You are allowed to enter")
else:
    print("You are not 15, you cannot enter")

age_2 = int(input("How old are you:"))
if age_2 >= 18:
    print("You are allowed to enter the movie, Enjoy!")
else:
    print("You cannot enter, 18+ only")

num = int(input("Enter a number: "))
if num % 2 == 0:
    print (f"{num} is even.")
else:
    print (f"{num} is odd.")

point = int(input("Enter your final test score:"))
if point >= 71:
    print("You got excellence, well done!")
elif point >= 51 and point <= 70:
    print("You got Merit, good job!")
elif point >= 31 and point <= 50:
    print("You got achieved, try a little harder but well done.")
else:
    print("You got not achieved. Detention!")

for num in range(1, 101):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
