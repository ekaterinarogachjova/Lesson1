from Address import Address
from Mailing import Mailing


from_address = Address("123456", "Москва", "Ленина", "12", "34")
to_address = Address("987654", "Санкт-Петербург", "Невского", "78", "90")


mailing = Mailing(to_address, from_address, 1500, "ABC123456789")


mailing.print_mailing_info()
