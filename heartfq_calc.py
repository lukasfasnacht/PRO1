def freq(age):
  frequency = 220 - age
  return frequency

age = int(input("Geben Sie ihr Alter ein:"))

result = freq(age)

print("Ihre maximale Herzfrequenz mit " + str(age) + " Jahren ist: " + str(result) + "hz")