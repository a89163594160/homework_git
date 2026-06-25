from address import Address
from mailing import Mailing

from_add = Address('123123', 'Москва', 'Твардовского', 2, 100)
to_add = Address('987654', 'Тамбов', 'Отдыха', '7', '2')
mailing1 = Mailing(to_add, from_add, track='rt34576889', cost=457)

print(f"Отправление {mailing1.track} из {from_add} в {to_add}. Стоимость "
      f"{mailing1.cost} рублей.")
