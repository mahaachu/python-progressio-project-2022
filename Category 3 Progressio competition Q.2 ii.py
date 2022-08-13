T = input("How many test cases are there?: ")
count = 0
X = input("What is the height of Alice?: ")
Y = input("What is the height of Bob?: ")
if (count  <= int(T) and 1 <= int(T) <= 1000):
     X = input("What is the height of Alice?: ")
     Y = input("What is the height of Bob?: ")
else:
    pass
if (100 <= int(X) and 200 <= int(Y)  and int(X) != int(Y)):
    print("A")
    count += 1
else:
    print("B") 
    count += 1


