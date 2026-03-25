class Contact:
    all_contacts = []  # wspolna lista dla wszystkich obiejktow tej klasy
    x = 'TEST'

    def __init__(self, name, email):
        """

        :param name:
        :param mail:
        """
        self.name = name
        self.email = email

        Contact.all_contacts.append(self)

    def __repr__(self):
        return f"{self.name} {self.email}"


c1 = Contact("Radek", "radek@wp.pl")
c2 = Contact("Anna", "anna@wp.pl")
c3 = Contact("Tomek", "tomek@wp.pl")
print(c1.all_contacts)  # [Radek radek@wp.pl, Anna anna@wp.pl, Tomek tomek@wp.pl]
# bez obiektu
print(Contact.all_contacts)  # [Radek radek@wp.pl, Anna anna@wp.pl, Tomek tomek@wp.pl]

print(c1.x)
print(Contact.x)
# TEST
# TEST
c2.x = "TEST2"
print(Contact.x)  # TEST
print(c2.x)  # TEST2
print(c1.x)  # TEST


class Suplier(Contact):
    """
    Klasa dziedziczy po klasie contact
    """

    def order(self, order):
        print(f'{order} zamówiono od {self.name}')


sup1 = Suplier('Marek', "marek@wp.pl")
print(sup1)  # Marek marek@wp.pl
print(sup1.all_contacts)
# [Radek radek@wp.pl, Anna anna@wp.pl, Tomek tomek@wp.pl, Marek marek@wp.pl]
print(Suplier.all_contacts)
# [Radek radek@wp.pl, Anna anna@wp.pl, Tomek tomek@wp.pl, Marek marek@wp.pl]
sup1.order("kawa")  # kawa zamówiono od Marek

print(c1)
print(c2)
print(c3)
print(sup1)
# Radek radek@wp.pl
# Anna anna@wp.pl
# Tomek tomek@wp.pl
# Marek marek@wp.pl
