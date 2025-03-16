from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 14", "+79001234567"),
    Smartphone("Samsung", "Galaxy S22", "+79009876543"),
    Smartphone("Xiaomi", "Mi 11", "+79007654321")
]


for phone in catalog:
    phone.print_info()
