print ("Izvēlies konversiju: 1) km<->mi  2) kg<->lb  3) L<->gal")
choice = input("# > ") #ievadam numuru izvēlēties. Choise definējam kā input lai pēc tam rakstītu if loop pēc izvēles
if choice=="1": #obligāte vajag":" pēc if statement
  print("# Virziens: 1) km -> mi  2) mi -> km")
  direction=input("# > ")
  value=float(input("Ievadi vērtību:")) #float parvērš ievadi par decimalskaitli, jo input vienmēr ir teksts(string) Ar šo definējam cik km vai mi jāpārvērš
  if direction=="1":
    result = value*0.621371
    print(f"#{value:.2f} km={result:.2f} mi") #f string ļauļ ievietot mainīgo tekstā.  2f norāda ka value un result ir decimalskaitlis ar 2 cipariem aiz komata
  elif direction=="2":
    result = value/0.621371
    print(f"#{value:.2f} mi= {result:.2f}km")
elif choice=="2":
  print("#Virziens: 1)kg->lb 2)lb->kg")
  direction=input("#>")
  value=float(input("#Ievadi vērtību"))
  if direction == "1":
        result = value * 2.20462
        print(f"# {value:.2f} kg = {result:.2f} lb")
  elif direction == "2":
        result = value / 2.20462
        print(f"# {value:.2f} lb = {result:.2f} kg")
elif choice == "3":
    print("# Virziens: 1) L -> gal  2) gal -> L")
    direction = input("# > ")
    value = float(input("# Ievadi vērtību: "))

    if direction == "1":
        result = value * 0.264172
        print(f"# {value:.2f} L = {result:.2f} gal")
    elif direction == "2":
        result = value / 0.264172
        print(f"# {value:.2f} gal = {result:.2f} L")
else:
    print("# Nepareiza izvēle")