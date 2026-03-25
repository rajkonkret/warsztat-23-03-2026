import wycieczka

print(25 * "-")
rabaty = [0, 5, 10, 15, 20]
for r in rabaty:
    kw = wycieczka.kwota(
        transport=500,
        nocleg=800,
        wyzywienie=300,
        wycieczki=300,
        ubezpiecenie=100,
        inne=50,
        rabat=r
    )
    print(f"Rabat: {r:>3} -> {kw:.2f} zł")
# -------------------------
# Rabat:   0 -> 2050.00 zł
# Rabat:   5 -> 1985.00 zł
# Rabat:  10 -> 1920.00 zł
# Rabat:  15 -> 1855.00 zł
# Rabat:  20 -> 1790.00 zł