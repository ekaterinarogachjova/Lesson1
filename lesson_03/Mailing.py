class Mailing:
    def __init__(self, to_address, from_address, cost, track):

        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def print_mailing_info(self):

        print(
            f"Отправление {self.track} из {self.from_address.print_address()} в {self.to_address.print_address()}. Стоимость {self.cost} рублей.")  # noqa: E501
