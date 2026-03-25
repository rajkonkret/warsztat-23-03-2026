from pprint import pprint


class ContactList(list['Contact']):

    def search(self, name):
        matching_contact = []
        for c in self:
            if name.casefold().strip() in c.name.casefold().strip():
                matching_contact.append(c)
        return matching_contact


class Contact:
    # all_contacts = []  # wspolna lista dla wszystkich obiejktow tej klasy
    all_contacts = ContactList()  # wspolna lista dla wszystkich obiejktow tej klasy
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
c4 = Contact("Radek", "radek@wp.pl")
c2 = Contact("Anna", "anna@wp.pl")
c3 = Contact("Tomek", "tomek@wp.pl")
print(c1.all_contacts)  # [Radek radek@wp.pl, Anna anna@wp.pl, Tomek tomek@wp.pl]
# bez obiektu
print(Contact.all_contacts)  # [Radek radek@wp.pl, Anna anna@wp.pl, Tomek tomek@wp.pl]
# print(Contact.all_contacts.search("Radek"))
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

#
print(Contact.all_contacts.search("Radek"))  # [Radek radek@wp.pl]
# [Radek radek@wp.pl, Radek radek@wp.pl]
contact_list = ContactList()
print(contact_list)  # []
print(contact_list.search("radek"))  # []

osoba = Contact.all_contacts.search("Radek")
print(osoba)
# [Radek radek@wp.pl, Radek radek@wp.pl]
for i in osoba:
    print(i)
    print(i.name)
    print(i.email)


# Radek radek@wp.pl
# Radek
# radek@wp.pl

class Friend(Suplier):
    """
    Klasa dziedziczy po kalsie Suplier
    """

    def __init__(self, name, email, phone="000000000"):
        super().__init__(name, email)  # super() klasa nadrzedna, musimy wywołac metode __init__
        self.phone = phone

    def __repr__(self):
        return f"{self.name} {self.email} +48{self.phone}"


f1 = Friend("Marek", "marek@gov.pl")
f2 = Friend("Kamil", "kamil@gov.pl", "890987811")

print(f1, f2)  # Marek marek@gov.pl +48000000000 Kamil kamil@gov.pl +48890987811

print(Contact.all_contacts)
# [Radek radek@wp.pl, Radek radek@wp.pl, Anna anna@wp.pl, Tomek tomek@wp.pl, Marek marek@wp.pl, Marek marek@gov.pl +48000000000, Kamil kamil@gov.pl +48890987811]

print(Contact.all_contacts.search("Kamil"))  # [Kamil kamil@gov.pl +48890987811]

print(Contact.all_contacts)
# [Radek radek@wp.pl,
# Radek radek@wp.pl,
# Anna anna@wp.pl,
# Tomek tomek@wp.pl,
# Marek marek@wp.pl,
# Marek marek@gov.pl +48000000000,
# Kamil kamil@gov.pl +48890987811]

pprint(Contact.all_contacts)
# [Radek radek@wp.pl,
#  Radek radek@wp.pl,
#  Anna anna@wp.pl,
#  Tomek tomek@wp.pl,
#  Marek marek@wp.pl,
#  Marek marek@gov.pl +48000000000,
#  Kamil kamil@gov.pl +48890987811]

# kolejność rozwiązywane nazw metod (pól) dla obiektu
pprint(Friend.__mro__)
# (<class '__main__.Friend'>,
#  <class '__main__.Suplier'>,
#  <class '__main__.Contact'>,
#  <class 'object'>)
