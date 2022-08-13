
name = input("Hello! What is your name? ")
consent = input("Welcome to this adventure! Would you like to play? ")
if consent.lower() == "yes" or consent.lower() == "yeah" or consent.lower() == "okay":
    print("Great! Let's get into the game!")
else:
    print("Alright, have a nice day!")
    quit()
answer1 = input("You're traveling to the library which is located around 800m away from your house. Would you rather walk there, or go by car?" )
if answer1.lower() == "walk":
    print("Good job! You've chosen a healthy and environmental friendly option of transport! Keep going?")
if answer1.lower() == "car":
    print("A more eco-friendly method would be much better! Let's move on to the next one.")
answer2 = input("At the library, you notice, that there is small pop-up stand selling samosas and drinks. They give you an option to choose between having your snack delivered on a free polyester plate or a metal plate for 0.50 cents. Which option would you choose?")
if answer2.lower() == "metal":
    print("That's a nice thing to do! Keep going!!")
else:
    print("Oh :( While i do understand you would wish to save some money, isn't it nice to do something for the earth once in a while? Polyester is completely non-biodegradable!")
answer3 = input("You've found all the books you wanted to read. It's time to borrow! Would you opt for a digital e-receipt or a physical paper receipt at the borrowing kiosk?")
if answer3.lower() == "e-receipt" or answer3 == "ereceipt" or answer3 == "digital receipt":
    print("That's great!! You've saved paper by opting for this option..!")
    print("Oh look! It's your lucky day..the library is giving away free goodies to those who opted for e-receipts..! a good gesture is never wasted, my friend :))")
else:
    print("Oh :( keep in mind that printing paper receipts contributes to the emission of CO2...!")
answer4 = input("You decide to leave the library after a while. You find that you have ordered too much, and still have some drinks leftover.Would you, on the way home, travel a little more to dispose your drink in a recyclable bin? Or use the all-waste bin provided at the library?")
if answer4.lower() == "recyclable bin" or answer4.lower() == "recyclable":
    print("Good job! Proud of you!")
else:
    print("A little kindness goes a long way! Please think over this!")
print("Thank you for playing," , name, "!")
consent2 = input("Do you want to play a quiz next? ")
if consent2.lower() == "yes" or consent2.lower() == "yeah" or consent2.lower() == "okay":
    print("Hi, welcome to the climate and environment quiz!")
score = 0
play_again = 0
if play_again <100:
    print("Let's begin with some truth/false questions to start...")
answer1 = input("Natural disasters in 2021 cost the United States more than $200 billion. True or false? ")
if answer1.lower() == "true":
    print("correct! keep going!")
    score += 1
else:
    print("Nope! but keep going! you can do it!")
answer2 = input("The weight of annual plastic waste production across the globe is nearly equivalent to that of the entire human population. True or false? ")
if answer2.lower() == "true":
    print("correct! fantastic!")
    score += 1
else:
    print("Nope! but keep going! on to the next one!")
answer3 = input("Approximately 80% of the world's wastewater flows back into the ecosystem without being treated or reused. True or false? ")
if answer3.lower() == "true":
    print("that is incorrect! about 80% of watewater goes untreated! That's too large of a number, don't you think?")
    print("You got", str(score), "questions correct!")
else:
    print("correct! good going!")
    score += 1
    print("You got", str(score), "questions correct!")

