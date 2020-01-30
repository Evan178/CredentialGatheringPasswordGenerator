import random
options = ["a","A","b","B","c","C","d","D","e","E","f","F","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","x","z","1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*","(",")"]
userSite = input("Please type the name of the website you are stornig credentials for: ")
userName = input("Please type the Username you would like to use: ")
userNumber = input("Please select a length for your password that is between 5 and 50: ")
userNumber = int(userNumber)
PassString = str()
while len(PassString) < userNumber:
    PassString = PassString + random.choice(options)
if len(PassString) == userNumber:

    print("Your username for ", userSite, " is", userName, " and your password is ", PassString)
