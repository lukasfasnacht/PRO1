# Defines function
def triangle(side):
  result = side * 3
  return result

# Take user inputs and stores it in variable
side = float(input ("Wie lang ist die Seite des Gleichseitigen Dreiecks (in cm)?:"))

# Returns function with user input
result = triangle(side)

# Prints results
print("Das Dreieck hat einen Umfang von " + str(result) + "cm")