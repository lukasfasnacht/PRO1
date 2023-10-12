personas = {
    "Vorname": ["Men"],
    "Nachname": ["Zimmermann"],
    "Alter": [23],
    "Stadt": ["Chur"]
}

personas["Vorname"].append("Noa")
personas["Nachname"].append("Roth")
personas["Alter"].append(23)
personas["Stadt"].append("Solothurn")

for i in range(len(personas["Vorname"])):
    print(f"Vorname: {personas['Vorname'][i]}")
    print(f"Nachname: {personas['Nachname'][i]}")
    print(f"Alter: {personas['Alter'][i]}")
    print(f"Stadt: {personas['Stadt'][i]}")
    print()
