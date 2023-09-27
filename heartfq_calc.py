def freq(age):
  frequency = 220 - age
  return frequency

user_input = int(input("Geben Sie ihr Alter ein:"))

result = freq(user_input)

print("Ihre maximale Herzfrequenz mit " + str(user_input) + " Jahren ist: " + str(result) + "hz")