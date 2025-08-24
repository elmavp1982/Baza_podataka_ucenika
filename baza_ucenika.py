# Lista svih učenika
students = []

# Dodavanje novog učenika
def add_student():
    print("\n--- Dodavanje novog učenika ---")
    ime = input("Unesi ime učenika: ")
    godine = int(input("Unesi godine učenika: "))
    
    predmeti_input = input("Unesi predmete (odvojene zarezom): ")
    predmeti = [p.strip() for p in predmeti_input.split(",")]
    
    ocjene_input = input("Unesi ocjene (odvojene zarezom): ")
    ocjene = [int(o.strip()) for o in ocjene_input.split(",")]

    prosjek = sum(ocjene) / len(ocjene) if ocjene else 0

    student = {
        "ime": ime,
        "godine": godine,
        "predmeti": predmeti,
        "ocjene": ocjene,
        "prosjek": round(prosjek, 2)
    }

    students.append(student)
    print(f"Učenik {ime} je uspješno dodan.")

# Brisanje učenika po imenu
def remove_student():
    print("\n--- Brisanje učenika po imenu ---")
    ime_za_brisanje = input("Unesi ime učenika za brisanje: ").strip().lower()

    broj_prije = len(students)
    students = [s for s in students if s["ime"].lower() != ime_za_brisanje]
    broj_poslije = len(students)

    obrisano = broj_prije - broj_poslije

    if obrisano == 0:
        print("Nema učenika s tim imenom.")
    else:
        print(f"Uklonjeno {obrisano} učenika s imenom '{ime_za_brisanje}'.")

# Pretraga učenika po imenu
def find_student():
    print("\n--- Pretraga učenika po imenu ---")
    ime_za_trazenje = input("Unesi ime učenika za pretragu: ").strip().lower()

    pronadjeni = [s for s in students if s["ime"].lower() == ime_za_trazenje]

    if not pronadjeni:
        print("Nema učenika s tim imenom.")
        return

    for i, student in enumerate(pronadjeni, start=1):
        print(f"\nRezultat {i}:")
        print(f"  Ime: {student['ime']}")
        print(f"  Godine: {student['godine']}")
        print(f"  Predmeti: {', '.join(student['predmeti'])}")
        print(f"  Ocjene: {student['ocjene']}")
        print(f"  Prosjek: {student['prosjek']}")

# Prikaz učenika sa najboljim prosjekom
def find_best_student():
    print("\n--- Najbolji učenik ---")

    if not students:
        print("Nema unesenih učenika.")
        return

    def uzmi_prosjek(student):
        return student["prosjek"]

    najbolji = max(students, key=uzmi_prosjek)

    print(f"\n Najbolji učenik je: {najbolji['ime']}")
    print(f"  Godine: {najbolji['godine']}")
    print(f"  Predmeti: {', '.join(najbolji['predmeti'])}")
    print(f"  Ocjene: {najbolji['ocjene']}")
    print(f"  Prosjek: {najbolji['prosjek']}")

# Prikaz svih učenika
def show_all():
    print("\n--- Lista svih učenika ---")
    
    if not students:
        print("Nema unesenih učenika.")
        return

    for i, student in enumerate(students, start=1):
        print(f"\nUčenik {i}:")
        print(f"  Ime: {student['ime']}")
        print(f"  Godine: {student['godine']}")
        print(f"  Predmeti: {', '.join(student['predmeti'])}")
        print(f"  Ocjene: {student['ocjene']}")
        print(f"  Prosjek: {student['prosjek']}")

# Sortiranje po prosjeku
def get_average(student):
    return student["prosjek"]

def sort_by_average():
    print("\n--- Sortiranje učenika po prosjeku ---")

    if not students:
        print("Nema unesenih učenika.")
        return

    sortirani = sorted(students, key=get_average, reverse=True)

    for i, student in enumerate(sortirani, start=1):
        print(f"\nUčenik {i}:")
        print(f"  Ime: {student['ime']}")
        print(f"  Godine: {student['godine']}")
        print(f"  Prosjek: {student['prosjek']}")
        print(f"  Predmeti: {', '.join(student['predmeti'])}")
        print(f"  Ocjene: {student['ocjene']}")

# Filtriranje učenika po prosjeku većem od zadatog
def filter_by_average():
    print("\n--- Filtriranje učenika po prosjeku ---")

    if not students:
        print("Nema unesenih učenika.")
        return

    try:
        prag = float(input("Unesi minimalni prosjek (npr. 4.5): "))
    except ValueError:
        print("Neispravan unos. Molimo unesi broj.")
        return

    filtrirani = []
    for student in students:
        if student["prosjek"] >= prag:
            filtrirani.append(student)

    if not filtrirani:
        print(f"Nema učenika sa prosjekom većim od {prag}.")
        return

    for i, student in enumerate(filtrirani, start=1):
        print(f"\nUčenik {i}:")
        print(f"  Ime: {student['ime']}")
        print(f"  Godine: {student['godine']}")
        print(f"  Prosjek: {student['prosjek']}")
        print(f"  Predmeti: {', '.join(student['predmeti'])}")
        print(f"  Ocjene: {student['ocjene']}")

# Glavni meni
def main():
    while True:
        print("\n--- Baza podataka učenika ---")
        print("1. Dodaj učenika")
        print("2. Prikaži sve učenike")
        print("3. Pretraži učenika")
        print("4. Prikaži najboljeg učenika")
        print("5. Sortiraj po prosjeku")
        print("6. Filtriraj po prosjeku")
        print("7. Obriši učenika po imenu") 
        print("8. Izlaz")

        choice = input("Izaberi opciju (1-8): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_all()
        elif choice == "3":
            find_student()
        elif choice == "4":
            find_best_student()
        elif choice == "5":
            sort_by_average()
        elif choice == "6":
            filter_by_average()
        elif choice == "7":
            remove_student() 
        elif choice == "8":
            print("Doviđenja!")

            break
        else:
            print("Nepoznata opcija. Pokušaj ponovo.")

# Pokretanje programa
if __name__ == "__main__":
    main()
