zahl = float(input("Welche Zahl möchtest du auf gerade/ungerade überprüfen?:"))

def is_even(zahl):
  if zahl % 2 == 0:
    return True
  else:
    return False

if is_even(zahl):
  print(f"{zahl} ist eine gerade Zahl.")
else:
  print(f"{zahl} ist eine ungerade Zahl.")