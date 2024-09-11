print("Hej och välkommen till mitt program")

namn = input("Vad heter du, skriv ditt namn här:")

print(f"hej {namn} Vad kul att du är här!")

print("Jag undrar hur gammal du är?")
user_age = input("Skriv din ålder ")
print(f"Tack, vad roligt att du är {user_age} år gammal")
user_age_converted = int(user_age)
if user_age_converted >= 15:

    print("Du får köra moppen.")
else:
    print("DU får ej köra moppen")

    #lektion nummer 2