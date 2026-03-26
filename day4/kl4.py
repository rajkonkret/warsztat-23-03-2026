# słownik
# gdy nie ma klucza w słowniku: KeyError
# __missing__ - wykonywana gdy nie ma klucza w słowniku
class DefaultDict(dict):
    def __missing__(self, key):
        return "default"


d1 = DefaultDict()
print(type(d1))  # <class '__main__.DefaultDict'>
print(d1)
print(d1['name'])  # default

d1 = {}  # pusty słownik
print(type(d1))  # {}


# print(d1['name'])  # KeyError: 'name'

# słownik w którym, gdy nie ma klucza, tworzy taki klucz z wartością domyslna np.: 0
class AutoDict(dict):
    def __missing__(self, key):
        self[key] = 0
        return key


a1 = AutoDict()
print(a1)  # {}
print(a1['name'])  # name
print(a1)  # {'name': 0}
print(a1['name'])  # 0


# zmienia klucze na małe litera
class CaseInsensitiveDict(dict):
    def __missing__(self, key):
        # return self.get(key.lower())
        if isinstance(key, str):  # sprawdzenie czy klucz jest str
            return self.get(key.lower())
        return key


c1 = CaseInsensitiveDict()
c1['name'] = 'Radek'
print(c1)  # {'name': 'Radek'}
print(c1['Name'])  # Radek
print(c1['age'])  # None

# c1[1] = 10
print(c1[1])  # AttributeError: 'int' object has no attribute 'lower'
