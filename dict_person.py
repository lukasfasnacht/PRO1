import json

personas = {
    "Vorname": ["Men"],
    "Nachname": ["Zimmermann"],
    "Alter": [23],
    "Stadt": ["Chur"]
}

# Formatiert unser dict in eine json ähnliche Liste. Indent gibt an wie viele Leerschläge die Einrückung der versch. Attribute haben
format_personas = json.dumps(personas, indent=4)

print(format_personas)