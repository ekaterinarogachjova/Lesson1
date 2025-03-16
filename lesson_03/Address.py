class Address:
    def __init__(self, index, city, street, house, apartment):

        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def print_address(self):

        return f"{self.index}, {self.city}, {self.street}, {self.house}, {self.apartment}"  # noqa: E501
