from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S26", '+79163456789'),
    Smartphone("Samsung", "Galaxy S25 Ultra", '+79207896760'),
    Smartphone("Samsung", "Galaxy S25 Plus", '+79263456735'),
    Smartphone("Samsung", "Galaxy A37", '+79178954566'),
    Smartphone("Samsung", "Galaxy S25 Edge", '+79163768309')
    ]

for smartphone in catalog:
    print(f'{smartphone.brand}, {smartphone.model}, {smartphone.number}')
