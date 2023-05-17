import baraja
print(baraja.crear_baraja(['A','1','2','3','4','5','6','7','8','C','R'],['O','C','B','E']))


b = baraja.crear_baraja("A23456789SCR","OCEB")
print(b)
print()
print()
print()

baraja.barajar_for(b)
print(b)