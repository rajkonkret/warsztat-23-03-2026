from xyz import XYZ
from regular import Regular

xyz1 = XYZ(1, 2, 3)
print(xyz1.info("xyz 001"))
print(f"Policz: {xyz1.policz()}")
# xyz 001xyz 001xyz 001
# Policz: 5
xyz1.msg()
# Metoda nieabstrakcyjna klasy abstrakcyjnej

rg = Regular(3, 4)
print(rg.info("Tekst"))
print(f"Policz: {rg.policz()}")
rg.msg()
# Wiadomość: Tekst
# Policz: 3.0
# Metoda nieabstrakcyjna klasy abstrakcyjnej

# polimorfizm
# obiekty różnych klas możemy potraktowac jak
# obiekty jednej wspólnej klasy
# zapewnia nam to klasa abstrakcyjna
lista = [rg, xyz1]
for i in lista:
    print(i.policz())
# 3.0
# 5
