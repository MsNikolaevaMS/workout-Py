from smartphone import Smartphone


catalog = []


catalog.append(Smartphone("Apple", "iPhone 14", "+79161234567"))
catalog.append(Smartphone("Samsung", "Galaxy S22", "+79051234567"))
catalog.append(Smartphone("Google", "Pixel 6", "+79151234567"))
catalog.append(Smartphone("OnePlus", "9 Pro", "+79061234567"))
catalog.append(Smartphone("Xiaomi", "Mi 11", "+79171234567"))


for smartphone in catalog:
    print(f"{smartphone.brand}-{smartphone.model}.{smartphone.phone_number}")
