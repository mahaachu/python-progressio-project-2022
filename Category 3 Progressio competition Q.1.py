
value_of_coins = 1
value_of_notes = 10
def notes_to_coins(T, Z, X):
        T = input("How many test cases do you need to run?:")
        Z = input("How many notes do you have?:")
        X = input("How many coins do you have?:")
        Amount_of_money = Z*10 + X
        No_of_coins = int(Z)*10 + int(X) 
        if (1 <= int(T) <= 1000 and 1 <= int(Z) <= 1000):
            print("You should pay them", No_of_coins,  "coins, if you owe them", Z, "number of notes, and",X, "number of coins.")
        else:
            pass
notes_to_coins(4,5,3)