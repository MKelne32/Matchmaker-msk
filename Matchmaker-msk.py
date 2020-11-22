# Mathew Kelne
# Match Maker

print("You will be asked a series of questions")
print("Please respond with a 1-5, 1 being strongly disagree, and 5 being strongly agree")
print("Please answer honestly")

print("MatchMaker")

#Question 1
userResponce1 = int(input("Modifying cars is a fun passion? "))
while userResponce1 > 5 or userResponce1 < 1:
    print("Whoops! Make sure your responce is between 1-5!")
    userResponce1 = int(input("Modifying cars is a fun passion? "))
    break
if userResponce1 >= 1 and userResponce1 <= 5:
    desiredAnswer1 = 5
    compatibility1 = 5 - abs(userResponce1 - desiredAnswer1)
    print("Question 1 compatability: " + str(compatibility1))
    print(" ")

#Question 2
userResponce2 = int(input("Miatas are the best sports car ever! "))
while userResponce2 > 5 or userResponce2 < 1:
    print("Whoops! Make sure your responce is between 1-5!")
    userResponce2 = int(input("Miatas are the best sports car ever! "))
    break
if userResponce2 >= 1 and userResponce2 <= 5:
    desiredAnswer2 = 5
    compatibility2 = 5 - abs(userResponce2 - desiredAnswer2)
    print("Question 2 compatability: " + str(compatibility2))
    print(" ")

#Question 3
userResponce3 = int(input("Mustangs are cool cars! "))
while userResponce3 > 5 or userResponce3 < 1:
    print("Whoops! Make sure your responce is between 1-5!")
    userResponce3 = int(input("Mustangs are cool cars! "))
    break
if userResponce3 >= 1 and userResponce3 <= 5:
    desiredAnswer3 = 1
    compatibility3 = 5 - abs(userResponce3 - desiredAnswer3)
    print("Question 3 compatability: " + str(compatibility3))
    print(" ")

#Question 4
userResponce4 = int(input("JDM is always the way to go! "))
while userResponce4 > 5 or userResponce4 < 1:
    print("Whoops! Make sure your responce is between 1-5!")
    userResponce4 = int(input("JDM is always the way to go! "))
    break
if userResponce4 >= 1 and userResponce4 <= 5:
    desiredAnswer4 = 5
    compatibility4 = 5 - abs(userResponce4 - desiredAnswer4)
    print("Question 4 compatability: " + str(compatibility4))
    print(" ")

#Question 5
userResponce5 = int(input("Drifting is the most fun you can have with a car! "))
while userResponce5 > 5 or userResponce5 < 1:
    print("Whoops! Make sure your responce is between 1-5!")
    userResponce5 = int(input("Drifting is the most fun you can have with a car! "))
    break
if userResponce5 >= 1 and userResponce5 <= 5:
    desiredAnswer5 = 5
    compatibility5 = 5 - abs(userResponce5 - desiredAnswer5)
    print("Question 5 compatability: " + str(compatibility5))
    print(" ")

#Calculate total compatibility
totalCompatibility = (compatibility1 + compatibility2 + compatibility3 + compatibility4 + compatibility5) * 10
print("Total compatability: " + str(totalCompatibility))

#Output final decision
if totalCompatibility >= 200:
    print("Wow! We are a match!")

if totalCompatibility >= 150 and totalCompatibility < 200:
    print("I don't think we will work, we can still be friends though!")

if totalCompatibility < 150:
    print("Sorry, we were not meant to be...")