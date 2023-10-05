# Erstellt eine leere Liste, welche wir mit Noten füllen
grades = []

# Definiert wie viele Noten eingegeben werden können
number_grades = int(input("Wie viele Noten möchtest du eingeben?:"))
number = number_grades + 1

# Führt die Inputs aus und checkt, ob der Input eine Zahl zwischen 1-6 ist
for i in range(1, number):
    while True:
        try:
            value = float(input(f"Geben Sie Note {i} ein: "))
            if value <= 6:
                grades.append(value)
                break
            else:
                print("Ungültige Eingabe. Der Wert muss kleiner oder gleich 6 sein.")
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")

# Rechnet den Notendurchschnitt aus
average = sum(grades) / number_grades

print(average)