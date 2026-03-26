# import hermetyzacja

import pakiet

# pakiet.powitanie()
# AttributeError: module 'pakiet' has no attribute 'powitanie'

from pakiet import fun

fun.powitanie()  # Hello!

import pakiet.fun as pk

pk.powitanie()  # Hello!

# po dopisaniu w __init__ i __all__
pakiet.info()  # Pakiet v1.23.678
