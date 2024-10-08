import numpy as np

def sichere_auswertung(funktions_input, x_werte):
    """Bewertet die Eingabefunktion sicher."""
    try:
        # Erstellen einer Lambda-Funktion aus der Eingabe
        func = eval("lambda x: " + funktions_input)
        # Vektorisieren der Funktion für numpy-Arrays
        vektorisierte_func = np.vectorize(func)
        return vektorisierte_func(x_werte)
    except Exception as e:
        raise ValueError(f"Fehler beim Auswerten der Funktion: {e}")

def main():
    # Benutzereingaben
    funktions_input = input("f(x): ")
    x_min = float(input("minimalen Wert von x: "))
    x_max = float(input("maximalen Wert von x: "))
    step = float(input("Schrittweite: "))

    # Erstellen eines Arrays von x-Werten
    x_werte = np.arange(x_min, x_max, step)

    # Berechnen der y-Werte
    try:
        y_werte = sichere_auswertung(funktions_input, x_werte)
    except ValueError as e:
        print(e)
        return

    # Ausgabe der Ergebnisse
    print("\nErgebnisse:")
    for x, y in zip(x_werte, y_werte):
        print(f"f({x}) = {y}")

if __name__ == "__main__":
    main()
