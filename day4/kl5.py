# longest() - znajduje najdłuższy klucz w słowniku
class LongestKeyDict(dict):

    def longest_key(self):
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key
        return longest


art = LongestKeyDict()
art['tomasz'] = 12
art['abraham'] = 8
art['zen'] = 2
print(art.longest_key())  # abraham
