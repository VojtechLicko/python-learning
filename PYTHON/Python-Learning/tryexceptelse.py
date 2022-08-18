try:
    a = int(input("Zadej číslo: "))
except:
    print("zadej číslo: ")
else:
    print("mám pravdu")
finally:
    print("finally statement")
seznam = range(1, 10, 2)
