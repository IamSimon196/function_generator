import random
import sympy as sp

# Definice proměnné
x = sp.Symbol('x')

# Pravděpodobnostní funkce pro délku výrazu
def pravdepodobnost_delky():
    base_prob = 0.8
    clen = 1
    while clen < 10 and random.random() < base_prob:
        clen += 1
        base_prob *= 0.5
    return clen

# Funkce pro generování členů v exponentové formě
def generuj_clen():
    a = random.randint(1, 10)
    n = random.choices(range(1, 5), weights=[5, 4, 3, 2], k=1)[0]

    if random.random() < 0.5:  
        return (a * x**n) / random.randint(1, 10)
    else:
        return a / (x ** n)  # Zlomek bude převeden níže na exponent

# Nekonečná smyčka pro opakované generování funkcí
while True:
    # Generování délky funkce
    delka = pravdepodobnost_delky()
    funkce = sum(generuj_clen() for _ in range(delka))

    # Převedení všech lomených výrazů na exponentový tvar
    funkce = sp.simplify(sp.expand_power_base(funkce, force=True))

    # Výpočet derivace a integrálu
    derivace = sp.simplify(sp.diff(funkce, x))
    integral = sp.simplify(sp.integrate(funkce, x))

    # Oprava výpisu log -> ln
    integral = integral.subs(sp.log(x), sp.Symbol("ln(x)"))

    # Zobrazení výsledků
    print("\n" + "-"*50)
    print()
    sp.pprint(funkce, use_unicode=True, num_columns=300)
    print()

    input("Stiskni Enter pro zobrazení derivace a integrálu...")

    print("\nDerivace:")
    print()
    sp.pprint(sp.simplify(derivace), use_unicode=True,num_columns=300)
    print()

    print("\nIntegrál:")
    print()
    sp.pprint(sp.simplify(integral), use_unicode=True, num_columns=300)
    print()
    print("+ C")

    input("\nStiskni Enter pro novou funkci nebo zavři program pro ukončení...")
