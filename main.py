print("Check what tools to use based on your month")
month = int(input("Enter your month: "))

if month == 1:
    print("Use coddy.tech and w3schools")
elif month == 2:
    print("Use codedex and programiz")
elif month == 3:
    print("Use brocode and exercism:")
elif month == 4:
    print("Use codewars and chatgpt")
elif month == 5:
    print("Use github and realpython and programming with mosh")
elif month == 6:
    print("Use boot.dev and w3schools")
elif month == 7:
    print("Datacamp and realpython and brocode")
elif month == 8:
    print("Use leetcode and automate the boring stuff with python")
elif month == 9:
    print("Use freecodecamp and corey schafer")
elif month == 10:
    print("Use Kaggle and scikit-learn")
elif month == 11:
    print("Use fastapi and realpython")
elif month == 12:
    print("build a fullstack app or website!")
else:
    print("Sorry wrong month?")

if month <= 12:
    print("Thanks for using my tool!")
