# 35. Transport yo‘nalishlari

class TransportRoute:
    def __init__(self, name, distance_km):
        self.name = name              # yo‘nalish nomi
        self.distance = distance_km   # masofa (km)

    def get_distance(self):
        """Yo‘nalish masofasi (km)"""
        return self.distance

    def __str__(self):
        return f"{self.name:14} | {self.distance:5.1f} km"


# -----------------------------------------------
# Voris sinflar (chiroyli chiqish + emoji)
# -----------------------------------------------

class BusRoute(TransportRoute):
    def __str__(self):
        dist = self.get_distance()
        return f"🚌 {self.name:12} → {dist:5.1f} km"


class MetroRoute(TransportRoute):
    def __str__(self):
        dist = self.get_distance()
        return f"🚇 {self.name:12} → {dist:5.1f} km"


# Qo‘shimcha misol uchun (foydali bo‘lishi mumkin)
class TaxiRoute(TransportRoute):
    def __str__(self):
        dist = self.get_distance()
        return f"🚖 {self.name:12} → {dist:5.1f} km"


# --------------------------------------------------
# Barcha yo‘nalishlar masofasini chiqarish
# --------------------------------------------------

def show_transport_routes(routes):
    print("\n" + "═" * 60)
    print("     TRANSPORT YO‘NALISHLARI — MASOFA HISOBI     ".center(60))
    print("═" * 60)
    print("Yo‘nalish turi         Masofa (km)")
    print("─" * 60)

    total_distance = 0

    for route in routes:
        print(route)
        total_distance += route.get_distance()

    print("─" * 60)
    print(f"Jami masofa (barcha yo‘nalishlar):       {total_distance:6.1f} km")
    print("═" * 60 + "\n")


# Test ma'lumotlari
yonallishlar = [
    BusRoute("Avtobus №12 (markaz–chilonzor)", 14.8),
    MetroRoute("Metro Chilanzor yo‘nalishi", 9.5),
    BusRoute("Avtobus №67 (yunusobod–sergeli)", 21.2),
    MetroRoute("Metro Yunusobod yo‘nalishi", 12.3),
    TaxiRoute("Taksi (uy–ish)", 7.5),
]

show_transport_routes(yonallishlar)


# Sizning misol qiymatlaringiz bilan:
print("\nSizning misol yo‘nalishlaringiz:\n")
misol_yonallishlar = [
    BusRoute("Avtobus", 15),
    MetroRoute("Metro", 10),
]

show_transport_routes(misol_yonallishlar)
