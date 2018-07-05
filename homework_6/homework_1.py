class Car:
    def __init__(self, name, color, year, price):
        self.name = name
        self.color = color
        self.year = year
        self.price = price

    def __str__(self):
        string = 'Name: {}\nColor: {}\nYear: {}\nPrice: {}'.format(
            self.name,
            self.color,
            self.year,
            self.price
        )
        return string

#car1 = Car('BMW', 'Red', '2010', '$10000')

#print(car1)
