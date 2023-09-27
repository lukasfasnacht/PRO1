user_name = input("Wie heisst du?:")
age = int(input("Wie alt bist/wirst du dieses Jahr?:"))
prompt = int(input("Wie oft soll deine Nachricht ausgegeben werden?:"))

def year100(age):
  year = 2023 + (100 - age)
  return year

year = year100(age)

for i in range(prompt):
  print(user_name + ", du wirst im Jahre " + str(year) + " 100 Jahre alt")