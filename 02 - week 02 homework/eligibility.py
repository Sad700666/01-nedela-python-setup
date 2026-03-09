age=int(input('Ievadi savu vecumu:'))
license_input = input("Vai ir autovadītāja apliecība? (j/n): ").lower()
student_input = input("Vai ir students? (j/n): ").lower()
veteran_input = input("Vai ir veterāns? (j/n): ").lower() #Rakstot colab AI piedāvā likt .lower() Tā ir funkcija kas padara ievadīto tekstu mazajiem burtiem.

has_license = license_input == 'j'
is_student = student_input =="j"
is_veteran = veteran_input =="j"

can_vote= age >=18
car_rent= age >=21 and has_license
student_discount= 16<= age <=26 and is_student
veteran_discount= age >=65 or is_veteran

vote_result="Jā" if can_vote else "Nē"
rent_result="Jā" if car_rent else "Nē"
student_result="Jā" if student_discount else "Nē"
veteran_result="Jā" if veteran_discount else "Nē"

print(f"Balsošana:        {vote_result}")
print(f"Auto īre:         {rent_result}")
print(f"Senioru atlaide:  {veteran_result}")
print(f"Studentu atlaide: {student_result}")