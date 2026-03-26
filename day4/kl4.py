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
