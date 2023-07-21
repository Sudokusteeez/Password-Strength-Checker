
import string

password = "Superman4"

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters = [upper_case, lower_case, special, digits]

length = len(password)

score = 0

if length > 8:
    score += 1
if length > 12:
    score += 2
if length > 16:
    score += 3
if length > 20:
    score += 4
print(f"Password length is {str(length)}, adding {str(score)} points!")

if sum(characters) > 1:
    score += 1

if sum(characters) > 2:
    score += 2

if sum(characters) > 3:
    score += 3

print(f"Your password has {str(sum(characters))} different character types, adding {str(sum(characters))} points!")

with open('PW Strength Common .txt', 'r') as f:
    common = f.read().splitlines()

if password in common:
    print("The password is too common, 0 points added here. ")
    exit()

if score < 4: 
    print(f"Your score is: {str(score)} /8, please try again.")
elif score == 4: 
     print(f"Your score is: {str(score)} /8, I think you can find something stronger.")

elif 4 < score < 6: 
     print(f"Your score is: {str(score)} /8, good job!")

elif score > 6: 
     print(f"Your score is: {str(score)} /8, well done!")




