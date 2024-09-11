from random input randint
rule = input("Skriv om ni spelar udda eller jämna:")
computer = randint(1, 6)
player = randint(1, 6)

if rule == "udda"
computer = computer % computer 
else:
print"jämnt"