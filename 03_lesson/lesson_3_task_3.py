from address import Address
from mailing import Mailing


to_address = Address("625023", "Тюмень", "Республики", "196", "11")
from_address = Address("620075", "Екатеринбург", "Малышева", "51", "2")


mailing = Mailing(to_address, from_address, 5945.45, "TRK123456")

# Печатаем информацию об отправлении в нужном формате
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house}-{mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
