print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = name1 + name2
lower_names = names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_words = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")

second_words = l + o + v + e

adding_names = int(str(first_words) + str(second_words))

if adding_names < (10) or adding_names > (90):
 print(f"Your score is {adding_names}, you go together like coke and mentos.")
elif adding_names > (40) and adding_names < (50):
  print(f"Your score is {adding_names}, you are alright together.") 
else:
  print(f"Your score is {adding_names}.")
  