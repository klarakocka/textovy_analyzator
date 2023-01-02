"""
textovyanalfinverze.py: prvni projekt do Engeto Online Python Akademie

author: Klara Kocikova
email: klara_hamplova@seznam.cz
discord: KlaraK#9112
"""

cara = ".♡." * 15

username = input("Please enter your login name: ")
password = input("Please enter your password: ")

users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

print(cara)

if users.get(username) == password:
    print(f"Welcome to the app, {username}.","\nWe have 3 texts to be analyzed.")
else:
    print("Unregistered user, terminating the program...")
    quit()


text_1 = {"cislo": 1, "text": (""" Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.""")}

text_2 = {"cislo": 2, "text": ("""At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""")}

text_3 = {"cislo": 3, "text": ("""The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.""")}


print(cara, "\n", cara)
print(text_1.get("cislo"), text_1.get("text"))
print(text_2.get("cislo"), text_2.get("text"))
print(text_3.get("cislo"), text_3.get("text"))


texts = {text_1["cislo"]: text_1["text"],
         text_2["cislo"]: text_2["text"],
         text_3["cislo"]: text_3["text"]}


print(cara, "\n", cara)
uzivatel = input("Enter a number between 1 and 3 to select:")

if uzivatel.isdigit() == False:
    print("Your selection must be a number.")
    quit()


uzivatel = int(uzivatel)
print(uzivatel)

if uzivatel < 1 or uzivatel > 3:
    print("Your selection must be a number between 1-3.")
    quit()
else:
    print(texts[uzivatel])

print(cara, "\n", cara)


vybrany_text = (texts[uzivatel]).replace("\n", " ")


pocet_slov = vybrany_text.split(" ")
print("There are", len(pocet_slov), "words in the selected text.")

prvni_velky = 0
vsechna_velka = 0
vsechna_mala = 0
pocet_cisel = 0
suma_cisel = 0
for slovo in pocet_slov:
    if slovo.istitle():
        prvni_velky = prvni_velky + 1
    if slovo.isupper():
        vsechna_velka = vsechna_velka + 1
    if slovo.islower():
        vsechna_mala = vsechna_mala + 1
    if slovo.isdigit():
        pocet_cisel = pocet_cisel + 1
        suma_cisel = suma_cisel + int(slovo)

print(cara, "\n", cara)

print("There are", prvni_velky, "titlecase words.")
print("There are", vsechna_velka, "uppercase words.")
print("There are", vsechna_mala, "lowercase words.")
print("There are", pocet_cisel, "numeric strings.")
print(f"The sum of all the numbers is {suma_cisel}.")

print(cara, "\n", cara)


horni_nadpis_tabulky = "LEN     |OCCURENCES         |NR"
print(horni_nadpis_tabulky)


pocet_delek = {}  
for slovo in pocet_slov:  
    delka_slova = len(slovo)  
    pocet_delek[delka_slova] = pocet_delek.get(delka_slova, 0) + 1

for klic in sorted(pocet_delek.keys()):
    width = 18 - int(pocet_delek[klic]) 
    print(klic, "\t|", "♡" * pocet_delek[klic], "|".rjust(width), pocet_delek[klic])
