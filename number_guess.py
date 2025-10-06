import random
print("-------------- WELCOME TO NUMBER GUESSING GAME -----------")

trials = 0

def guess(n):
    global trials
    while True:
        try:
            a = int(input("Enter a number: "))
            trials = trials + 1
            if a > n:
                print("Too high! Try a smaller number.\n")
            elif a < n:
                print("Too low! Try a bigger number.\n")
            else:
                print("CONGRATULATIONS !! You did it in ", trials, " trials")
                print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                break
        except:
            print("Code is executing error")

print()
print("1 - Easy (Guess between 1-20)")
print("2 - Medium (Guess between 1-50)")
print("3 - Hard (Guess between 1-100)")
print()

k = int(input("Choose Your Difficulty: "))

if k == 1:
    n = random.randint(1, 20)
    guess(n)
elif k == 2:
    n = random.randint(1, 50)
    guess(n)
else:
    n = random.randint(1, 100)
    guess(n)
